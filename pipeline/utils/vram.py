import gc
import torch


def get_free_vram_mb() -> float:
    if not torch.cuda.is_available():
        return 0.0
    free, _ = torch.cuda.mem_get_info()
    return free / (1024 * 1024)


def unload_model(*models):
    for m in models:
        if m is not None:
            del m
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def get_device() -> torch.device:
    return torch.device("cuda" if torch.cuda.is_available() else "cpu")


def log_vram(label: str = ""):
    if torch.cuda.is_available():
        free = get_free_vram_mb()
        total = torch.cuda.get_device_properties(0).total_memory / (1024 * 1024)
        used = total - free
        print(f"  [VRAM] {label}: {used:.0f}/{total:.0f} MB (free: {free:.0f} MB)")
