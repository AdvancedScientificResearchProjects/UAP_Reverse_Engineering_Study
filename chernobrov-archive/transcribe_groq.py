#!<repo>/.venv/bin/python3
"""Transcribe Chernobrov corpus via Groq Whisper-large-v3 with rate limiting.

Groq free tier limits:
- 2h audio/hour
- 8h audio/day
- 25MB file size cap per request
"""

import os, subprocess, json, time
from pathlib import Path
from collections import deque
import requests

GROQ_API_KEY = os.environ["GROQ_API_KEY"]
GROQ_URL = "https://api.groq.com/openai/v1/audio/transcriptions"
MODEL = "whisper-large-v3"

BASE_DIR = Path("<repo>/chernobrov-archive")
AUDIO_DIR = BASE_DIR / "audio"
TRANSCRIPT_DIR = BASE_DIR / "transcripts"
CHUNKS_DIR = BASE_DIR / "chunks"
STATUS_FILE = BASE_DIR / "status.json"
USAGE_FILE = BASE_DIR / "groq_usage.json"

# Rate limiting: file size 25MB, audio bitrate ~90kbps mp3 ≈ ~37 min per 25MB
# Chunks ~20 min safe. Groq: 2h per rolling hour, 8h per rolling day.
MAX_CHUNK_SEC = 20 * 60   # 20 min chunks (well under 25MB)
HOUR_CAP_SEC = 2 * 3600 * 0.90   # 90% of 2h = 1h48m safety margin
DAY_CAP_SEC = 8 * 3600 * 0.90    # 90% of 8h = 7h12m

INTERVIEWS = [
    ("01", "01_Chernobrov_MashinaVremeni_2h37"),
    ("02", "02_Chernobrov_MashinaVremeni_LAI_1h46"),
    ("03", "03_Chernobrov_MashinaVremeni_41min"),
    ("04", "04_Chernobrov_MashinaVremeni_1h46_alt"),
    ("05", "05_Gaiduchok_traveler_58min"),
    ("06", "06_SlediPutesh_2h55"),
    ("07", "07_MashinaVremeni_Hronoput_3h04"),
    ("08", "08_3zvezdnie_NLO_22min"),
    ("09", "09_ParallelnyeMiry_39min"),
    ("10", "10_KakUstroenoVremya_2011_11min"),
    ("11", "11_MashinaVremeni_GhostHunters_1h45"),
    ("12", "12_MashinaVremeni_Chernobrov_46min"),
    ("13", "13_Hronoput_Murom_2h37"),
    ("14", "14_ZagadkiVremeni_25min"),
    ("15", "15_MedveditskayaGryada_docfilm_2017_32min"),
    ("16", "16_KrugiNaPolyakh_2013_2h57"),
    ("17", "17_NLO_dolya_pravdy_2h24"),
    ("18", "18_Kosmopoisk_MashinaVremeni_N24_58min"),
    ("19", "19_GravitatsionnyeAnomalii_12min"),
]

def load_status():
    return json.loads(STATUS_FILE.read_text()) if STATUS_FILE.exists() else {}

def save_status(s):
    STATUS_FILE.write_text(json.dumps(s, indent=2, ensure_ascii=False))

def load_usage():
    if USAGE_FILE.exists():
        u = json.loads(USAGE_FILE.read_text())
        u["events"] = deque(u.get("events", []))
        return u
    return {"events": deque()}

def save_usage(u):
    USAGE_FILE.write_text(json.dumps({"events": list(u["events"])}, indent=2))

def audio_duration(path):
    r = subprocess.run(["ffprobe","-v","quiet","-show_entries","format=duration","-of","csv=p=0",str(path)],
                       capture_output=True, text=True)
    return float(r.stdout.strip()) if r.stdout.strip() else 0

def split_audio(audio_path, filename_base):
    dur = audio_duration(audio_path)
    if dur <= MAX_CHUNK_SEC:
        return [str(audio_path)]
    cd = CHUNKS_DIR / filename_base
    cd.mkdir(exist_ok=True, parents=True)
    chunks = []
    i = 0
    start = 0
    while start < dur:
        cp = cd / f"chunk_{i:03d}.mp3"
        if not cp.exists() or cp.stat().st_size < 1000:
            subprocess.run(["ffmpeg","-i",str(audio_path),"-ss",str(start),"-t",str(MAX_CHUNK_SEC),
                            "-q:a","5",str(cp),"-y"], capture_output=True)
        chunks.append(str(cp))
        start += MAX_CHUNK_SEC
        i += 1
    return chunks

def check_rate_limit(usage, next_sec):
    """Wait if we'd exceed rate limits. Returns when safe to proceed."""
    now = time.time()
    # Prune old events
    while usage["events"] and now - usage["events"][0][0] > 24 * 3600:
        usage["events"].popleft()

    hour_used = sum(sec for t, sec in usage["events"] if now - t <= 3600)
    day_used = sum(sec for t, sec in usage["events"])

    print(f"  [rate] last-hour: {hour_used/60:.1f}min, last-24h: {day_used/60:.1f}min, next: {next_sec/60:.1f}min",
          flush=True)

    # Wait if over hour cap
    if hour_used + next_sec > HOUR_CAP_SEC:
        # sleep until oldest in-hour event expires
        oldest = min(t for t, _ in usage["events"] if now - t <= 3600)
        wait = int(oldest + 3600 - now) + 30
        print(f"  [rate] hour cap reached. Sleeping {wait}s...", flush=True)
        time.sleep(wait)
    # Wait if over day cap
    if day_used + next_sec > DAY_CAP_SEC:
        oldest = usage["events"][0][0]
        wait = int(oldest + 24*3600 - now) + 60
        print(f"  [rate] day cap reached. Sleeping {wait}s ({wait/60:.0f}min)...", flush=True)
        time.sleep(wait)

def transcribe_chunk(audio_path):
    with open(audio_path, "rb") as f:
        files = {"file": (Path(audio_path).name, f, "audio/mpeg")}
        data = {
            "model": MODEL,
            "language": "ru",
            "response_format": "verbose_json",
            "timestamp_granularities[]": "segment",
        }
        headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
        for attempt in range(5):
            try:
                resp = requests.post(GROQ_URL, headers=headers, files=files, data=data, timeout=600)
                if resp.status_code == 200:
                    return resp.json()
                if resp.status_code == 429:
                    retry_after = int(resp.headers.get("retry-after", 60))
                    print(f"    [429] rate limit hit. Sleeping {retry_after}s...", flush=True)
                    time.sleep(retry_after)
                    f.seek(0)
                    files = {"file": (Path(audio_path).name, f, "audio/mpeg")}
                    continue
                print(f"    retry {attempt+1}: HTTP {resp.status_code} — {resp.text[:300]}", flush=True)
                time.sleep(5 * (attempt + 1))
                f.seek(0)
                files = {"file": (Path(audio_path).name, f, "audio/mpeg")}
            except Exception as e:
                print(f"    retry {attempt+1}: {e}", flush=True)
                time.sleep(5 * (attempt + 1))
                f.seek(0)
                files = {"file": (Path(audio_path).name, f, "audio/mpeg")}
    return None

def format_transcript(r, offset=0):
    lines = []
    segs = r.get("segments") or []
    if segs:
        for s in segs:
            start = s.get("start", 0) + offset
            text = (s.get("text") or "").strip()
            if text:
                h, m, sc = int(start//3600), int((start%3600)//60), int(start%60)
                lines.append(f"[{h:02d}:{m:02d}:{sc:02d}] {text}")
    else:
        lines.append(r.get("text", "").strip())
    return "\n".join(lines)

def bar(cur, tot, w=30):
    f = int(w * cur / tot) if tot else 0
    return f"[{'#'*f}{'-'*(w-f)}] {cur}/{tot}"

def main():
    status = load_status()
    usage = load_usage()
    total = len(INTERVIEWS)

    done_pre = sum(1 for e, _ in INTERVIEWS if status.get(e, {}).get("transcribed"))
    print(f"=== Chernobrov Groq Transcription === ({done_pre}/{total} already done)\n", flush=True)

    for i, (eid, fname) in enumerate(INTERVIEWS):
        if status.get(eid, {}).get("transcribed"):
            print(f"{bar(i+1, total)} SKIP {fname}", flush=True)
            continue

        audio = AUDIO_DIR / f"{fname}.mp3"
        if not audio.exists() or audio.stat().st_size < 10000:
            print(f"{bar(i+1, total)} MISSING {fname}", flush=True)
            continue

        dur_sec = audio_duration(audio)
        print(f"{bar(i+1, total)} START {fname} ({dur_sec/60:.1f}min)", flush=True)

        chunks = split_audio(str(audio), fname)
        print(f"  → {len(chunks)} chunk(s)", flush=True)

        all_text = []
        offset = 0
        success = True
        for ci, cp in enumerate(chunks):
            chunk_dur = audio_duration(cp)
            check_rate_limit(usage, chunk_dur)

            print(f"  chunk {ci+1}/{len(chunks)} ({chunk_dur/60:.1f}min) ...", end="", flush=True)
            t0 = time.time()
            r = transcribe_chunk(cp)
            elapsed = time.time() - t0
            if r:
                all_text.append(format_transcript(r, offset=offset))
                usage["events"].append((time.time(), chunk_dur))
                save_usage(usage)
                print(f" OK ({elapsed:.1f}s)", flush=True)
            else:
                all_text.append(f"[CHUNK {ci} FAILED]")
                print(f" FAIL after {elapsed:.1f}s", flush=True)
                success = False
            offset += chunk_dur

        tp = TRANSCRIPT_DIR / f"{fname}.txt"
        header = (f"# {fname}\n# Transcribed via Groq whisper-large-v3\n"
                  f"# Date: {time.strftime('%Y-%m-%d %H:%M')}\n# Duration: {dur_sec/60:.1f} min\n\n")
        tp.write_text(header + "\n".join(all_text))
        kb = tp.stat().st_size // 1024
        print(f"  ✓ saved {tp.name} ({kb}KB)", flush=True)

        status[eid] = {
            "status": "transcribed" if success else "partial",
            "transcribed": success,
            "provider": "groq",
            "audio": str(audio),
            "transcript": str(tp),
            "chunks": len(chunks),
            "duration_min": dur_sec / 60,
        }
        save_status(status)

    done = sum(1 for e, _ in INTERVIEWS if status.get(e, {}).get("transcribed"))
    print(f"\n=== DONE === {done}/{total} transcribed", flush=True)

if __name__ == "__main__":
    main()
