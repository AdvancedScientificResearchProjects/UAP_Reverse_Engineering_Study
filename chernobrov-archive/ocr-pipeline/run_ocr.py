"""OCR Russian-language scanned PDFs via docling on GPU (or CPU fallback).

Usage:
    .venv/bin/python run_ocr.py <input.pdf> <output.txt> [--page-range A-B]

Two-stage strategy for large image-only scans (Russian):
  1. layout + table detection on accelerator
  2. RapidOCR / EasyOCR (Russian) per page
"""
import sys
import time
import argparse
from pathlib import Path

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    EasyOcrOptions,
    AcceleratorOptions,
    AcceleratorDevice,
)
from docling.document_converter import DocumentConverter, PdfFormatOption


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input", type=Path)
    ap.add_argument("output", type=Path)
    ap.add_argument("--page-range", default=None, help="A-B (1-indexed)")
    ap.add_argument("--lang", default="ru,en")
    ap.add_argument("--device", default="cuda", choices=["cuda", "cpu", "auto"])
    args = ap.parse_args()

    if not args.input.exists():
        sys.exit(f"input not found: {args.input}")

    page_range = None
    if args.page_range:
        a, b = args.page_range.split("-")
        page_range = (int(a), int(b))

    langs = args.lang.split(",")
    print(f"OCR languages: {langs}")
    print(f"Device: {args.device}")
    if page_range:
        print(f"Page range: {page_range[0]}-{page_range[1]}")

    device_map = {
        "cuda": AcceleratorDevice.CUDA,
        "cpu": AcceleratorDevice.CPU,
        "auto": AcceleratorDevice.AUTO,
    }

    pipeline_opts = PdfPipelineOptions(
        do_ocr=True,
        ocr_options=EasyOcrOptions(
            lang=langs,
            force_full_page_ocr=True,
            use_gpu=(args.device == "cuda"),
        ),
        do_table_structure=False,
        accelerator_options=AcceleratorOptions(
            num_threads=4, device=device_map[args.device]
        ),
    )

    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_opts),
        }
    )

    t0 = time.time()
    convert_kw = {}
    if page_range:
        convert_kw["page_range"] = page_range

    result = converter.convert(args.input, **convert_kw)
    md = result.document.export_to_markdown()

    args.output.write_text(md, encoding="utf-8")
    elapsed = time.time() - t0
    npages = len(result.document.pages) if hasattr(result.document, "pages") else "?"
    print(
        f"DONE: {args.output} ({len(md)/1024:.1f} KB) "
        f"in {elapsed:.1f}s, pages={npages}"
    )


if __name__ == "__main__":
    main()
