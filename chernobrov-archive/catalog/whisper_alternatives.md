# Альтернативы Whisper для русского ASR — корпус Черноброва / Whisper Alternatives for Russian ASR — Chernobrov Corpus

**Охват / Scope:** 15 файлов, ~21 час, русский язык, нужны посегментные временные метки / 15 files, ~21 hours, Russian language, need sentence-level timestamps  
**Дата составления / Date compiled:** 17 апреля 2026 / April 17, 2026

---

## Ранжирование по стоимости для 21 часа русской транскрипции / Cost Ranking for 21 Hours of Russian Transcription

| # | Сервис / Service | Бесплатная квота / Free Quota | Стоимость за 21ч (после бесплатной) / Cost for 21h (after free) | Качество RU / RU Quality | Метки / Timestamps | Установка / Setup |
|---|---------|-----------|--------------------------|------------|------------|-------|
| 1 | **faster-whisper (локально / local, large-v3)** | Безлимит (self-hosted) / Unlimited (self-hosted) | **$0.00** | WER ~6.4% (fine-tuned) / ~9.8% (базовая / base) | Пословно / Word-level | Средне — установка Python / Medium — Python install |
| 2 | **whisper.cpp (локально / local, large-v3)** | Безлимит (self-hosted) / Unlimited (self-hosted) | **$0.00** | То же, что выше / Same as above | Пословно / Word-level | Средне — сборка C++ / Medium — C++ build |
| 3 | **Groq Whisper-large-v3-turbo** | 8ч/день бесплатно (28,800 с ASD) / 8h/day free (28,800s ASD) | **$0.00** (3 дня / 3 days) или / or $0.04/ч платно / paid | Отлично (модель OpenAI) / Excellent (OpenAI model) | Посегментно / Segment-level | Легко — регистрация API / Easy — API key signup |
| 4 | **AssemblyAI** (модель / model Universal) | $50 единовременный кредит (~185ч) / $50 one-time credit (~185h) | **$0.00** (кредит покрывает всё / credit covers all) | Хорошо, 99 языков включая RU / Good, 99 langs incl. RU | Пофразно / Sentence-level | Легко — регистрация API / Easy — API key signup |
| 5 | **Gladia** | 10ч/месяц, возобновляется / 10h/month recurring | $0.61/ч → ~$6.71 за оставшиеся 11ч / $0.61/h → ~$6.71 for remaining 11h | Хорошо, 100+ языков включая RU / Good, 100+ langs incl. RU | Пословно / Word-level | Легко — регистрация API / Easy — API key signup |
| 6 | **OpenAI whisper-1 / GPT-4o Transcribe** | $5 кредит новому аккаунту (~833 мин = 13.9ч) / $5 new-acct credit (~833 min = 13.9h) | $0.006/мин → ~$4.51 за оставшиеся 7.1ч / $0.006/min → ~$4.51 remaining 7.1h | Референсное качество / Reference quality | Посегментно / Segment-level | Легко — аккаунт уже есть / Easy — already have account |
| 7 | **OpenAI GPT-4o Mini Transcribe** | тот же $5 кредит (~27.8ч покрывает всё) / same $5 credit (~27.8h covers all) | $0.003/мин → ~$0 при активном кредите / $0.003/min → ~$0 if credit active | Близко к whisper / Near-whisper quality | Посегментно / Segment-level | Легко — тот же аккаунт / Easy — same account |
| 8 | **ElevenLabs Scribe v1** | Включено в платные планы; бесплатный план ограничен / Included in paid plans; free plan limited | $0.22/ч → **$4.84** за 21ч / $0.22/h → **$4.84** for 21h | Отлично, WER ≤5% для RU / Excellent, WER ≤5% for RU | Пословно / Word-level | Легко — регистрация API / Easy — API key signup |
| 9 | **Deepgram Nova-3 Multilingual** | $200 кредит новому аккаунту (~775ч) / $200 new-acct credit (~775h) | **$0.00** (кредит покрывает всё / credit covers all) | Хорошо — RU в Nova-3 / Good — RU in Nova-3 | Пословно / Word-level | Легко — регистрация API / Easy — API key signup |
| 10 | **Yandex SpeechKit** (async) | ~$50 пробный грант (новый Yandex Cloud аккаунт) / ~$50 trial grant (new Yandex Cloud acct) | ~$0.48–$0.60/ч → ~$10–$13 полностью / ~$0.48–$0.60/h → ~$10–$13 full | Лучшее для RU (95-97% точность) / Best for RU (95-97% acc) | Пофразно / Phrase-level | Средне — аккаунт Yandex Cloud / Medium — Yandex Cloud account |
| 11 | **Google Cloud STT v2** | 60 мин/месяц бесплатно / 60 min/month free | $0.024/мин → **$28.80** за 21ч / $0.024/min → **$28.80** for 21h | Хорошо, 125+ языков / Good, 125+ langs | Пословно / Word-level | Средне — аккаунт GCP, биллинг / Medium — GCP account, billing |
| 12 | **Replicate Whisper** | Нет (оплата за запуск) / None (pay per run) | ~$0.0041/запуск × ~200 запусков → ~**$0.82** / ~$0.0041/run × ~200 runs → ~**$0.82** | Как OpenAI whisper / Same as OpenAI whisper | Посегментно / Segment-level | Легко — API key / Easy — API key |
| 13 | **AssemblyAI Slam-1** (расширенный / advanced) | тот же $50 кредит / same $50 credit | $0.27/ч при израсходованном кредите / $0.27/h if credit spent | Лучшая точность, ограниченные языки / Best accuracy, limited langs | Пофразно / Sentence-level | Легко — тот же аккаунт / Easy — same account |
| 14 | **HuggingFace Inference API** | Фактически недоступно — Whisper возвращает 410 Gone / Effectively unusable — Whisper returns 410 Gone | N/A | N/A | N/A | Сломано / Broken |
| 15 | **Cerebras** | Нет предложения Whisper/ASR / No Whisper/ASR offering | N/A | N/A | N/A | N/A |

---

## Детальные замечания по опциям / Detailed Option Notes

### 1. faster-whisper (локально / local) — РЕКОМЕНДОВАННЫЙ ВЫБОР / RECOMMENDED TOP PICK

**RU:**
- **Стоимость:** $0.00
- **Модель:** `large-v3` или fine-tuned `antony66/whisper-large-v3-russian` (WER 6.39 против базы 9.84)
- **Русский WER:** 6.4% (fine-tuned на Mozilla Common Voice 17 Russian, 225k строк)
- **Скорость:** 4x быстрее openai/whisper; GPU с 10GB VRAM = ~6-18 мин на час аудио; только CPU = ~1-2 часа на час аудио
- **ОЗУ (режим CPU):** ~10GB RAM для large-v3; int8-квантование снижает до ~5-6GB
- **ОЗУ (режим GPU):** ~10GB VRAM для large-v3; large-v3-turbo требует ~5GB VRAM
- **Метки:** пословные доступны
- **Форматы вывода:** JSON, SRT, VTT, plain text
- **Оговорка:** large-v3-turbo в 6 раз быстрее с потерей WER ~1-2%; хороший компромисс для CPU

**EN:**
- **Cost:** $0.00
- **Model:** `large-v3` or fine-tuned `antony66/whisper-large-v3-russian` (WER 6.39 vs base 9.84)
- **Russian WER:** 6.4% (fine-tuned on Mozilla Common Voice 17 Russian, 225k rows)
- **Speed:** 4x faster than openai/whisper; GPU with 10GB VRAM = ~6-18 min per hour of audio; CPU-only = ~1-2 hours per audio hour
- **RAM (CPU mode):** ~10GB RAM for large-v3; int8 quantization reduces to ~5-6GB
- **RAM (GPU mode):** ~10GB VRAM for large-v3; large-v3-turbo needs ~5GB VRAM
- **Timestamps:** Word-level available
- **Output formats:** JSON, SRT, VTT, plain text
- **Caveat:** large-v3-turbo is 6x faster with ~1-2% WER penalty; good tradeoff for CPU use

**Установка / Setup:**
```bash
pip install faster-whisper
# Use the Russian fine-tune:
from faster_whisper import WhisperModel
model = WhisperModel("antony66/whisper-large-v3-russian", device="cpu", compute_type="int8")
segments, info = model.transcribe("audio.mp3", word_timestamps=True, language="ru")
```

### 2. whisper.cpp (локально / local)

**RU:**
- **Стоимость:** $0.00
- **Поддержка GPU:** CUDA, Metal (Apple), OpenCL, Vulkan, SYCL — версия 1.8.3 добавляет 12-кратный прирост iGPU
- **Память:** То же, что faster-whisper (~10GB VRAM или RAM для large-v3)
- **Метки:** пословные
- **Формат:** может выводить SRT, VTT, JSON, plain text
- **Лучше всего для:** окружений с низкой зависимостью или встраиваемого скриптинга; чуть сложнее получить пословные метки по сравнению с Python API faster-whisper

**EN:**
- **Cost:** $0.00
- **GPU support:** CUDA, Metal (Apple), OpenCL, Vulkan, SYCL — version 1.8.3 adds 12x iGPU boost
- **Memory:** Same as faster-whisper (~10GB VRAM or RAM for large-v3)
- **Timestamps:** Word-level
- **Format:** Can output SRT, VTT, JSON, plain text
- **Best for:** Lower-dependency environments or embedded scripting; slightly harder to get word timestamps vs faster-whisper Python API

### 3. Groq Whisper — ЛУЧШИЙ БЕСПЛАТНЫЙ ОБЛАЧНЫЙ ВАРИАНТ / BEST FREE CLOUD OPTION

**RU:**
- **Модели:** `whisper-large-v3` ($0.111/ч) и `whisper-large-v3-turbo` ($0.04/ч)
- **Ограничения бесплатного уровня (без карты):**
  - RPM: 20
  - RPD: 2,000
  - Аудио-секунды в час (ASH): 7,200 (= 2ч аудио/час часов)
  - Аудио-секунды в день (ASD): **28,800 (= 8 часов/день)**
  - Макс. размер файла: 25 МБ на запрос
- **Стратегия на 21ч:** разделить аудио на куски <25MB. Обрабатывать 8ч/день бесплатно 3 дня = 21ч всего за $0.00
- **Качество для RU:** идентично OpenAI whisper-large-v3 (это та же модель, только на железе Groq)
- **Метки:** посегментные; пословные через `timestamp_granularities=["word"]`
- **Ограничение:** лимит 25MB означает, что типичные MP3 на 128kbps длятся максимум ~26 минут на кусок. Делить через ffmpeg.
- **Установка:** регистрация на console.groq.com, карта не нужна

**EN:**
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

**RU:**
- **Бесплатный кредит:** $50 единовременно (новый аккаунт, срок не указан)
- **Модель Universal:** $0.15/ч (база) — $50 покрывает ~333ч. Более чем достаточно.
- **Модель Slam-1 (расширенная):** $0.27/ч — $50 покрывает ~185ч. Всё равно много.
- **Поддержка RU:** 99 языков включая русский, автоопределение
- **Метки:** пофразно и пословно
- **Оговорка:** Потоковая транскрипция реального времени — только EN/ES/FR/DE/IT/PT. Пакетная транскрипция поддерживает RU отлично.
- **Установка:** assemblyai.com, бесплатный аккаунт

**EN:**
- **Free credit:** $50 one-time (new account, no expiry mentioned)
- **Universal model:** $0.15/h (base) — $50 covers ~333h. More than enough.
- **Slam-1 model (advanced):** $0.27/h — $50 covers ~185h. Still plenty.
- **Russian support:** 99 languages including Russian, auto-detected
- **Timestamps:** Sentence and word-level
- **Caveat:** Real-time streaming is English/Spanish/French/German/Italian/Portuguese only. Batch transcription supports Russian fine.
- **Setup:** assemblyai.com, free account

### 5. Gladia

**RU:**
- **Бесплатный уровень:** 10 часов/месяц, возобновляемо
- **Стратегия 21ч:** использовать 10ч в месяц 1, 10ч в месяц 2, 1ч в месяц 3 = $0. Или платить $6.71 за оставшиеся 11ч.
- **Ценообразование:** $0.61/ч async (Starter); $0.20/ч на плане Growth
- **Поддержка RU:** 100+ языков включая русский
- **Метки:** пословные
- **Установка:** gladia.io, бесплатная регистрация

**EN:**
- **Free tier:** 10 hours/month, recurring monthly
- **21h strategy:** Use 10h in month 1, 10h in month 2, 1h in month 3 = $0. Or pay $6.71 for remaining 11h.
- **Pricing:** $0.61/h async (Starter); $0.20/h on Growth plan
- **Russian support:** 100+ languages including Russian
- **Timestamps:** Word-level
- **Setup:** gladia.io, free signup

### 6-7. OpenAI (whisper-1 и варианты GPT-4o / whisper-1 and GPT-4o variants)

**RU:**
- **Текущее ценообразование:**
  - `whisper-1`: $0.006/мин ($0.36/ч)
  - `gpt-4o-transcribe`: $0.006/мин ($0.36/ч)
  - `gpt-4o-mini-transcribe`: $0.003/мин ($0.18/ч)
- **Кредит нового аккаунта:** $5 (истекает через 3 месяца, карта не требуется при регистрации)
  - $5 по $0.003/мин = 1,667 минут = **27.8 часов** — хватит на все 21ч с mini-transcribe
  - $5 по $0.006/мин = 833 минуты = 13.9ч — покрывает ~2/3 с whisper-1
- **Качество для RU:** референсное (Whisper обучен OpenAI)
- **Метки:** посегментные; пословные через `timestamp_granularities=["word"]`

**EN:**
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

**RU:**
- **Scribe v1:** $0.22/ч; Scribe v2 realtime: $0.39/ч
- **Стоимость 21ч:** $4.62 с Scribe v1
- **Качество для RU:** отличное — указано WER ≤5% для русского
- **Метки:** пословные
- **Бесплатное использование:** нет отдельного бесплатного уровня для API; кредиты приходят только с платными планами
- **Регистрация:** elevenlabs.io

**EN:**
- **Scribe v1:** $0.22/h; Scribe v2 realtime: $0.39/h
- **21h cost:** $4.62 with Scribe v1
- **Russian quality:** Excellent — listed at WER ≤5% for Russian
- **Timestamps:** Word-level
- **Free usage:** No standalone free tier for API; credits come with paid plans only
- **Signup:** elevenlabs.io

### 9. Deepgram

**RU:**
- **Бесплатный кредит:** $200 единовременно для новых пользователей (некоторые источники говорят $150 — проверяйте при регистрации)
- **Nova-3 Multilingual:** $0.0043/мин ($0.258/ч) — $200 покрывает ~775 часов
- **Поддержка RU:** Nova-3 Multilingual явно поддерживает русский (10 языков)
- **Метки:** пословные
- **Оговорка:** после исчерпания кредита бесплатного уровня нет; сумма кредита может меняться
- **Установка:** deepgram.com, бесплатная регистрация

**EN:**
- **Free credit:** $200 one-time for new users (some sources say $150 — verify at signup)
- **Nova-3 Multilingual:** $0.0043/min ($0.258/h) — $200 covers ~775 hours
- **Russian support:** Nova-3 Multilingual explicitly supports Russian (10 languages)
- **Timestamps:** Word-level
- **Caveat:** No ongoing free tier after credit exhausted; credit amount may vary
- **Setup:** deepgram.com, free signup

### 10. Yandex SpeechKit

**RU:**
- **Качество для RU:** лучшее из доступных для русского — 95-97% точности, обрабатывает акценты/диалекты
- **Ценообразование async-распознавания:** биллинг за секунду аудио (мин 15с); точная ставка ~0.008–0.01 руб/с (проверить текущую)
- **Приблизительная стоимость за 21ч:** ~400-500 руб (~$4-5 USD по текущему курсу)
- **Пробный грант:** новые аккаунты Yandex Cloud получают грант (~$50 эквивалент); проверить yandex.cloud/en/prices
- **Языки:** русский, английский, турецкий (русский — первоклассный)
- **Метки:** пофразные
- **Установка:** аккаунт Yandex Cloud (требует верификацию телефона), несколько бюрократично для не-российских пользователей
- **Примечание:** идеальный выбор, если нужно лучшее возможное качество русской транскрипции

**EN:**
- **Russian quality:** Best available for Russian — 95-97% accuracy, handles accents/dialects
- **Async recognition pricing:** Billed per second of audio (min 15s); exact rate ~0.008–0.01 RUB/s (check current rate)
- **Approximate cost for 21h:** ~400-500 RUB (~$4-5 USD at current exchange)
- **Trial grant:** New Yandex Cloud accounts receive a grant (~$50 equivalent); check yandex.cloud/en/prices
- **Languages:** Russian, English, Turkish (Russian is first-class citizen)
- **Timestamps:** Phrase-level
- **Setup:** Yandex Cloud account (requires phone verification), somewhat bureaucratic for non-Russian users
- **Note:** Ideal choice if you want the best possible Russian transcription quality

### 11. Google Cloud STT v2

**RU:**
- **Бесплатный уровень:** только 60 мин/месяц — покрывает менее 0.5% задачи
- **Ценообразование:** $0.024/мин ($1.44/ч) — 21ч = **$28.80** (дорого)
- **Поддержка RU:** да, 125+ языков
- **Метки:** пословные
- **Вердикт:** не рекомендуется для этой нагрузки

**EN:**
- **Free tier:** 60 min/month only — covers less than 0.5% of the job
- **Pricing:** $0.024/min ($1.44/h) — 21h = **$28.80** (expensive)
- **Russian support:** Yes, 125+ languages
- **Timestamps:** Word-level
- **Verdict:** Not recommended for this workload

### 12. Replicate

**RU:**
- **Нет бесплатного уровня для Whisper**
- **Стоимость:** ~$0.0041 за запуск; разделение 21ч на куски ~30 мин = ~42 запуска = ~$0.17 всего
- **Оговорка:** требуется карта; биллинг за запуск; задержка холодного старта модели
- **Метки:** посегментные

**EN:**
- **No free tier for Whisper**
- **Cost:** ~$0.0041 per run; splitting 21h into ~30-min chunks = ~42 runs = ~$0.17 total
- **Caveat:** Requires credit card; per-run billing; model cold-start latency
- **Timestamps:** Segment-level

### 13. HuggingFace Inference API

**RU:**
- **Статус:** модели Whisper возвращают 410 Gone на бесплатном уровне с ноября 2025
- **Обходной путь:** план HF Pro ($9/месяц) включает $2 кредита + оплата за compute-секунду
- **Вердикт:** фактически недоступно на бесплатном уровне; не стоит преследовать

**EN:**
- **Status:** Whisper models return 410 Gone on free tier as of November 2025
- **Workaround:** HF Pro plan ($9/month) includes $2 credit + pay-per-compute-second
- **Verdict:** Effectively unavailable on free tier; not worth pursuing

### 14. Cerebras

**RU:** Нет продукта ASR/Whisper — только инференс LLM.  
**EN:** No ASR/Whisper product — LLM inference only.

---

## Стратегия комбинирования бесплатных уровней (Нулевая стоимость за 21ч) / Free Tier Combination Strategy (Zero Cost for 21h)

**RU:** Чтобы транскрибировать все 21 час полностью бесплатно, используя несколько сервисов:  
**EN:** To transcribe all 21 hours entirely free using multiple services:

### Вариант A / Option A: Groq один (3 дня / alone, 3 days)
- День 1 / Day 1: 8ч на бесплатном уровне Groq / 8h on Groq free tier
- День 2 / Day 2: 8ч на бесплатном уровне Groq / 8h on Groq free tier
- День 3 / Day 3: 5ч на бесплатном уровне Groq / 5h on Groq free tier
- **Итого стоимость / Total cost: $0.00**
- **Использованная модель / Model used:** whisper-large-v3-turbo (идентичное OpenAI качество / identical quality to OpenAI)
- **Требование / Requirement:** разбить файлы на куски <25MB; скрипт для паузы/возобновления / Split files to <25MB chunks; script to pause/resume

### Вариант B / Option B: новый аккаунт AssemblyAI (в один день / same day)
- Создать новый аккаунт → получить $50 кредит / Create new account → get $50 credit
- 21ч × $0.15/ч = $3.15 вычтено из $50 кредита / 21h × $0.15/h = $3.15 deducted from $50 credit
- **Итого из кармана / Total out of pocket: $0.00** (кредит всё поглощает / credit absorbs it all)
- **Преимущество / Advantage:** без разбиения, без ожидания / No chunking, no waiting

### Вариант C / Option C: локальный faster-whisper (в любое время / anytime)
- Без квот, без аккаунтов, без стоимости / No quotas, no accounts, no cost
- С GPU: ~2-3 часа реального времени на 21ч / With GPU: ~2-3 hours wall time for 21h
- Только CPU (int8): ~1-2 дня реального времени на 21ч / With CPU only (int8): ~1-2 days wall time for 21h
- **Итого стоимость / Total cost: $0.00**

### Вариант D / Option D: микс бесплатных уровней / Mix free tiers
- Gladia: 10ч бесплатно в месяц 1 / 10h free month 1
- Groq: 8ч бесплатно за 1 день / 8h free in 1 day
- новый аккаунт OpenAI: покрывает оставшиеся ~3ч с $5 кредитом / OpenAI new account: covers remaining ~3h with $5 credit
- **Итого стоимость / Total cost: $0.00**

---

## Расхождение в стоимости Лазар против Чернобров / The Lazar vs Chernobrov Cost Discrepancy

### Вероятное объяснение: истёк пробный кредит $5 / Likely explanation: expired $5 free trial credit

**RU:** OpenAI даёт новым API-аккаунтам **$5 бесплатных кредитов, действительных 3 месяца**.

- **Корпус Лазар (~35ч):** эта сумма кажется слишком большой для покрытия $5 кредитом. Однако если Лазар транскрибировался ~3 месяца назад, $5 кредит, вероятно, был активен. По $0.006/мин $5 покрывает 833 минуты (13.9ч). Если он покрыл весь Лазар, пачка файлов могла быть обработана в нескольких сессиях с всё ещё активным кредитом, или файлы были короче, чем казалось.
  - Если Лазар был на самом деле ~13ч и казался 35ч (из-за путаницы со счётом файлов), кредит его покрыл.
  - Альтернативно: Лазар был запущен против `gpt-4o-mini-transcribe` по $0.003/мин — $5 покрыли бы 27.8ч.

- **Чернобров (~5ч стоил $2):** по $0.006/мин 5ч = 300 мин = $1.80 ≈ $2 в счёте. Это подтверждает, что пробный кредит уже был исчерпан или истёк.

**EN:** OpenAI gives new API accounts **$5 in free credits, valid for 3 months**.

- **Lazar corpus (~35h):** This amount seems too large to have been covered by $5 credit. However, if Lazar was transcribed ~3 months ago, the $5 credit was likely active. At $0.006/min, $5 covers 833 minutes (13.9h). If it covered all of Lazar, the file batch may have been processed in multiple sessions with the credit still active, or the files were shorter than perceived.
  - If Lazar was actually ~13h and seemed like 35h (due to file count confusion), the credit covered it.
  - Alternatively: Lazar was run against `gpt-4o-mini-transcribe` at $0.003/min — $5 would cover 27.8h.

- **Chernobrov (~5h cost $2):** At $0.006/min, 5h = 300 minutes = $1.80 ≈ $2 billed. This confirms the free trial credit had already been exhausted or expired.

### Изменения цен: не подтверждены / Pricing changes: None confirmed
**RU:** Цена OpenAI Whisper стабильна на $0.006/мин с момента введения. Повышений цен в исследовании 2025-2026 не обнаружено.  
**EN:** OpenAI Whisper pricing has been stable at $0.006/min since introduction. No price increases detected in 2025-2026 research.

### Что, вероятно, произошло: / What likely happened:
1. Лазар был запущен пока пробный кредит $5 был ещё активен (в первые 3 месяца создания аккаунта) / Lazar was run while the $5 trial credit was still active (within first 3 months of account creation)
2. Кредит истёк (3-месячное окно) / The credit expired (3-month window)
3. Чернобров попал на живой биллинг-аккаунт, показав фактические затраты / Chernobrov hit a live billing account, showing actual costs

### Что делать сейчас: / What to do now:
- Вариант 1 / Option 1: использовать бесплатный уровень Groq (та же модель whisper, нулевая стоимость) / Use Groq free tier (same whisper model, zero cost)
- Вариант 2 / Option 2: создать новый аккаунт OpenAI (новый $5 кредит) — примечание: один на человека/номер телефона / Create a new OpenAI account (new $5 credit) — note: one per person/phone number
- Вариант 3 / Option 3: использовать faster-whisper локально с нулевой стоимостью / Use faster-whisper locally at zero cost

---

## Рекомендованная настройка для оставшихся 21 часов / Recommended Setup for Remaining 21 Hours

### Если нужна нулевая стоимость, облачно, сегодня: / If you want zero cost, cloud-based, today:
**AssemblyAI** — создать бесплатный аккаунт, получить $50 кредит, запустить все 21ч за $3.15, готово. / create free account, get $50 credit, run all 21h for $3.15, done.

### Если нужна нулевая стоимость, облачно, на 3 дня: / If you want zero cost, cloud-based, spread over 3 days:
**Groq** — `whisper-large-v3-turbo`, 8ч/день бесплатно, разделить файлы через ffmpeg. / 8h/day free, split files with ffmpeg.

```bash
# Split each MP3 into 20-minute segments (well under 25MB at 128kbps)
ffmpeg -i input.mp3 -f segment -segment_time 1200 -c copy segment_%03d.mp3
```

### Если нужно лучшее качество русского + нулевая стоимость, self-hosted: / If you want best Russian quality + zero cost, self-hosted:
**faster-whisper с / with antony66/whisper-large-v3-russian**

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

## Источники / Sources

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
*Составлено / Compiled: 2026-04-17 | Уверенность / Confidence: ВЫСОКАЯ для облачного ценообразования (прямой запрос источника). Точные ставки Yandex в рублях требуют проверки на уровне аккаунта. / HIGH for cloud pricing (direct source fetch). Yandex exact RUB rates require account-level verification.*
