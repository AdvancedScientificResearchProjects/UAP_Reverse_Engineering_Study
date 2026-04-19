#!/bin/bash
set -u
cd <repo>/chernobrov-archive/ocr-pipeline
source .venv/bin/activate
mkdir -p out

UFO_PDF=<repo>/chernobrov-archive/books/downloads/enciklopediya_ufologii.pdf
VBCH_PDF=<repo>/chernobrov-archive/books/downloads/vremya_bessmertie_chelovek_2010.pdf

run_chunk() {
    local pdf="$1"; local out="$2"; local pr="$3"
    echo "=== $(date +%H:%M:%S) START $out [$pr] ==="
    .venv/bin/python run_ocr.py "$pdf" "$out" --page-range "$pr" --device cuda 2>&1 | tail -3
    echo "=== $(date +%H:%M:%S) DONE $out (size: $(wc -c < "$out") bytes) ==="
}

# Энциклопедия уфологии — 468 страниц, чанки по 100
for r in 1-100 101-200 201-300 301-400 401-468; do
    run_chunk "$UFO_PDF" "out/ufologii_${r/-/_}.md" "$r"
done

# ВБЧ 2010 — 322 страницы, чанки по 100
for r in 1-100 101-200 201-300 301-322; do
    run_chunk "$VBCH_PDF" "out/vbch_${r/-/_}.md" "$r"
done

# Объединение
cat out/ufologii_*.md > out/ufologii_FULL.md
cat out/vbch_*.md > out/vbch_FULL.md

echo "=== ALL DONE $(date +%H:%M:%S) ==="
echo "ufologii_FULL.md: $(wc -c < out/ufologii_FULL.md) bytes / $(wc -l < out/ufologii_FULL.md) lines"
echo "vbch_FULL.md: $(wc -c < out/vbch_FULL.md) bytes / $(wc -l < out/vbch_FULL.md) lines"
