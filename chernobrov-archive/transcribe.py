#!/home/liker2/asrp-audit/UAP_Reverse_Engineering_Study/.venv/bin/python3
"""Download, extract audio, and transcribe Chernobrov/Kosmopoisk videos via OpenAI Whisper API."""

import os, subprocess, json, time
from pathlib import Path
from openai import OpenAI

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
client = OpenAI(api_key=OPENAI_API_KEY)

BASE_DIR = Path("/home/liker2/asrp-audit/UAP_Reverse_Engineering_Study/chernobrov-archive")
AUDIO_DIR = BASE_DIR / "audio"
TRANSCRIPT_DIR = BASE_DIR / "transcripts"
CHUNKS_DIR = BASE_DIR / "chunks"
STATUS_FILE = BASE_DIR / "status.json"

TRANSCRIPT_DIR.mkdir(exist_ok=True)
CHUNKS_DIR.mkdir(exist_ok=True)

MAX_CHUNK_SIZE_MB = 24

INTERVIEWS = [
    ("01", "01_Chernobrov_MashinaVremeni_2h37",           "https://youtu.be/fAeumSyWHAk", "Чернобров. Машина Времени (2h37)"),
    ("02", "02_Chernobrov_MashinaVremeni_LAI_1h46",       "https://youtu.be/-lmeYxV8Iuw", "Чернобров. Машина Времени — ЛАИ (1h46)"),
    ("03", "03_Chernobrov_MashinaVremeni_41min",          "https://youtu.be/NFcLDb-aWZ0", "Чернобров. Машина Времени (41 мин)"),
    ("04", "04_Chernobrov_MashinaVremeni_1h46_alt",       "https://youtu.be/LnrWHa4w4os", "Чернобров. Машина Времени (1h46, alt)"),
    ("05", "05_Gaiduchok_traveler_58min",                 "https://youtu.be/-BL3H9obTDs", "Гайдучок — человек из будущего (58 мин)"),
    ("06", "06_SlediPutesh_2h55",                         "https://youtu.be/RxV7dDXoMLg", "Как найти следы путешественников во Времени (2h55)"),
    ("07", "07_MashinaVremeni_Hronoput_3h04",             "https://youtu.be/9k-mlSfU9V0", "Машина Времени и хронопутешествия (3h04)"),
    ("08", "08_3zvezdnie_NLO_22min",                      "https://youtu.be/4YGeR1KsXy0", "Трёхзвёздные НЛО (22 мин)"),
    ("09", "09_ParallelnyeMiry_39min",                    "https://youtu.be/I2u233WU0fY", "Параллельные миры (39 мин)"),
    ("10", "10_KakUstroenoVremya_2011_11min",             "https://youtu.be/-RC75ZeAfsE", "Как устроено Время (2011, 11 мин)"),
    ("11", "11_MashinaVremeni_GhostHunters_1h45",         "https://youtu.be/_kvcAfBqOmE", "Машина времени — Ghost Hunters (1h45)"),
    ("12", "12_MashinaVremeni_Chernobrov_46min",          "https://youtu.be/ff4bB3kUMi4", "Машина Времени Черноброва (46 мин)"),
    ("13", "13_Hronoput_Murom_2h37",                      "https://youtu.be/yeL7msYWhxc", "Хронопутешествия — Муром (2h37)"),
    ("14", "14_ZagadkiVremeni_25min",                     "https://youtu.be/ITxwY3oOM4I", "Загадки Времени (25 мин)"),
    ("15", "15_MedveditskayaGryada_docfilm_2017_32min",   "https://youtu.be/zAfnwTj5bW8", "Медведицкая гряда (док.фильм 2017, 32 мин)"),
    ("16", "16_KrugiNaPolyakh_2013_2h57",                 "https://youtu.be/LBTUqPvaMe8", "Круги на полях (2013, 2h57)"),
    ("17", "17_NLO_dolya_pravdy_2h24",                    "https://youtu.be/-l4tzEFcfWE", "НЛО — доля правды, домысла и лжи (2h24)"),
    ("18", "18_Kosmopoisk_MashinaVremeni_N24_58min",      "https://youtu.be/G240ne2rx_s", "Космопоиск. Машина времени на Новости 24 (58 мин)"),
    ("19", "19_GravitatsionnyeAnomalii_12min",            "https://youtu.be/hbg5ATAyq2s", "Гравитационные аномалии (12 мин)"),
]

def load_status():
    return json.loads(STATUS_FILE.read_text()) if STATUS_FILE.exists() else {}

def save_status(s):
    STATUS_FILE.write_text(json.dumps(s, indent=2, ensure_ascii=False))

def bar(cur, tot, w=30):
    f = int(w * cur/tot) if tot else 0
    return f"[{'#'*f}{'-'*(w-f)}] {cur}/{tot}"

def split_audio(audio_path, filename_base):
    ap = Path(audio_path)
    size_mb = ap.stat().st_size / (1024*1024)
    if size_mb <= MAX_CHUNK_SIZE_MB:
        return [str(ap)]
    r = subprocess.run(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",str(ap)],
                       capture_output=True, text=True)
    dur = float(r.stdout.strip())
    num = int(size_mb / MAX_CHUNK_SIZE_MB) + 1
    chunk_dur = int(dur / num)
    cd = CHUNKS_DIR / filename_base
    cd.mkdir(exist_ok=True)
    chunks = []
    for i in range(num + 2):
        start = i * chunk_dur
        if start >= dur: break
        cp = cd / f"chunk_{i:03d}.mp3"
        if not cp.exists() or cp.stat().st_size < 1000:
            subprocess.run(["ffmpeg","-i",str(ap),"-ss",str(start),"-t",str(chunk_dur),"-q:a","5",str(cp),"-y"],
                           capture_output=True)
        chunks.append(str(cp))
    return chunks

def transcribe_audio(audio_path, lang="ru"):
    with open(audio_path, "rb") as f:
        for attempt in range(5):
            try:
                return client.audio.transcriptions.create(
                    model="whisper-1", file=f, language=lang,
                    response_format="verbose_json", timestamp_granularities=["segment"])
            except Exception as e:
                print(f"      retry {attempt+1}: {e}", flush=True)
                time.sleep(5*(attempt+1))
                f.seek(0)
    return None

def format_transcript(r, offset=0):
    lines = []
    if hasattr(r, 'segments') and r.segments:
        for s in r.segments:
            start = (s.start if hasattr(s, 'start') else 0) + offset
            text = (s.text if hasattr(s, 'text') else '').strip()
            if text:
                h, m, sc = int(start//3600), int((start%3600)//60), int(start%60)
                lines.append(f"[{h:02d}:{m:02d}:{sc:02d}] {text}")
    elif hasattr(r, 'text'):
        lines.append(r.text)
    return "\n".join(lines)

def main():
    status = load_status()
    total = len(INTERVIEWS)
    print(f"=== Chernobrov Transcription Pipeline ===", flush=True)
    done_pre = sum(1 for e, *_ in INTERVIEWS if status.get(e, {}).get("transcribed"))
    print(f"Already done: {done_pre}/{total}\n", flush=True)

    for i, (eid, fname, url, desc) in enumerate(INTERVIEWS):
        if status.get(eid, {}).get("transcribed"):
            print(f"{bar(i+1, total)} SKIP  {desc}", flush=True)
            continue

        audio_path = AUDIO_DIR / f"{fname}.mp3"
        if not audio_path.exists() or audio_path.stat().st_size < 10000:
            print(f"{bar(i+1, total)} MISSING audio for {desc} — skipping for now", flush=True)
            status[eid] = {"status": "audio_missing"}
            save_status(status)
            continue

        size_mb = audio_path.stat().st_size / (1024*1024)
        print(f"{bar(i+1, total)} START {desc} ({size_mb:.1f}MB)", flush=True)

        chunks = split_audio(str(audio_path), fname)
        print(f"  → {len(chunks)} chunk(s)", flush=True)

        all_text = []
        offset = 0
        for ci, cp in enumerate(chunks):
            print(f"  chunk {ci+1}/{len(chunks)} ...", end="", flush=True)
            r = transcribe_audio(cp)
            probe = subprocess.run(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",cp],
                                   capture_output=True, text=True)
            dur = float(probe.stdout.strip()) if probe.stdout.strip() else 0
            if r:
                all_text.append(format_transcript(r, offset=offset))
                print(f" OK", flush=True)
            else:
                all_text.append(f"[CHUNK {ci} FAILED]")
                print(f" FAIL", flush=True)
            offset += dur

        tp = TRANSCRIPT_DIR / f"{fname}.txt"
        header = f"# {desc}\n# Source: {url}\n# Transcribed: {time.strftime('%Y-%m-%d %H:%M')}\n\n"
        tp.write_text(header + "\n".join(all_text))
        kb = tp.stat().st_size // 1024
        print(f"  ✓ saved to {tp.name} ({kb}KB)", flush=True)

        status[eid] = {"status": "transcribed", "transcribed": True,
                       "audio": str(audio_path), "transcript": str(tp), "chunks": len(chunks)}
        save_status(status)

    done = sum(1 for e, *_ in INTERVIEWS if status.get(e, {}).get("transcribed"))
    print(f"\n=== DONE === {done}/{total} transcribed", flush=True)

if __name__ == "__main__":
    main()
