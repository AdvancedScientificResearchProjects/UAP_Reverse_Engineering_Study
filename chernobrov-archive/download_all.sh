#!/bin/bash
# Download all Chernobrov interview audio in parallel batches (max 4 concurrent)
set -u

VENV="<repo>/.venv/bin"
YTDLP="$VENV/yt-dlp"
AUDIO_DIR="<repo>/chernobrov-archive/audio"
LOG="<repo>/chernobrov-archive/download.log"
cd "$AUDIO_DIR"

download() {
    local idx="$1" url="$2" name="$3"
    if [[ -f "${name}.mp3" ]] && [[ $(stat -c%s "${name}.mp3" 2>/dev/null) -gt 10000 ]]; then
        echo "[SKIP $idx] ${name}" | tee -a "$LOG"
        return 0
    fi
    rm -f "${name}".part "${name}".ytdl 2>/dev/null
    echo "[START $idx] ${name}" | tee -a "$LOG"
    "$YTDLP" --no-playlist -x --audio-format mp3 --audio-quality 5 \
        -o "${name}.%(ext)s" --no-overwrites \
        --retries 10 --fragment-retries 10 \
        --socket-timeout 120 --extractor-retries 5 \
        "$url" 2>>"$LOG"

    for ext in m4a opus webm ogg wav; do
        if [[ -f "${name}.${ext}" ]]; then
            ffmpeg -i "${name}.${ext}" -q:a 5 "${name}.mp3" -y 2>/dev/null
            rm -f "${name}.${ext}"
        fi
    done

    if [[ -f "${name}.mp3" ]] && [[ $(stat -c%s "${name}.mp3" 2>/dev/null) -gt 10000 ]]; then
        echo "[DONE $idx] ${name} ($(du -h "${name}.mp3" | cut -f1))" | tee -a "$LOG"
    else
        echo "[FAIL $idx] ${name}" | tee -a "$LOG"
    fi
}

echo "=== Download started $(date) ===" > "$LOG"

# Batch 1 (first 4)
download 01 "https://youtu.be/fAeumSyWHAk" "01_Chernobrov_MashinaVremeni_2h37" &
download 02 "https://youtu.be/-lmeYxV8Iuw" "02_Chernobrov_MashinaVremeni_LAI_1h46" &
download 03 "https://youtu.be/NFcLDb-aWZ0" "03_Chernobrov_MashinaVremeni_41min" &
download 04 "https://youtu.be/LnrWHa4w4os" "04_Chernobrov_MashinaVremeni_1h46_alt" &
wait
echo "=== Batch 1 done ===" | tee -a "$LOG"

# Batch 2
download 05 "https://youtu.be/-BL3H9obTDs" "05_Gaiduchok_traveler_58min" &
download 06 "https://youtu.be/RxV7dDXoMLg" "06_SlediPutesh_2h55" &
download 07 "https://youtu.be/9k-mlSfU9V0" "07_MashinaVremeni_Hronoput_3h04" &
download 08 "https://youtu.be/4YGeR1KsXy0" "08_3zvezdnie_NLO_22min" &
wait
echo "=== Batch 2 done ===" | tee -a "$LOG"

# Batch 3
download 09 "https://youtu.be/I2u233WU0fY" "09_ParallelnyeMiry_39min" &
download 10 "https://youtu.be/-RC75ZeAfsE" "10_KakUstroenoVremya_2011_11min" &
download 11 "https://youtu.be/_kvcAfBqOmE" "11_MashinaVremeni_GhostHunters_1h45" &
download 12 "https://youtu.be/ff4bB3kUMi4" "12_MashinaVremeni_Chernobrov_46min" &
wait
echo "=== Batch 3 done ===" | tee -a "$LOG"

# Batch 4
download 13 "https://youtu.be/yeL7msYWhxc" "13_Hronoput_Murom_2h37" &
download 14 "https://youtu.be/ITxwY3oOM4I" "14_ZagadkiVremeni_25min" &
download 15 "https://youtu.be/zAfnwTj5bW8" "15_MedveditskayaGryada_docfilm_2017_32min" &
download 16 "https://youtu.be/LBTUqPvaMe8" "16_KrugiNaPolyakh_2013_2h57" &
wait
echo "=== Batch 4 done ===" | tee -a "$LOG"

# Batch 5 (last 3)
download 17 "https://youtu.be/-l4tzEFcfWE" "17_NLO_dolya_pravdy_2h24" &
download 18 "https://youtu.be/G240ne2rx_s" "18_Kosmopoisk_MashinaVremeni_N24_58min" &
download 19 "https://youtu.be/hbg5ATAyq2s" "19_GravitatsionnyeAnomalii_12min" &
wait
echo "=== Batch 5 done ===" | tee -a "$LOG"

echo "=== ALL DOWNLOADS COMPLETE $(date) ===" | tee -a "$LOG"
ls -lhS "$AUDIO_DIR"/*.mp3 2>/dev/null | awk '{print $5, $NF}'
