# Filtered-out sources (irrelevant to Gershtein) / Отфильтрованные источники (нерелевантные Герштейну)

Of the 55 URLs Perplexity returned, the 5 below were judged unrelated to Mikhail B.
Gershtein himself or his work and were therefore excluded from the corpus. They are
kept here for traceability only.

| # | URL | Reason it was filtered out |
|---|---|---|
| 1 | <https://ru.yamaha.com/ru/about-yamaha/yasm/> | Yamaha music school in Moscow — false-positive from a "Yamaha-Soyuz" string match. |
| 2 | <https://artsmoscow.ru/artists/aleksey-rybnikov> | Aleksey Rybnikov composer biography — surfaced via "Rybnikov" co-occurrence, no Gershtein content. |
| 3 | <https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D1%85%D0%B0%D1%80%D0%BE%D0%B2,_%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9_%D0%94%D0%BC%D0%B8%D1%82%D1%80%D0%B8%D0%B5%D0%B2%D0%B8%D1%87> | A. D. Sakharov Wikipedia page — likely surfaced from a Sakharov-era physics tangent in the dialog, no Gershtein content. |
| 4 | <https://www.tiktok.com/@bednovcovers/video/7193719311377222918> | TikTok cover song "Ваше благородие" — co-occurrence of unrelated music tag, no Gershtein content. |
| 5 | <https://polpred.com/news?wregion=23&fo=1> | Russian Central Federal District news aggregator landing page — no Gershtein content visible. |

## Other gaps recorded in the dataset

- **1 YouTube video unavailable** at the time of download: `nuiQhQ1Ap2s` (geo/age-restricted or removed).
- **2 paywalled book sources skipped**:
  - `lib-dpr.ru` (initially returned HTTP 0; on retry returned 23 KB stub — kept in `books/catalog_pages/` but content not paywalled-bypassed).
  - `ast.ru` (publisher catalog — original URL 404; retried via search page, 163 KB landing kept in `books/catalog_pages/`).
