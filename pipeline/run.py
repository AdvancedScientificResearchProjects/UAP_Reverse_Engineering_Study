#!/usr/bin/env python3
import sys
import time
from pathlib import Path

# Ensure pipeline package is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from pipeline.utils.vram import unload_model

from pipeline.stages import (
    s0_preprocess,
    s1_detect,
    s2_segment,
    s3_features,
    s4_siglip,
    s5_material,
    s6_anomaly_ead,
    s7_anomaly_clip,
    s8_depth,
    s9_report,
)


STAGES = [
    ("s0_preprocess", s0_preprocess, True),
    ("s1_detect", s1_detect, True),
    ("s2_segment", s2_segment, True),
    ("s3_features", s3_features, False),
    ("s4_siglip", s4_siglip, False),
    ("s5_material", s5_material, False),
    ("s6_anomaly_ead", s6_anomaly_ead, False),
    ("s7_anomaly_clip", s7_anomaly_clip, False),
    ("s8_depth", s8_depth, False),
    ("s9_report", s9_report, False),
]


def main():
    start_from = 0
    if len(sys.argv) > 1:
        start_from = int(sys.argv[1])

    print(f"\n{'='*60}")
    print(f"  UAP-FRAG-001 AI Analysis Pipeline v3.0")
    print(f"{'='*60}\n")

    total_start = time.time()
    results = {}

    for i, (name, module, critical) in enumerate(STAGES):
        if i < start_from:
            print(f"[SKIP] {name}")
            continue

        stage_start = time.time()
        try:
            result = module.run()
            elapsed = time.time() - stage_start
            print(f"  [{name}] Done in {elapsed:.1f}s\n")
            results[name] = result
        except Exception as e:
            elapsed = time.time() - stage_start
            print(f"  [{name}] FAILED after {elapsed:.1f}s: {e}\n")
            import traceback; traceback.print_exc()
            results[name] = {"error": str(e)}
            unload_model()  # force VRAM cleanup
            if critical:
                print(f"  CRITICAL stage failed, aborting pipeline.")
                break

    total_elapsed = time.time() - total_start
    print(f"\n{'='*60}")
    print(f"  Pipeline complete in {total_elapsed:.1f}s ({total_elapsed/60:.1f} min)")
    print(f"{'='*60}\n")

    # Summary
    for name, result in results.items():
        status = "ERROR" if result.get("error") else "OK"
        print(f"  [{status}] {name}")

    return results


if __name__ == "__main__":
    main()
