# Whisper Alternatives for Russian ASR — Chernobrov Corpus
**Scope:** 15 files, ~21 hours, Russian language, need sentence-level timestamps
**Date compiled:** April 17, 2026

---

## Cost Ranking for 21 Hours of Russian Transcription

| # | Service | Free Quota | Cost for 21h (after free) | RU Quality | Timestamps | Setup |
|---|---------|-----------|--------------------------|------------|------------|-------|
| 1 | **faster-whisper (local, large-v3)** | Unlimited (self-hosted) | **$0.00** | WER ~6.4% (fine-tuned) / ~9.8% (base) | Word-level | Medium — Python install |
| 2 | **whisper.cpp (local, large-v3)** | Unlimited (self-hosted) | **$0.00** | Same as above | Word-level | Medium — C++ build |
| 3 | **Groq Whisper-large-v3-turbo** | 8h/day free (28,800s ASD) | **$0.00** (3 days) or $0.04/h paid | Excellent (OpenAI model) | Segment-level | Easy — API key signup |
| 4 | **AssemblyAI** (Universal model) | $50 one-time credit (~185h) | **$0.00** (credit covers all) | Good, 99 langs incl. RU | Sentence-level | Easy — API key signup |
| 5 | **Gladia** | 10h/month recurring | $0.61/h → ~$6.71 for remaining 11h | Good, 100+ langs incl. RU | Word-level | Easy — API key signup |
| 6 | **OpenAI whisper-1 / GPT-4o Transcribe** | $5 new-acct credit (~833 min = 13.9h) | $0.006/min → ~$4.51 remaining 7.1h | Reference quality | Segment-level | Easy — already have account |
| 7 | **OpenAI GPT-4o Mini Transcribe** | same $5 credit (~27.8h covers all) | $0.003/min → ~$0 if credit active | Near-whisper quality | Segment-level | Easy — same account |
| 8 | **ElevenLabs Scribe v1** | Included in paid plans; free plan limited | $0.22/h → **$4.84** for 21h | Excellent, WER ≤5% for RU | Word-level | Easy — API key signup |
| 9 | **Deepgram Nova-3 Multilingual** | $200 new-acct credit (~775h) | **$0.00** (credit covers all) | Good — RU in Nova-3 | Word-level | Easy — API key signup |
| 10 | **Yandex SpeechKit** (async) | ~$50 trial grant (new Yandex Cloud acct) | ~$0.48–$0.60/h → ~$10–$13 full | Best for RU (95-97% acc) | Phrase-level | Medium — Yandex Cloud account |
| 11 | **Google Cloud STT v2** | 60 min/month free | $0.024/min → **$28.80** for 21h | Good, 125+ langs | Word-level | Medium — GCP account, billing |
| 12 | **Replicate Whisper** | None (pay per run) | ~$0.0041/run × ~200 runs → ~**$0.82** | Same as OpenAI whisper | Segment-level | Easy — API key |
| 13 | **AssemblyAI Slam-1** (advanced) | same $50 credit | $0.27/h if credit spent | Best accuracy, limited langs | Sentence-level | Easy — same account |
| 14 | **HuggingFace Inference API** | Effectively unusable — Whisper returns 410 Gone | N/A | N/A | N/A | Broken |
| 15 | **Cerebras** | No Whisper/ASR offering | N/A | N/A | N/A | N/A |

---

## Detailed Option Notes

### 1. faster-whisper (local) — RECOMMENDED TOP PICK

- **Cost:** $0.00
- **Model:** `large-v3` or fine-tuned `antony66/whisper-large-v3-russian` (WER 6.39 vs base 9.84)
- **Russian WER:** 6.4% (fine-tuned on Mozilla Common Voice 17 Russian, 225k rows)
- **Speed:** 4x faster than openai/whisper; GPU with 10GB VRAM = ~6-18 min per hour of audio; CPU-only = ~1-2 hours per audio hour
- **RAM (CPU mode):** ~10GB RAM for large-v3; int8 quantization reduces to ~5-6GB
- **RAM (GPU mode):** ~10GB VRAM for large-v3; large-v3-turbo needs ~5GB VRAM
- **Timestamps:** Word-level available
- **Output formats:** JSON, SRT, VTT, plain text
- **Setup:**
  ```bash
  pip install faster-whisper
  # Use the Russian fine-tune:
  from faster_whisper import WhisperModel
  model = WhisperModel("antony66/whisper-large-v3-russian", device="cpu", compute_type="int8")
  segments, info = model.transcribe("audio.mp3", word_timestamps=True, language="ru")
  ```
- **Caveat:** large-v3-turbo is 6x faster with ~1-2% WER penalty; good tradeoff for CPU use

### 2. whisper.cpp (local)

- **Cost:** $0.00
- **GPU support:** CUDA, Metal (Apple), OpenCL, Vulkan, SYCL — version 1.8.3 adds 12x iGPU boost
- **Memory:** Same as faster-whisper (~10GB VRAM or RAM for large-v3)
- **Timestamps:** Word-level
- **Format:** Can output SRT, VTT, JSON, plain text
- **Best for:** Lower-dependency environments or embedded scripting; slightly harder to get word timestamps vs faster-whisper Python API

### 3. Groq Whisper — BEST FREE CLOUD OPTION

- **Models:** `whisper-large-v3` ($0.111/h) and `whisper-large-v3-turbo` ($0.04/h)
- **Free tier limits (no credit card):**
  - RPM: 20
  - RPD: 2,000
  - Audio seconds/hour (ASH): 7,200 (= 2h audio/clock-hour)
  - Audio seconds/day (ASD): **28,800 (= 8 hours/day)**
  - File size: 25 MB max per request
- **21h strategy:** Split audio into <25MB chunks. Process 8h/day free for 3 days = 21h total at $0.00
- **Russian quality:** Identical to OpenAI whisper-large-v3 (it IS the same model, just on Groq hardware)
- **Timestamps:** Segment-level; word-level available via `timestamp_granularities=["word"]`
- **Limitation:** 25MB file cap means typical MP3s at 128kbps last ~26 minutes max per chunk. Split with ffmpeg.
- **Setup:** Sign up at console.groq.com, no credit card needed

### 4. AssemblyAI

- **Free credit:** $50 one-time (new account, no expiry mentioned)
- **Universal model:** $0.15/h (base) — $50 covers ~333h. More than enough.
- **Slam-1 model (advanced):** $0.27/h — $50 covers ~185h. Still plenty.
- **Russian support:** 99 languages including Russian, auto-detected
- **Timestamps:** Sentence and word-level
- **Caveat:** Real-time streaming is English/Spanish/French/German/Italian/Portuguese only. Batch transcription supports Russian fine.
- **Setup:** assemblyai.com, free account

### 5. Gladia

- **Free tier:** 10 hours/month, recurring monthly
- **21h strategy:** Use 10h in month 1, 10h in month 2, 1h in month 3 = $0. Or pay $6.71 for remaining 11h.
- **Pricing:** $0.61/h async (Starter); $0.20/h on Growth plan
- **Russian support:** 100+ languages including Russian
- **Timestamps:** Word-level
- **Setup:** gladia.io, free signup

### 6-7. OpenAI (whisper-1 and GPT-4o variants)

- **Current pricing:**
  - `whisper-1`: $0.006/min ($0.36/h)
  - `gpt-4o-transcribe`: $0.006/min ($0.36/h)
  - `gpt-4o-mini-transcribe`: $0.003/min ($0.18/h)
- **New account credit:** $5 (expires after 3 months, no credit card required at signup)
  - $5 at $0.003/min = 1,667 minutes = **27.8 hours** — enough to cover all 21h with mini-transcribe
  - $5 at $0.006/min = 833 minutes = 13.9h — covers ~2/3 with whisper-1
- **Russian quality:** Reference quality (Whisper is trained by OpenAI)
- **Timestamps:** Segment-level; word-level with `timestamp_granularities=["word"]`

### 8. ElevenLabs Scribe

- **Scribe v1:** $0.22/h; Scribe v2 realtime: $0.39/h
- **21h cost:** $4.62 with Scribe v1
- **Russian quality:** Excellent — listed at WER ≤5% for Russian
- **Timestamps:** Word-level
- **Free usage:** No standalone free tier for API; credits come with paid plans only
- **Signup:** elevenlabs.io

### 9. Deepgram

- **Free credit:** $200 one-time for new users (some sources say $150 — verify at signup)
- **Nova-3 Multilingual:** $0.0043/min ($0.258/h) — $200 covers ~775 hours
- **Russian support:** Nova-3 Multilingual explicitly supports Russian (10 languages)
- **Timestamps:** Word-level
- **Caveat:** No ongoing free tier after credit exhausted; credit amount may vary
- **Setup:** deepgram.com, free signup

### 10. Yandex SpeechKit

- **Russian quality:** Best available for Russian — 95-97% accuracy, handles accents/dialects
- **Async recognition pricing:** Billed per second of audio (min 15s); exact rate ~0.008–0.01 RUB/s (check current rate)
- **Approximate cost for 21h:** ~400-500 RUB (~$4-5 USD at current exchange)
- **Trial grant:** New Yandex Cloud accounts receive a grant (~$50 equivalent); check yandex.cloud/en/prices
- **Languages:** Russian, English, Turkish (Russian is first-class citizen)
- **Timestamps:** Phrase-level
- **Setup:** Yandex Cloud account (requires phone verification), somewhat bureaucratic for non-Russian users
- **Note:** Ideal choice if you want the best possible Russian transcription quality

### 11. Google Cloud STT v2

- **Free tier:** 60 min/month only — covers less than 0.5% of the job
- **Pricing:** $0.024/min ($1.44/h) — 21h = **$28.80** (expensive)
- **Russian support:** Yes, 125+ languages
- **Timestamps:** Word-level
- **Verdict:** Not recommended for this workload

### 12. Replicate

- **No free tier for Whisper**
- **Cost:** ~$0.0041 per run; splitting 21h into ~30-min chunks = ~42 runs = ~$0.17 total
- **Caveat:** Requires credit card; per-run billing; model cold-start latency
- **Timestamps:** Segment-level

### 13. HuggingFace Inference API

- **Status:** Whisper models return 410 Gone on free tier as of November 2025
- **Workaround:** HF Pro plan ($9/month) includes $2 credit + pay-per-compute-second
- **Verdict:** Effectively unavailable on free tier; not worth pursuing

### 14. Cerebras

- **No ASR/Whisper product** — LLM inference only

---

## Free Tier Combination Strategy (Zero Cost for 21h)

To transcribe all 21 hours entirely free using multiple services:

### Option A: Groq alone (3 days)
- Day 1: 8h on Groq free tier
- Day 2: 8h on Groq free tier
- Day 3: 5h on Groq free tier
- **Total cost: $0.00**
- **Model used:** whisper-large-v3-turbo (identical quality to OpenAI)
- **Requirement:** Split files to <25MB chunks; script to pause/resume

### Option B: AssemblyAI new account (same day)
- Create new account → get $50 credit
- 21h × $0.15/h = $3.15 deducted from $50 credit
- **Total out of pocket: $0.00** (credit absorbs it all)
- **Advantage:** No chunking, no waiting

### Option C: Local faster-whisper (anytime)
- No quotas, no accounts, no cost
- With GPU: ~2-3 hours wall time for 21h
- With CPU only (int8): ~1-2 days wall time for 21h
- **Total cost: $0.00**

### Option D: Mix free tiers
- Gladia: 10h free month 1
- Groq: 8h free in 1 day
- OpenAI new account: covers remaining ~3h with $5 credit
- **Total cost: $0.00**

---

## The Lazar vs Chernobrov Cost Discrepancy

### Likely explanation: expired $5 free trial credit

OpenAI gives new API accounts **$5 in free credits, valid for 3 months**.

- **Lazar corpus (~35h):** This amount seems too large to have been covered by $5 credit. However, if Lazar was transcribed ~3 months ago, the $5 credit was likely active. At $0.006/min, $5 covers 833 minutes (13.9h). If it covered all of Lazar, the file batch may have been processed in multiple sessions with the credit still active, or the files were shorter than perceived.
  - If Lazar was actually ~13h and seemed like 35h (due to file count confusion), the credit covered it.
  - Alternatively: Lazar was run against `gpt-4o-mini-transcribe` at $0.003/min — $5 would cover 27.8h.

- **Chernobrov (~5h cost $2):** At $0.006/min, 5h = 300 minutes = $1.80 ≈ $2 billed. This confirms the free trial credit had already been exhausted or expired.

### Pricing changes: None confirmed
OpenAI Whisper pricing has been stable at $0.006/min since introduction. No price increases detected in 2025-2026 research.

### What likely happened:
1. Lazar was run while the $5 trial credit was still active (within first 3 months of account creation)
2. The credit expired (3-month window)
3. Chernobrov hit a live billing account, showing actual costs

### What to do now:
- Option 1: Use Groq free tier (same whisper model, zero cost)
- Option 2: Create a new OpenAI account (new $5 credit) — note: one per person/phone number
- Option 3: Use faster-whisper locally at zero cost

---

## Recommended Setup for Remaining 21 Hours

### If you want zero cost, cloud-based, today:
**AssemblyAI** — create free account, get $50 credit, run all 21h for $3.15, done.

### If you want zero cost, cloud-based, spread over 3 days:
**Groq** — `whisper-large-v3-turbo`, 8h/day free, split files with ffmpeg.

```bash
# Split each MP3 into 20-minute segments (well under 25MB at 128kbps)
ffmpeg -i input.mp3 -f segment -segment_time 1200 -c copy segment_%03d.mp3
```

### If you want best Russian quality + zero cost, self-hosted:
**faster-whisper with antony66/whisper-large-v3-russian**

```bash
pip install faster-whisper
python3 - <<'EOF'
from faster_whisper import WhisperModel
import json, sys

model = WhisperModel(
    "antony66/whisper-large-v3-russian",
    device="cpu",  # or "cuda" if GPU available
    compute_type="int8"  # reduces RAM from 10GB to ~5GB
)

audio_file = sys.argv[1]
segments, info = model.transcribe(
    audio_file,
    word_timestamps=True,
    language="ru",
    beam_size=5
)

output = []
for seg in segments:
    output.append({
        "start": seg.start,
        "end": seg.end,
        "text": seg.text.strip(),
        "words": [{"word": w.word, "start": w.start, "end": w.end} for w in seg.words]
    })

print(json.dumps(output, ensure_ascii=False, indent=2))
EOF
```

---

## Sources

- [Groq Pricing](https://groq.com/pricing)
- [Groq Rate Limits](https://console.groq.com/docs/rate-limits)
- [Groq Speech-to-Text Docs](https://console.groq.com/docs/speech-to-text)
- [AssemblyAI Pricing](https://www.assemblyai.com/pricing)
- [Deepgram Pricing](https://deepgram.com/pricing)
- [ElevenLabs Scribe](https://elevenlabs.io/blog/meet-scribe)
- [Gladia Pricing](https://www.gladia.io/pricing)
- [OpenAI Transcription Pricing (Apr 2026)](https://costgoat.com/pricing/openai-transcription)
- [Google Cloud STT Pricing](https://cloud.google.com/speech-to-text/pricing)
- [Yandex SpeechKit](https://yandex.cloud/en/services/speechkit)
- [SYSTRAN/faster-whisper GitHub](https://github.com/SYSTRAN/faster-whisper)
- [ggml-org/whisper.cpp GitHub](https://github.com/ggml-org/whisper.cpp)
- [antony66/whisper-large-v3-russian (HuggingFace)](https://huggingface.co/antony66/whisper-large-v3-russian) — WER 6.39 vs base 9.84
- [HuggingFace Inference API 410 Gone issue](https://huggingface.co/openai/whisper-large-v3/discussions/216)
- [OpenAI Free Credits status 2026](https://tokenmix.ai/blog/openai-api-key-free)
- [Replicate Whisper](https://replicate.com/openai/whisper)

---
*Compiled: 2026-04-17 | Confidence: HIGH for cloud pricing (direct source fetch). Yandex exact RUB rates require account-level verification.*
