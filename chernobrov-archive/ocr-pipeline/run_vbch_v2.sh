#!/bin/bash
set -u
WORK=/tmp/vbch_ocr_work
OUT=<repo>/chernobrov-archive/ocr-pipeline/out
mkdir -p "$WORK/binarized" "$WORK/txt2"

NUM=$(ls "$WORK/pages"/*.png 2>/dev/null | wc -l)
echo "=== $(date +%H:%M:%S) Binarize+OCR $NUM pages ==="

i=0
for png in "$WORK/pages"/p-*.png; do
    base=$(basename "$png" .png)
    bin="$WORK/binarized/$base.png"
    if [ ! -s "$bin" ]; then
        convert "$png" -threshold 50% "$bin" 2>/dev/null
    fi
    tesseract "$bin" "$WORK/txt2/$base" -l rus 2>/dev/null
    i=$((i+1))
    if [ $((i % 20)) -eq 0 ]; then
        echo "  $(date +%H:%M:%S) [$i/$NUM]"
    fi
done

echo "=== $(date +%H:%M:%S) Concatenating ==="
{
    echo "# OCR Result: Время, Бессмертие, Человек (2010, Рипол Классик)"
    echo "# Source: vremya_bessmertie_chelovek_2010.pdf"
    echo "# Method: pdftoppm 200dpi + ImageMagick threshold 50% + tesseract 5.5 rus"
    echo
    for txt in "$WORK/txt2"/p-*.txt; do
        page=$(basename "$txt" .txt | sed 's/p-0*//')
        if [ -s "$txt" ]; then
            echo "## Page $page"
            echo
            cat "$txt"
            echo
        fi
    done
} > "$OUT/vbch_FULL.md"

echo "=== $(date +%H:%M:%S) DONE ==="
echo "Output: $OUT/vbch_FULL.md"
echo "Size: $(wc -c < "$OUT/vbch_FULL.md") bytes / $(wc -l < "$OUT/vbch_FULL.md") lines"
