"""Light touch-up: black forward sleeve + shoulder bar only (grips excluded)."""

from __future__ import annotations

from pathlib import Path

import numpy as np
from PIL import Image, ImageEnhance, ImageFilter
from scipy.ndimage import gaussian_filter

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "visuals/launcher/output"

GRIP_ZONES = (
    (0.26, 0.40, 0.52, 0.88),
    (0.46, 0.60, 0.52, 0.88),
)


def _exclude_grips(mask: np.ndarray, w: int, h: int) -> np.ndarray:
    for x0, x1, y0, y1 in GRIP_ZONES:
        mask[int(h * y0) : int(h * y1), int(w * x0) : int(w * x1)] = False
    return mask


def build_mask(arr: np.ndarray, variant: str) -> np.ndarray:
    h, w, _ = arr.shape
    gray = arr.mean(axis=2)
    dark = gray < 95
    right = np.zeros((h, w), dtype=bool)
    right[:, int(w * 0.58) :] = True
    mask = dark & right
    mask = _exclude_grips(mask, w, h)

    if variant == "deployed":
        col = int(w * 0.68)
        x0, x1 = max(0, col - 12), min(w, col + 12)
        mask[int(h * 0.52) :, x0:x1] |= dark[int(h * 0.52) :, x0:x1]
    else:
        ys, ye = int(h * 0.56), int(h * 0.67)
        xs, xe = int(w * 0.58), int(w * 0.93)
        mask[ys:ye, xs:xe] |= dark[ys:ye, xs:xe]

    return _exclude_grips(mask, w, h)


def touchup(path: Path, variant: str) -> None:
    backup = path.with_name(path.stem + "-original.png")
    if not backup.exists():
        Image.open(path).convert("RGB").save(backup)

    src = Image.open(backup).convert("RGB")
    w, h = src.size
    arr = np.array(src, dtype=float)
    mask = build_mask(arr, variant)
    feather = gaussian_filter(mask.astype(float), 4.0)[..., None]

    smooth = src.filter(ImageFilter.SMOOTH_MORE).filter(ImageFilter.GaussianBlur(0.4))
    contrast = ImageEnhance.Contrast(src).enhance(1.06)
    proc = np.array(smooth, dtype=float) * 0.7 + np.array(contrast, dtype=float) * 0.3
    out = np.clip(arr * (1.0 - feather) + proc * feather, 0, 255).astype(np.uint8)
    Image.fromarray(out).save(path, quality=96)
    print(f"{path.name}: touched ~{mask.mean() * 100:.1f}% of pixels")


def main() -> None:
    touchup(OUT / "radr-bazooka-authoritative-stowed.png", "stowed")
    touchup(OUT / "radr-bazooka-authoritative-deployed.png", "deployed")


if __name__ == "__main__":
    main()
