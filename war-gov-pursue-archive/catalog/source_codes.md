# PURSUE Release 01 + Release 02 — Source Code Registry / Реестр кодов источников PURSUE Релиз 01 + Релиз 02

Stable identifiers for cross-referencing PURSUE records in `analysis/per-document/`, `analysis/topical/`, `analysis/MASTER_pursue_claims.md`, and `graph/fragments/agentI_war_gov_pursue.py`.

**RU:** Стабильные идентификаторы для перекрёстных ссылок на записи PURSUE в `analysis/per-document/`, `analysis/topical/`, `analysis/MASTER_pursue_claims.md` и `graph/fragments/agentI_war_gov_pursue.py`.

## Convention / Конвенция

`{AGENCY}-{TYPE}-{IDENTIFIER}` — short, stable, regex-safe (no spaces, no commas). / короткий, стабильный, безопасный для регулярных выражений (без пробелов, без запятых).

Codes are assigned in `catalog/documents.md` for all 161 records. Use the codes as-is in claim tables and cross-references.

**RU:** Коды назначены в `catalog/documents.md` для всех 161 записи. Используйте коды как есть в таблицах заявлений и перекрёстных ссылках.

---

## DoW (Department of War) — 82 records / 82 записи

### `DOW-D{n}` — Mission Reports and historical documents / Рапорты о миссиях и исторические документы

D-series numbers are assigned by the war.gov publisher (D3–D75 with gaps). / Номера D-серии присваиваются издателем war.gov (D3–D75 с пропусками).

| Code / Код | Title (excerpt) / Название (фрагмент) | Date / Дата | Notes / Примечания |
|------|-----------------|------|-------|
| `DOW-D3` … `DOW-D75` | Various MISREPs and reports / Различные рапорты о миссиях | 2016–2026 | Most are recent military encounters; D48 = 1996 USAF report; D49 = Vandenberg launch summary 1958–2000 / Большинство — недавние военные встречи; D48 = отчёт ВВС США 1996; D49 = сводка запусков Vandenberg 1958–2000 |

### `DOW-PR{n}` — Unresolved/Pending UAP Reports / Нерешённые/ожидающие рассмотрения отчёты НАЯ

PR-series 19–49. Mostly IR sensor B-roll videos (DVIDS-hosted) with some companion PDFs. / Серия PR 19–49. В основном B-roll видео с ИК-датчиков (хостинг DVIDS), некоторые с сопутствующими PDF.

### Special-purpose DoW codes / Специальные коды DoW

| Code / Код | Document / Документ | Note / Примечание |
|------|----------|------|
| `DOW-FOO-1944` | Foo-fighters / 415th NFS / SHAEF | **PDF corrupted at source — irrecoverable / PDF повреждён в источнике — невосстановимо** |
| `DOW-1947-AMC-MEMO` | 18_100754 General 1946-7 Vol 2 | Air Materiel Command memos Dec 1947 / Меморандумы Air Materiel Command декабрь 1947 |
| `DOW-1948-FLYING-DISCS` | 18_6369445 General 1948 Vol 1 | Flying discs reporting / Отчётность по «летающим тарелкам» |
| `DOW-1949-FSR-200-4` | 342_hs1-416511228 box186 319.1 | FSR 200-4 + MATS/AACS messages / Сообщения FSR 200-4 + MATS/AACS |
| `DOW-INC-SUM-1-100` | 38_143685 box7 incident summaries 1-100 | Standardized "Check-List Unidentified Flying Objects" / Стандартизированный «Контрольный список неопознанных летающих объектов» |
| `DOW-INC-SUM-101-172` | …101-172 | continuation / продолжение |
| `DOW-INC-SUM-173-233` | …173-233 | continuation / продолжение |
| `DOW-1948-NETHERLANDS-INTEL` | 341_110448 records 1948-1955 TS Cont No.2 | Air Force intel report Nov 1948 / Разведывательный отчёт ВВС ноябрь 1948 |
| `DOW-1955-AZERBAIJAN` | 341_110677 numerical file 5-2500 | 14 Oct 1955 ascent UFO Trans-Caucasus / НЛО 14 октября 1955 Закавказье |
| `DOW-WESTERN-US-2023` | Western US Event Slides | AARO presentation: 4 phenomena categories observed by 7 federal USPER witnesses (2023) / Презентация AARO: 4 категории явлений, наблюдавшихся 7 федеральными свидетелями USPER (2023) |

---

## FBI — 57 records / 57 записей

### `FBI-62HQ-{S/Sr/Sub}` — Master case file 62-HQ-83894 "Flying Discs" (1947–1968) / Основное дело 62-HQ-83894 «Летающие тарелки» (1947–1968)

| Code / Код | Type / Тип | Count / Количество |
|------|------|------|
| `FBI-62HQ-S01` … `FBI-62HQ-S10` | Sections / Разделы | 10 |
| `FBI-62HQ-Sr130`, `Sr153`, `Sr164`, `Sr220`, `Sr403`, `Sr438`, `Sr449` | Serials / Серийные | 7 |
| `FBI-62HQ-SubA` | Sub / Подфайл | 1 |

### `FBI-IR-{A/B}{nn}` — 2025 Western US IR photo cluster / Кластер ИК-фотографий Западного US 2025

| Code / Код | Format / Формат | Count / Количество |
|------|--------|------|
| `FBI-IR-A01` … `FBI-IR-A08` | A-series (general locations N/A) / Серия A (местоположения N/A) | 8 (8 PDFs + 8 thumbnail JPGs) |
| `FBI-IR-B01` … `FBI-IR-B24` | B-series (Western United States) / Серия B (Западные Штаты США) | 24 PDFs |

### `FBI-ELLIPSE-*` — September 2023 bronze ellipsoid case / Дело бронзового эллипсоида сентябрь 2023

| Code / Код | Document / Документ | Note / Примечание |
|------|----------|------|
| `FBI-ELLIPSE-SKETCH-2023` | Composite sketch / Составной эскиз | Site photo + FBI Lab graphic overlay / Фото места + графический оверлей лаборатории FBI |
| `FBI-ELLIPSE-Sr3` / `Sr4` / `Sr5` | Serial 3/4/5 / Серийный 3/4/5 | Redacted serials / Редактированные серийные |

### Single-purpose FBI codes / Однократные коды FBI

| Code / Код | Document / Документ |
|------|----------|
| `FBI-USPER-302` | USPER statement (likely linked to ground-pursuit B7) / Заявление USPER (предположительно связано с наземным преследованием B7) |
| `FBI-100-DE-18221-1957` | Earlier FBI individual case file (Delaware, 1957) / Более раннее индивидуальное дело FBI (Делавэр, 1957) |
| `FBI-100-DE-26505-1958` | Earlier FBI individual case file (Delaware, 1958) / Более раннее индивидуальное дело FBI (Делавэр, 1958) |

---

## NASA — 14 records (excl. COMETA) / 14 записей (без COMETA)

| Code prefix / Префикс кода | Type / Тип |
|-------------|------|
| `NASA-D1` … `NASA-D7` | Apollo/Skylab transcripts and Gemini reference docs / Транскрипты Apollo/Skylab и справочные документы Gemini |
| `NASA-VM1` … `NASA-VM6` | Apollo 12 / Apollo 17 archival images flagged for UAP review / Архивные снимки Apollo 12 / Apollo 17, помеченные для проверки НАЯ |
| `NASA-GEMINI-AUDIO` | Gemini 7 audio segment (Borman "bogey", 1965) / Аудиосегмент Gemini 7 (Borman «bogey», 1965) |

### NASA mission cross-reference / Перекрёстные ссылки миссий NASA

| Code / Код | Mission / Миссия | Year / Год | Format / Формат |
|------|---------|------|--------|
| `NASA-D1` | Apollo 12 Transcript / Транскрипт Apollo 12 | 1969 | PDF |
| `NASA-D2` | Apollo 17 Transcript / Транскрипт Apollo 17 | 1972 | PDF |
| `NASA-D3` | Gemini 7 Transcript / Транскрипт Gemini 7 | 1965 | PDF (slug `255_t_763_r1b_transcripts`) |
| `NASA-D4` | Apollo 11 Technical Crew Debriefing / Технический инструктаж экипажа Apollo 11 | 1969 | PDF |
| `NASA-D5` | Apollo 17 Crew Debriefing for Science / Научный инструктаж экипажа Apollo 17 | 1973 | PDF |
| `NASA-D6` | Apollo 17 Technical Crew Debriefing / Технический инструктаж экипажа Apollo 17 | 1973 | PDF |
| `NASA-D7` | Skylab Technical Crew Debriefing / Технический инструктаж экипажа Skylab | 1973 | PDF |
| `NASA-VM1` … `NASA-VM5` | Apollo 12 archival images / Архивные снимки Apollo 12 | 1969 | JPG |
| `NASA-VM6` | Apollo 17 archival image (triangular formation) / Архивный снимок Apollo 17 (треугольное построение) | 1972 | JPG |
| `NASA-GEMINI-AUDIO` | Gemini 7 LEO audio / Аудио Gemini 7 НОО | 1965 | MP4 |

---

## Department of State — 7 records / 7 записей

| Code / Код | Document / Документ | Date / Дата |
|------|----------|------|
| `DOS-PNG-1985` | Cable 1, Papua New Guinea / Кабель 1, Папуа Новая Гвинея | 1985-01-28 |
| `DOS-KAZ-1994` | Cable 2, Kazakhstan / Кабель 2, Казахстан | 1994-01-31 |
| `DOS-TBI-2001` | Cable 3, Tbilisi (Georgia) / Кабель 3, Тбилиси (Грузия) | 2001-10-30 |
| `DOS-MEX-2003` | Cable 5, Mexico / Кабель 5, Мексика | 2003-09-16 |
| `DOS-TKM-2004` | Cable 4, Ashgabat (Turkmenistan) / Кабель 4, Ашхабад (Туркменистан) | 2004-11-05 |
| `DOS-1952-MEMO` | 711.5612 memorandum on UFO reports / Меморандум 711.5612 об отчётах НЛО | 1952-07-18 |
| `DOS-1963-EOP-NASA` | EOP / NASA Council "alien race" planning memo / Меморандум EOP / Совета NASA о планировании по «инопланетной расе» | 1963-07-18 |

---

## Other / Прочее — 1 record / 1 запись

| Code / Код | Document / Документ |
|------|----------|
| `COMETA-1999` | French COMETA report (Carol Rosin / von Braun letter included) / Французский отчёт COMETA (включено письмо Carol Rosin / фон Брауна) |

---

# Release 02 — Source Code Additions (2026-05-22) / Дополнения кодов источников Релиз 02

64 new records, 0 overlap with Release 01. Two new agencies (CIA, DOE) and one new coordinating body (ODNI) appear in the PURSUE corpus for the first time.

**RU:** 64 новые записи, 0 пересечений с Release 01. В корпусе PURSUE впервые появляются два новых ведомства (CIA, DOE) и один координирующий орган (ODNI).

## CIA (Central Intelligence Agency) — 1 record / 1 запись

| Code / Код | Title (excerpt) / Название (фрагмент) | Date / Дата | Card |
|------|-----------------|------|-------|
| `CIA-UAP-D001` | Intelligence Information Report, USSR — Sary Shagan Weapons Testing Range / Информационный доклад ЦРУ по СССР — полигон Сары-Шаган | DOI Nov 1972 – Nov 1973 | [`CIA-UAP-D001_USSR-SARY-SHAGAN-1973.md`](../analysis/per-document/CIA-UAP-D001_USSR-SARY-SHAGAN-1973.md) |

## DOE (Department of Energy) — 3 records / 3 записи

| Code / Код | Title (excerpt) / Название (фрагмент) | Date / Дата | Card |
|------|-----------------|------|-------|
| `DOE-UAP-D001` | Enhanced PANTEX Imagery — Ground Surveillance Radar Tower / Улучшенные изображения PANTEX — башня наземного радара | — | [`DOE-UAP-D001_PANTEX-RADAR.md`](../analysis/per-document/DOE-UAP-D001_PANTEX-RADAR.md) |
| `DOE-UAP-D002` | James L. Tuck Correspondence (LANL, ball-lightning / Condon Report) / Корреспонденция Джеймса Така | 1970s | [`DOE-UAP-D002_JAMES-TUCK-CORRESPONDENCE.md`](../analysis/per-document/DOE-UAP-D002_JAMES-TUCK-CORRESPONDENCE.md) |
| `DOE-UAP-D003` | Pajarito Astronomers Invitation — Dr John Warren (AT-6) talk / Pajarito Astronomers — доклад Джона Уоррена | May 1986 | [`DOE-UAP-D003_PAJARITO-ASTRONOMERS.md`](../analysis/per-document/DOE-UAP-D003_PAJARITO-ASTRONOMERS.md) |

## ODNI (Office of the Director of National Intelligence) — 1 record / 1 запись

| Code / Код | Title (excerpt) / Название (фрагмент) | Date / Дата | Card |
|------|-----------------|------|-------|
| `ODNI-UAP-D001` | USPER Narrative, Senior USIC Official — helicopter orange-orb encounter / USPER нарратив, старший офицер разведсообщества — встреча с оранжевыми сферами | Late 2025 | [`ODNI-UAP-D001_USPER-ORANGE-ORBS-2025.md`](../analysis/per-document/ODNI-UAP-D001_USPER-ORANGE-ORBS-2025.md) |

**Pairing / Связи (official PdfPair field):** ODNI-UAP-D001 pairs with Release 01 records `FBI Photo A001`–`A008` and `FBI Photo B001`–`B024` (32 IR-photo records) plus `USPER Statement about UAP Sighting` — providing the eyewitness narrative for the R01 Western US 2025 FBI IR-photo corpus. / ODNI-UAP-D001 связан с записями Release 01 `FBI Photo A001`–`A008` и `FBI Photo B001`–`B024` (32 ИК-фото) и с `USPER Statement about UAP Sighting` — это нарратив очевидца для корпуса ИК-фотографий FBI Western US 2025 из R01.

## DoW R02 additions / Дополнения DoW в R02 — 52 records / 52 записи

### `DOW-UAP-D017` — single document / единственный документ

| Code / Код | Title (excerpt) / Название (фрагмент) | Date / Дата | Card |
|------|-----------------|------|-------|
| `DOW-UAP-D017` | UAP Reported at Sandia Base, 1948–1950 — Green-Fireball corpus / НЛО на Sandia Base, 1948–1950 — корпус «зелёных фаерболов» | 1948–1950 | [`DOW-UAP-D017_SANDIA-GREEN-FIREBALLS.md`](../analysis/per-document/DOW-UAP-D017_SANDIA-GREEN-FIREBALLS.md) |

### `DOW-UAP-PR050`–`PR099` — continuation of unresolved/pending UAP reports (videos) / продолжение нерешённых отчётов НАЯ (видео)

51 video records (50 unique DVIDS assets — `PR057a` and `PR057b` share the same source asset 1007720, segmented at the record level). All hosted on DVIDS, distributed via the war.gov video bundle `uap052226.zip` (5.6 GB). / 51 видеозапись (50 уникальных DVIDS-активов — `PR057a` и `PR057b` ссылаются на один и тот же исходный актив 1007720, сегментирование на уровне записи). Все размещены на DVIDS, распространяются через видео-bundle war.gov `uap052226.zip` (5.6 ГБ).

DVIDS ID range: `1007706`–`1007816`. CALLSIGN-redacted military encounters predominantly from CENTCOM (Iran, Syria, Iraq, Persian Gulf, Arabian Sea) and INDOPACOM (East China Sea), plus FBI Photo B-paired sightings, Eglin AFB, Tyndall AFB USCG, Lake Huron F-16C shootdown (2023), Kabul AFSOC (2017). / Диапазон DVIDS ID: `1007706`–`1007816`. Военные наблюдения с редактированным позывным, преимущественно CENTCOM (Иран, Сирия, Ирак, Персидский залив, Аравийское море) и INDOPACOM (Восточно-Китайское море), плюс наблюдения парные с FBI Photo B, Eglin AFB, Tyndall AFB USCG, сбитие F-16C над озером Гурон (2023), Кабул AFSOC (2017).

See [`catalog/documents-r02.md`](documents-r02.md) for the full chronological R02 record table. / См. полную хронологическую таблицу R02 в [`catalog/documents-r02.md`](documents-r02.md).

## NASA R02 additions / Дополнения NASA в R02 — 7 records / 7 записей

`NASA-UAP-D008`–`D014` continue the NASA debriefing audio series begun in Release 01 (which used `D1`–`D7` + `VM1`–`VM6`). All 7 R02 NASA records are **audio excerpts** (`AUD` type), distributed via the DVIDS-hosted video bundle. / `NASA-UAP-D008`–`D014` продолжают серию аудиозаписей инструктажей NASA, начатую в Release 01 (использовала `D1`–`D7` + `VM1`–`VM6`). Все 7 NASA-записей R02 — **аудиофрагменты** (тип `AUD`), распространяются через DVIDS видео-bundle.

| Code / Код | Mission / Миссия | Date / Дата |
|------|----------|------|
| `NASA-UAP-D008` | Apollo 12 Medical Debriefing, Tape 12 | 1969 |
| `NASA-UAP-D009` | Apollo 17 Audio Excerpt | Dec 7, 1972 |
| `NASA-UAP-D010` | Mercury Atlas 9 Audio Excerpt | May 15, 1963 |
| `NASA-UAP-D011` | Mercury Atlas 9 Audio Excerpt | May 15, 1963 |
| `NASA-UAP-D012` | Mercury Atlas 8 Audio Excerpt | Oct 3, 1962 |
| `NASA-UAP-D013` | Mercury Atlas 7 Audio Excerpt | May 24, 1962 |
| `NASA-UAP-D014` | Mercury-Redstone 4 Audio Excerpt | Jul 21, 1961 |

These cover the Mercury–Apollo spaceflight programmes (1961–1972). The two duplicate Mercury Atlas 9 entries (`D010` + `D011`) may be different segments of the same May 15, 1963 mission audio; verification via DVIDS metadata pending. / Покрывают пилотируемые программы Mercury–Apollo (1961–1972). Два дубликата Mercury Atlas 9 (`D010` + `D011`) могут быть разными сегментами одного и того же аудио миссии 15 мая 1963; проверка через DVIDS-метаданные ожидается.

---



Used in `Key claims` tables across `analysis/per-document/*.md` / Используются в таблицах `Key claims` в `analysis/per-document/*.md`:

- ✅ **CORROBORATED / ПОДТВЕРЖДЕНО** — claim supported by ≥2 independent sources or directly verbatim from source document / заявление подкреплено ≥2 независимыми источниками или дословно из исходного документа
- ⚠ **PARTIAL / ЧАСТИЧНОЕ** — partial / contradictory description, needs verification / частичное / противоречивое описание, требует верификации
- ❌ **EXPLAINED/MUNDANE / ОБЪЯСНЕНО/ОБЫДЕННОЕ** — officially explained or misattributed / официально объяснено или неверно атрибутировано
- ⬜ **UNRESOLVED / НЕРЕШЁННОЕ** — AARO pending, no explanation / AARO ожидает, объяснения нет
- ⬛ **REDACTED / РЕДАКТИРОВАНО** — substantial portion hidden, assessment impossible / существенная часть скрыта, оценка невозможна
- 🟧 **ANALYTICAL FLAG / АНАЛИТИЧЕСКИЙ ФЛАГ** — used in two related senses across `analysis/per-document/DOW-PR*.md` cards / используется в двух связанных значениях в карточках `analysis/per-document/DOW-PR*.md`:
  1. **AARO METADATA INCONSISTENCY / LIKELY MISLABELED BY AARO / НЕСОГЛАСОВАННОСТЬ МЕТАДАННЫХ AARO / ВЕРОЯТНО НЕВЕРНО РАЗМЕЧЕНО AARO** — AARO's portal description points to one record while content matches a different record (e.g. PR28 labeled D7 but content matches D25; PR29 labeled D8 but content matches D27). Distinguishes upstream metadata error from source-document uncertainty. / Описание портала AARO указывает на одну запись, тогда как содержание соответствует другой (напр. PR28 размечен как D7, но содержание соответствует D25; PR29 размечен как D8, но соответствует D27). Отличает ошибку метаданных вышестоящего источника от неопределённости исходного документа.
  2. **PLAUSIBLE INTERPRETATION / PROSAIC EXPLANATION / ОБОСНОВАННАЯ ИНТЕРПРЕТАЦИЯ / ОБЫДЕННОЕ ОБЪЯСНЕНИЕ** — analyst-side hypothesis that the observation has a mundane explanation (e.g. PR38 "8-pointed star" likely Cassegrain telescope diffraction artifact; PR42 position-shift on sensor-mode switch likely boresight misalignment). Not officially closed by AARO but flagged as the analyst's most-plausible reading. / Гипотеза аналитика о том, что наблюдение имеет обыденное объяснение (напр. «8-конечная звезда» PR38 — вероятный дифракционный артефакт телескопа Кассегрена; смещение положения при переключении режима датчика PR42 — вероятное угловое рассогласование). Официально не закрыто AARO, но помечено как наиболее вероятное прочтение аналитика.

  Both senses share the property of being "analyst-derived assessments not present in the source document". Use ⚠ PARTIAL when the source itself is contradictory; use 🟧 when the document is consistent but the analyst infers a non-source-supported interpretation. / Оба значения объединяет свойство «оценок, полученных аналитиком, отсутствующих в исходном документе». Используйте ⚠ PARTIAL когда источник сам противоречив; используйте 🟧 когда документ согласован, но аналитик выводит интерпретацию, не поддержанную источником.

## Naming convention notes / Примечания к конвенции именования

- DOS country codes: standard 3-letter ISO-3166 where unambiguous. `DOS-TKM-2004` uses Turkmenistan ISO code (Ashgabat is its capital); `DOS-TBI-2001` uses Tbilisi (city) rather than country code GEO because the cable is from the US embassy in Tbilisi during the post-Soviet Russia/Georgia airspace dispute. / Коды стран DOS: стандартные 3-буквенные ISO-3166 где однозначно. `DOS-TKM-2004` использует ISO-код Туркменистана (Ашхабад — его столица); `DOS-TBI-2001` использует Тбилиси (город), а не код страны GEO, поскольку кабель отправлен из посольства США в Тбилиси в период постсоветского российско-грузинского воздушного спора.
- DOS year-prefixed codes (`DOS-1952-MEMO`, `DOS-1963-EOP-NASA`): used for memoranda where no specific country is the subject; year+keyword distinguishes them from country cables. / Коды DOS с префиксом года (`DOS-1952-MEMO`, `DOS-1963-EOP-NASA`): используются для меморандумов, где конкретная страна не является предметом; год+ключевое слово отличает их от страновых кабелей.

## Card section conventions / Конвенции секций карточек

- All per-document cards have six sections: **Metadata / Summary / Key claims / Cross-references / Open questions / Notes**. / Все карточки по документам имеют шесть секций: **Metadata / Summary / Key claims / Cross-references / Open questions / Notes**.
- For image-only PDFs (`FBI-IR-A*` / `B*` photos) and video-only records (`DOW-PR*`), the **Open questions** section may use a templated boilerplate that defers to the relevant `analysis/topical/*.md` cluster synthesis — this is by design, since per-card differentiation is limited by the templated source content. Per-card open questions are inappropriate where the underlying record is a near-identical sibling within a known cluster. / Для PDF только с изображениями (`FBI-IR-A*` / `B*` фото) и записей только с видео (`DOW-PR*`) секция **Open questions** может использовать шаблонный шаблон, отсылающий к соответствующему тематическому кластерному синтезу `analysis/topical/*.md` — это по замыслу, поскольку дифференциация по карточкам ограничена шаблонным содержанием источника. Открытые вопросы по карточке неуместны там, где базовая запись почти идентична сиблингу в известном кластере.
- For information-rich records (MISREPs, FBI sections, NASA debriefings, DoS cables, ELLIPSE serials), Open questions should be specific and case-derived. / Для информационно насыщенных записей (рапорты о миссиях MISREP, разделы FBI, инструктажи NASA, кабели Госдепа, серийные ELLIPSE) открытые вопросы должны быть конкретными и производными от дела.

## Cross-archive code conventions (out of scope) / Конвенции кодов кросс-архивов (вне объёма)

When linking PURSUE codes from other archives, prefix with the archive name / При ссылке на коды PURSUE из других архивов — добавляйте префикс с именем архива:
- `[war-gov-pursue:DOW-PR34]` from another archive's MASTER
- `[bob-lazar-archive:F-S4-2026-DOC]` reference from PURSUE MASTER

This convention is used in `analysis/cross-archive-synthesis.md` and `graph/fragments/agentI_war_gov_pursue.py`. / Эта конвенция используется в `analysis/cross-archive-synthesis.md` и `graph/fragments/agentI_war_gov_pursue.py`.
