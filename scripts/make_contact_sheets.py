#!/usr/bin/env python3
"""Create four-page contact sheets for complete reading-edition visual review."""

from __future__ import annotations

import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    pages = sorted(args.source.glob("page-*.png"), key=lambda p: int(p.stem.split("-")[-1]))
    if not pages:
        raise SystemExit("No rendered pages found.")
    font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Arial Bold.ttf", 22)
    scale, gap, label_h = 0.62, 34, 38
    for old in args.output.glob("pages_*.png"):
        old.unlink()
    for start in range(0, len(pages), 4):
        batch = pages[start:start + 4]
        opened = [Image.open(path).convert("RGB") for path in batch]
        thumb_w, thumb_h = int(opened[0].width * scale), int(opened[0].height * scale)
        sheet = Image.new("RGB", (gap * 3 + thumb_w * 2, gap * 3 + (thumb_h + label_h) * 2), "#D8DDE3")
        draw = ImageDraw.Draw(sheet)
        for index, (path, page) in enumerate(zip(batch, opened)):
            row, col = divmod(index, 2)
            x, y = gap + col * (thumb_w + gap), gap + row * (thumb_h + label_h + gap)
            sheet.paste(page.resize((thumb_w, thumb_h), Image.Resampling.LANCZOS), (x, y + label_h))
            draw.text((x, y + 4), f"Page {int(path.stem.split('-')[-1])}", font=font, fill="#172B3A")
        first, last = int(batch[0].stem.split("-")[-1]), int(batch[-1].stem.split("-")[-1])
        sheet.save(args.output / f"pages_{first:03d}_{last:03d}.png")
    print(f"Created {len(list(args.output.glob('pages_*.png')))} contact sheets for {len(pages)} pages.")


if __name__ == "__main__":
    main()
