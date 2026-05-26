"""Overlay thin shoulder bar + hinge on goodmk60 (muzzle left). See SHOULDER-BAR-SPEC.md."""

from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "visuals/launcher/output/radr-bazooka-goodmk60.png"
OUT = ROOT / "visuals/launcher/output"


def overlay(img0: Image.Image) -> tuple[int, int, int, int, int, int]:
    w, h = img0.size
    hinge_x = int(w * 0.548)
    pad_bottom = int(h * 0.738)
    breech_x = int(w * 0.895)
    deploy_len = int(h * 0.095)
    return hinge_x, pad_bottom, breech_x, deploy_len, w, h


def main() -> None:
    img0 = Image.open(SRC).convert("RGBA")
    hinge_x, pad_bottom, breech_x, deploy_len, _, _ = overlay(img0)
    bar_w = 2
    hinge_r = 4
    bar_color = (22, 22, 24, 230)
    hinge_fill = (48, 48, 52, 255)
    hinge_outline = (18, 18, 20, 255)

    def hinge(draw: ImageDraw.ImageDraw, x: int, y: int) -> None:
        draw.ellipse(
            [x - hinge_r, y - hinge_r, x + hinge_r, y + hinge_r],
            fill=hinge_fill,
            outline=hinge_outline,
            width=1,
        )

    stowed = img0.copy()
    d = ImageDraw.Draw(stowed)
    hinge(d, hinge_x, pad_bottom)
    d.line([(hinge_x + 1, pad_bottom), (breech_x, pad_bottom)], fill=bar_color, width=bar_w)
    stowed.convert("RGB").save(OUT / "radr-bazooka-mk64-stowed.png", quality=95)

    deployed = img0.copy()
    d = ImageDraw.Draw(deployed)
    hinge(d, hinge_x, pad_bottom)
    d.line(
        [(hinge_x, pad_bottom), (hinge_x, pad_bottom + deploy_len)],
        fill=bar_color,
        width=bar_w,
    )
    deployed.convert("RGB").save(OUT / "radr-bazooka-mk64-deployed.png", quality=95)


if __name__ == "__main__":
    main()
