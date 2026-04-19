#!/bin/bash
set -u
PDF=/home/liker2/asrp-audit/UAP_Reverse_Engineering_Study/chernobrov-archive/books/downloads/vremya_bessmertie_chelovek_2010.pdf
WORK=/tmp/vbch_ocr_work
OUT=/home/liker2/asrp-audit/UAP_Reverse_Engineering_Study/chernobrov-archive/ocr-pipeline/out
TESSDATA=$HOME/.tesseract

mkdir -p "$WORK/pages"
mkdir -p "$WORK/txt"

echo "=== $(date +%H:%M:%S) Converting PDF -> PNG (200 DPI) ==="
pdftoppm -r 200 -png "$PDF" "$WORK/pages/p" 2>&1 | tail -3
NUM=$(ls "$WORK/pages"/*.png 2>/dev/null | wc -l)
echo "=== $(date +%H:%M:%S) Got $NUM PNGs ==="

echo "=== $(date +%H:%M:%S) Running tesseract rus+eng on $NUM pages ==="
i=0
for png in "$WORK/pages"/p-*.png; do
    base=$(basename "$png" .png)
    TESSDATA_PREFIX="$TESSDATA" tesseract "$png" "$WORK/txt/$base" -l rus+eng 2>/dev/null
    i=$((i+1))
    if [ $((i % 25)) -eq 0 ]; then
        echo "  $(date +%H:%M:%S) [$i/$NUM]"
    fi
done

echo "=== $(date +%H:%M:%S) Concatenating ==="
{
    echo "# OCR Result: Время, Бессмертие, Человек (2010)"
    echo "# Source: vremya_bessmertie_chelovek_2010.pdf"
    echo "# Method: pdftoppm 200dpi + tesseract 5.5 rus+eng"
    echo
    for txt in "$WORK/txt"/p-*.txt; do
        page=$(basename "$txt" .txt | sed 's/p-0*//')
        echo "## Page $page"
        echo
        cat "$txt"
        echo
    done
} > "$OUT/vbch_FULL.md"

echo "=== $(date +%H:%M:%S) DONE ==="
echo "Output: $OUT/vbch_FULL.md"
echo "Size: $(wc -c < "$OUT/vbch_FULL.md") bytes / $(wc -l < "$OUT/vbch_FULL.md") lines"
