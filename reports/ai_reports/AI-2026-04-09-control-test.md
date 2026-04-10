# AI CONTROL TEST REPORT / ОТЧЁТ КОНТРОЛЬНОГО ТЕСТА ИИ

## Session Information / Информация Сессии

| Field / Поле | Value / Значение |
|-------------|------------------|
| **Test ID / ID Теста** | AI-2026-04-09-CTRL |
| **Date / Дата** | 2026-04-09 |
| **Model / Модель** | google/siglip2-so400m-patch14-384 (SigLIP2 zero-shot) |
| **Scoring / Скоринг** | Sigmoid (independent per-prompt, 0-1) |
| **Device / Устройство** | CPU (float32) |
| **Protocol reference / Ссылка на протокол** | Identical to `pipeline/stages/s5_material.py` |

---

## 1. PURPOSE / ЦЕЛЬ

### EN

This control test determines whether the SigLIP2 material classifier can distinguish artifact UAP-FRAG-001 from genuine echinoid (sea urchin) fossils. The original AI report scored the artifact at 0.98 for "coral or sea urchin fossil" (using a cropped artifact image). This test uses the full artifact photograph and compares it against 12 control images spanning three categories: morphologically similar fossils, dissimilar biological specimens, and non-biological objects.

### RU

Контрольный тест определяет, может ли классификатор материалов SigLIP2 отличить артефакт UAP-FRAG-001 от настоящих окаменелостей морских ежей (эхиноидов). Оригинальный ИИ-отчёт оценил артефакт в 0.98 для "coral or sea urchin fossil" (на обрезанном изображении). Данный тест использует полную фотографию артефакта и сравнивает её с 12 контрольными изображениями в трёх категориях: морфологически похожие окаменелости, непохожие биологические образцы и небиологические объекты.

---

## 2. CONTROL IMAGE GROUPS / ГРУППЫ КОНТРОЛЬНЫХ ИЗОБРАЖЕНИЙ

### Group A: Morphologically Similar Fossils / Морфологически похожие окаменелости

Round, textured echinoid fossils — the primary comparison group.
Округлые, текстурированные окаменелости эхиноидов — основная группа сравнения.

| ID | Image / Изображение | Description / Описание | Source / Источник | Resolution / Разрешение | Brightness (V) |
|----|--------------------|-----------------------|-----------------|------------------------|----------------|
| A1 | `dark-urchin-hq-1.jpg` | Dark textured echinoid, round, held in hand / Тёмный текстурированный эхиноид | Google Images | 201×251 (30KB) | 148 |
| A2 | `fossil-cidaroida-carboniferous.jpg` | Archaeocidaris brownwoodensis, ~300 Mya / Археоцидарис, ~300 млн лет | Wikimedia MHNT | 1024×843 (504KB) | 164 |
| A3 | `fossil-sea-urchin-field.jpg` | Field-found echinoid with ruler / Полевая находка с линейкой | Wikimedia (FindID) | 1024×628 (172KB) | 167 |
| A4 | `fossil-cidaroida-triassic.jpg` | Miocidaris coaeva, ~240 Mya / Миоцидарис, ~240 млн лет | Wikimedia MHNT | 1024×696 (417KB) | 169 |
| A5 | `fossil-echinoid-cretaceous.jpg` | Echinocorys, ~80 Mya / Эхинокорис, ~80 млн лет | Wikimedia | 300×225 (15KB) | — |
| A6 | `control-fossil-2.jpg` | Round textured echinoid, Google thumbnail / Округлый текстурированный эхиноид, миниатюра Google | Google Images | ~200×200 (14KB) | — |

**Note / Примечание:** A6 is a low-resolution Google thumbnail included for completeness. Its score (0.9962) is the highest among all controls but may be inflated by image compression artifacts. / A6 — это миниатюра Google низкого разрешения, включённая для полноты. Её скор (0.9962) — самый высокий среди контролей, но может быть завышен артефактами сжатия.

### Group B: Dissimilar Biological / Непохожие биологические

| ID | Image / Изображение | Description / Описание | Score |
|----|--------------------|-----------------------|-------|
| B1 | `control-1-cidaridae.jpg` | Living Cidaridae with spines / Живой Cidaridae с иглами | 0.2093 |
| B2 | `control-fossil-0.jpg` | Scientific plate, multiple specimens / Научная пластина | 0.1407 |
| B3 | `dark-urchin-hq-0.jpg` | Dark flint echinoid, smooth / Тёмный кремнёвый, гладкий | 0.1775 |
| B4 | `urchin-test-clean.jpg` | Clean test (shell without spines) / Панцирь без игл | 0.0648 |
| B5 | `cidaridae-test-no-spines.jpg` | Cidaridae test (shell) / Панцирь Cidaridae | 0.0354 |

### Group C: Non-Biological Negatives / Небиологические негативные контроли

| ID | Image / Изображение | Description / Описание | Score |
|----|--------------------|-----------------------|-------|
| C1 | `control-metal-0.jpg` | Rusty metal part in ground / Ржавая деталь в земле | 0.0001 |
| C2 | `control-stone-0.jpg` | Stone with mineral deposits / Камень с минералами | 0.0226 |

---

## 3. RESULTS / РЕЗУЛЬТАТЫ

### 3.1. Bio/Organic Scores — Full Table / Полная таблица скоров

| Image / Изображение | Group / Группа | Bio/Organic Score | Brightness (V) |
|---------------------|---------------|-------------------|-----------------|
| **UAP-FRAG-001** | **Test subject** | **0.8912** | **90** |
| A1: Dark textured urchin | Similar fossil | 0.9870 | 148 |
| A2: Fossil Carboniferous | Similar fossil | 0.7801 | 164 |
| A3: Fossil field | Similar fossil | 0.7420 | 167 |
| A4: Fossil Triassic | Similar fossil | 0.7068 | 169 |
| A5: Fossil Cretaceous | Similar fossil | 0.4441 | — |
| A6: Round echinoid (thumbnail) | Similar fossil | 0.9962 | — |
| B1: Living Cidaridae | Dissimilar bio | 0.2093 | — |
| B3: Dark flint echinoid | Dissimilar bio | 0.1775 | 90 |
| B2: Scientific plate | Dissimilar bio | 0.1407 | — |
| B4: Urchin test clean | Dissimilar bio | 0.0648 | — |
| B5: Cidaridae test | Dissimilar bio | 0.0354 | — |
| C2: Mineral stone | Negative | 0.0226 | — |
| C1: Rusty metal | Negative | 0.0001 | — |

### 3.2. Statistical Summary — Group A (Similar Fossils) / Статистическая сводка

**Primary analysis (n=5, HQ images only, excluding A6 thumbnail) / Основной анализ (n=5, только HQ, без миниатюры A6):**

| Metric / Метрика | Value / Значение |
|-----------------|-----------------|
| **N (similar fossils)** | 5 |
| **Mean / Среднее** | 0.7320 |
| **Median / Медиана** | 0.7420 |
| **Std (population) / Стд. откл.** | 0.1738 |
| **Range / Диапазон** | 0.4441 — 0.9870 |
| **UAP-FRAG-001** | **0.8912** |
| **Z-score** | **0.916** |
| **Percentile / Процентиль** | **80th** |
| **Position / Позиция** | Above mean by +0.159 / Выше среднего на +0.159 |

**Sensitivity check with A6 included (n=6) / Проверка устойчивости с A6 (n=6):**

| Metric / Метрика | Value / Значение |
|-----------------|-----------------|
| **N** | 6 |
| **Mean / Среднее** | 0.7760 |
| **Median / Медиана** | 0.7611 |
| **Std (population) / Стд. откл.** | 0.1867 |
| **Z-score** | **0.617** |
| **Percentile / Процентиль** | **67th** |

> Conclusion is robust: with or without A6, the artifact falls within 1 std of the fossil mean and is not statistically distinguishable. / Вывод устойчив: с A6 или без, артефакт в пределах 1 стд. откл. от среднего и статистически неразличим.

### 3.3. Separation Analysis / Анализ разделения

| Comparison / Сравнение | Delta |
|-----------------------|-------|
| Artifact vs highest negative control (B1: 0.209) / Артефакт vs лучший негативный контроль | **+0.682** |
| Artifact vs mean of similar fossils (0.732) / Артефакт vs среднее похожих окаменелостей | **+0.159** |
| Artifact vs best matching fossil (A1: 0.987) / Артефакт vs лучшее совпадение | **−0.096** |

### 3.4. Color Analysis (OpenCV) / Анализ цвета

| Image / Изображение | Brightness (V) | Hue (H) | Saturation (S) | Color profile / Цветовой профиль |
|---------------------|----------------|---------|----------------|----------------------------------|
| **UAP-FRAG-001** | **90** | **89 (blue-gray)** | **42** | **Dark, blue-gray / Тёмный, сине-серый** |
| Dark flint (B3) | 90 | 102 (blue-gray) | 29 | Dark, gray / Тёмный, серый |
| Dark textured (A1) | 148 | 32 (warm) | 69 | Medium, warm / Средний, тёплый |
| Light fossils (A2-A4) | 164-169 | 15-82 | 40-51 | Light, warm / Светлый, тёплый |

**Color observation / Наблюдение по цвету:** UAP-FRAG-001 is approximately 2× darker (V=90) than typical light-colored echinoid fossils (V=164-169) and has an unusual blue-gray hue (H=89) rather than the warm beige/yellow typical of calcified fossils (H=15-31). / UAP-FRAG-001 примерно в 2 раза темнее типичных светлых окаменелостей (V=90 vs 164-169) и имеет нетипичный сине-серый оттенок (H=89) вместо тёплого бежевого/жёлтого, характерного для кальцифицированных окаменелостей (H=15-31).

---

## 4. ANALYSIS / АНАЛИЗ

### EN

**Finding 1: The artifact is clearly biological/organic-looking.**
The artifact scores 0.891 — far above all negative controls (max 0.023) and dissimilar biological specimens (max 0.209). The model unambiguously places it in the biological/organic category. There is no visual ambiguity between the artifact and non-biological objects.

**Finding 2: The artifact falls within the range of real fossils.**
The Z-score of 0.916 (80th percentile) means the artifact is above the mean of similar fossils but within one standard deviation. At n=5, this is **not statistically distinguishable** from the natural fossil population (t > 2.776 required for df=4, p < 0.05).

**Finding 3: The artifact scores below the best-matching fossil.**
The closest visual analog (dark textured urchin, A1) scores 0.987 — higher than the artifact's 0.891. The gap of 0.096 (9.6%) is consistent across tests. This means the artifact's surface has visual properties that deviate from a "textbook" echinoid fossil.

**Finding 4: The artifact has anomalous coloration.**
At V=90 (dark, blue-gray), the artifact is significantly darker than all Group A fossils (V=148-169) except the flint-embedded specimen. Echinoid fossils are typically light-colored (calcite/silica replacement). Dark blue-gray coloration could indicate:
- (a) Pyritization (iron sulfide replacement) — would explain dark metallic appearance
- (b) Phosphatization — dark phosphatic preservation
- (c) Non-biological material mimicking biological morphology
- (d) Artificial modification or manufacturing

**Finding 5: SigLIP2 cannot resolve the question.**
The model classifies visual morphology, not material composition. It cannot distinguish between a genuine dark pyritized echinoid fossil and a non-biological object with echinoid-like surface geometry. Only laboratory analysis can determine this.

### RU

**Вывод 1: Артефакт выглядит однозначно биологически/органически.**
Скор 0.891 — намного выше всех негативных контролей (макс 0.023) и непохожих биологических (макс 0.209). Модель однозначно помещает его в биологическую/органическую категорию.

**Вывод 2: Артефакт попадает в диапазон реальных окаменелостей.**
Z-score 0.916 (80-й процентиль) означает, что артефакт выше среднего по похожим окаменелостям, но в пределах одного стандартного отклонения. При n=5 это **статистически неразличимо** от популяции природных окаменелостей.

**Вывод 3: Артефакт набирает меньше, чем лучшее совпадение.**
Ближайший аналог (тёмный текстурированный ёж, A1) — 0.987. Разрыв 0.096 (9.6%) стабилен. Поверхность артефакта имеет свойства, отклоняющиеся от "идеальной" окаменелости.

**Вывод 4: Артефакт имеет аномальную окраску.**
При V=90 (тёмный, сине-серый) артефакт значительно темнее всех окаменелостей группы A (V=148-169). Типичные окаменелости эхиноидов — светлые (замещение кальцитом/кремнезёмом). Тёмная сине-серая окраска может указывать на пиритизацию, фосфатизацию, небиологический материал, имитирующий биологическую морфологию, или искусственную модификацию.

**Вывод 5: SigLIP2 не может разрешить вопрос.**
Модель классифицирует визуальную морфологию, а не состав. Только лабораторный анализ может определить, является ли это настоящей пиритизированной окаменелостью или небиологическим объектом с биоморфной геометрией поверхности.

---

## 5. VISUAL SUMMARY / ВИЗУАЛЬНАЯ СВОДКА

```
Score scale / Шкала скоров:
0.0                    0.25                   0.5                    0.75                   1.0
|----------------------|----------------------|----------------------|----------------------|
C1  C2  B5 B4  B3 B2 B1                      A5          A4  A3 A2       [FRAG-001]  A1
0.00  0.02 0.04  0.14 0.21                     0.44        0.71 0.74 0.78    0.89      0.99
|------- NEGATIVES ----|---- DISSIMILAR BIO --|------------- SIMILAR FOSSILS --------------|
                                                                    ↑
                                                              ARTIFACT
                                                              Z=0.92
                                                              80th percentile
```

---

## 6. LIMITATIONS / ОГРАНИЧЕНИЯ

### EN

1. **Small sample size (n=5 similar fossils).** Statistical conclusions are indicative, not definitive. A rigorous test requires 20-30 comparable specimens photographed in identical conditions.

2. **Heterogeneous image sources.** Control images come from different cameras, lighting, backgrounds, and resolutions (15KB to 504KB). The artifact was photographed in controlled studio conditions on a slate base. These differences affect model scores.

3. **No identical-condition controls.** The ideal test would photograph a genuine echinoid fossil and the artifact side-by-side with the same camera, lighting, and background.

4. **Single-model evaluation.** Only SigLIP2 zero-shot was used. Cross-validation with DINOv2 cosine similarity or CLIP would provide stronger evidence.

5. **RGB limitation.** The model cannot detect chemical composition, radioactivity, internal structure, or density — the properties most relevant to distinguishing "biometal" from fossil.

### RU

1. **Малый размер выборки (n=5).** Статистические выводы индикативны, не окончательны.
2. **Гетерогенные источники изображений.** Разные камеры, освещение, фон, разрешения.
3. **Нет контролей в идентичных условиях.**
4. **Один метод.** Только SigLIP2 zero-shot.
5. **Ограничение RGB.** Модель не определяет химсостав, радиоактивность, внутреннюю структуру.

---

## 7. RECOMMENDED NEXT STEPS / РЕКОМЕНДУЕМЫЕ СЛЕДУЮЩИЕ ШАГИ

| # | Step / Шаг | Purpose / Цель | Priority / Приоритет |
|---|-----------|---------------|---------------------|
| 1 | Photograph genuine echinoid fossil in identical conditions / Сфотографировать настоящую окаменелость в идентичных условиях | Eliminate photography bias / Устранить фотографический bias | High / Высокий |
| 2 | Run DINOv2 cosine similarity (artifact embedding vs fossil embedding) / Запустить DINOv2 cosine similarity | Cross-validate with second method / Кросс-валидация | High / Высокий |
| 3 | XRF/SEM-EDS elemental mapping / Элементное картирование XRF/SEM-EDS | Determine if pyritized fossil (Fe+S) or anomalous composition / Определить состав | Critical / Критический |
| 4 | Gamma spectroscopy over time / Гамма-спектроскопия в динамике | Test variable radioactivity / Проверить переменную радиоактивность | Critical / Критический |

---

## 8. CONCLUSION / ЗАКЛЮЧЕНИЕ

### EN

The SigLIP2 control test places UAP-FRAG-001 within the statistical range of genuine echinoid fossils (Z=0.92, 80th percentile, n=5). The artifact is not statistically distinguishable from real fossils by visual classification alone.

However, three observations warrant further investigation:
1. The artifact scores 9.6% below the best-matching dark fossil — a consistent gap across all test rounds
2. The artifact's blue-gray coloration (H=89, V=90) is atypical for calcified echinoid fossils (typically warm-toned, V>150)
3. The reference data describes "biometal" and "variable radioactivity" — properties invisible to RGB analysis

**The control test neither confirms nor excludes anomalous origin.** It establishes that the artifact is visually consistent with but not identical to known echinoid fossils. Laboratory analysis (SEM-EDS, XRF, gamma spectroscopy) is required to resolve the question.

### RU

Контрольный тест SigLIP2 помещает UAP-FRAG-001 в статистический диапазон настоящих окаменелостей эхиноидов (Z=0.92, 80-й процентиль, n=5). Артефакт статистически неразличим от реальных окаменелостей только по визуальной классификации.

Тем не менее три наблюдения требуют дальнейшего исследования:
1. Артефакт набирает на 9.6% меньше лучшего тёмного аналога — стабильный разрыв во всех раундах
2. Сине-серая окраска (H=89, V=90) нетипична для кальцифицированных окаменелостей (обычно тёплые тона, V>150)
3. Референсные данные описывают "биометалл" и "переменную радиоактивность" — свойства, невидимые для RGB-анализа

**Контрольный тест не подтверждает и не исключает аномальное происхождение.** Он устанавливает, что артефакт визуально совместим, но не идентичен известным окаменелостям эхиноидов. Для разрешения вопроса необходим лабораторный анализ.

---

## 9. RAW DATA / СЫРЫЕ ДАННЫЕ

### Control Images / Контрольные изображения

All images stored in [`data/raw/control-images/`](../../data/raw/control-images/):
Все изображения хранятся в [`data/raw/control-images/`](../../data/raw/control-images/):

| ID | File / Файл | Group / Группа |
|----|------------|---------------|
| Test | [`artifact-uap-frag-001.jpg`](../../data/raw/control-images/artifact-uap-frag-001.jpg) | Test subject / Объект исследования |
| A1 | [`dark-urchin-hq-1.jpg`](../../data/raw/control-images/dark-urchin-hq-1.jpg) | Similar fossil / Похожая окаменелость |
| A2 | [`fossil-cidaroida-carboniferous.jpg`](../../data/raw/control-images/fossil-cidaroida-carboniferous.jpg) | Similar fossil / Похожая окаменелость |
| A3 | [`fossil-sea-urchin-field.jpg`](../../data/raw/control-images/fossil-sea-urchin-field.jpg) | Similar fossil / Похожая окаменелость |
| A4 | [`fossil-cidaroida-triassic.jpg`](../../data/raw/control-images/fossil-cidaroida-triassic.jpg) | Similar fossil / Похожая окаменелость |
| A5 | [`fossil-echinoid-cretaceous.jpg`](../../data/raw/control-images/fossil-echinoid-cretaceous.jpg) | Similar fossil / Похожая окаменелость |
| A6 | [`control-fossil-2.jpg`](../../data/raw/control-images/control-fossil-2.jpg) | Similar fossil (thumbnail) / Похожая (миниатюра) |
| B1 | [`control-1-cidaridae.jpg`](../../data/raw/control-images/control-1-cidaridae.jpg) | Dissimilar bio / Непохожий биологический |
| B2 | [`control-fossil-0.jpg`](../../data/raw/control-images/control-fossil-0.jpg) | Dissimilar bio / Непохожий биологический |
| B3 | [`dark-urchin-hq-0.jpg`](../../data/raw/control-images/dark-urchin-hq-0.jpg) | Dissimilar bio / Непохожий биологический |
| B4 | [`urchin-test-clean.jpg`](../../data/raw/control-images/urchin-test-clean.jpg) | Dissimilar bio / Непохожий биологический |
| B5 | [`cidaridae-test-no-spines.jpg`](../../data/raw/control-images/cidaridae-test-no-spines.jpg) | Dissimilar bio / Непохожий биологический |
| C1 | [`control-metal-0.jpg`](../../data/raw/control-images/control-metal-0.jpg) | Negative / Негативный |
| C2 | [`control-stone-0.jpg`](../../data/raw/control-images/control-stone-0.jpg) | Negative / Негативный |

### JSON Results / Результаты JSON

- [`data/processed/control-test-results.json`](../../data/processed/control-test-results.json)
- [`data/processed/control-hq-results.json`](../../data/processed/control-hq-results.json)

### Methods / Методы

- Color analysis / Анализ цвета: OpenCV HSV center-crop
- Statistical calculations / Статистика: numpy (mean, median, std, z-score)

---

**Report Date / Дата отчёта:** 2026-04-09
**Analyst / Аналитик:** Zmiienko Kyryl / Змиенко Кирилл
**Status / Статус:** COMPLETE / ЗАВЕРШЁН

---

**ASRP RESEARCH STANDARD v2.1**
