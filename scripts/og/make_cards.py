# /// script
# requires-python = ">=3.11"
# dependencies = ["pillow==11.3.0", "pyyaml==6.0.2"]
# ///
"""Generate 1200x630 social preview cards for johndschultz.com.

One card per essay, thought and concept (keyed by section + content base
name, the same key layouts/partials/og-image.html computes), plus one default
card for every other page. Output goes to static/images/og/ (git-ignored);
the deploy workflow runs this before `hugo`.

Run locally:  uv run --script scripts/og/make_cards.py
Exits non-zero if a title can't fit, so a bad card fails the deploy instead
of shipping text drawn over the footer.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml
from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[2]
FONTS = Path(__file__).resolve().parent / "fonts"
SERIF = str(FONTS / "Newsreader-SemiBold.ttf")
MONO = str(FONTS / "JetBrainsMono-Regular.ttf")
MONO_B = str(FONTS / "JetBrainsMono-Bold.ttf")
AVATAR = ROOT / "static/images/john-schultz-avatar-800.jpg"
OUT = ROOT / "static/images/og"
SECTIONS = {"essays": "Essay", "thoughts": "Thought", "concepts": "Concept"}

# Palette: Grafe navy (approved 2026-11-19). Contrast vs BG, WCAG:
# TITLE 12.7:1, LABEL 7.4:1, SUB 10.2:1 (all AAA).
BG, BAR, RING = "#0E3552", "#378CC9", "#378CC9"
TITLE, LABEL, SUB, RULE = "#FFFFFF", "#9FCBEA", "#D9E8F3", "#2E5878"

W, H, M = 1200, 630, 80
PHOTO = 280
TITLE_TOP, TITLE_H = 130, 330
MAX_SIZE, MIN_SIZE, MAX_LINES = 84, 44, 4


class TitleTooLong(Exception):
    pass


def avatar(size: int) -> Image.Image:
    im = Image.open(AVATAR).convert("RGB")
    im = ImageOps.fit(im, (size, size), centering=(0.5, 0.35))
    mask = Image.new("L", (size * 4, size * 4), 0)
    ImageDraw.Draw(mask).ellipse((0, 0, size * 4, size * 4), fill=255)
    im.putalpha(mask.resize((size, size), Image.LANCZOS))
    return im


def wrap(d: ImageDraw.ImageDraw, text: str, font, maxw: int) -> list[str]:
    lines: list[str] = []
    cur = ""
    for word in text.split():
        trial = f"{cur} {word}".strip()
        if d.textlength(trial, font=font) <= maxw or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
    lines.append(cur)
    return lines


def fit_title(d: ImageDraw.ImageDraw, text: str, maxw: int):
    for size in range(MAX_SIZE, MIN_SIZE - 1, -2):
        font = ImageFont.truetype(SERIF, size)
        lines = wrap(d, text, font, maxw)
        lh = int(size * 1.15)
        widest = max(d.textlength(ln, font=font) for ln in lines)
        if len(lines) <= MAX_LINES and len(lines) * lh <= TITLE_H and widest <= maxw:
            return font, lines, lh
    raise TitleTooLong(text)


def card(label: str, title: str, footer_left: str, out: Path, avatar_img: Image.Image) -> None:
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    d.rectangle((0, 0, W, 14), fill=BAR)
    px = W - M - PHOTO
    d.text((M, 70), label.upper(), font=ImageFont.truetype(MONO_B, 26), fill=LABEL)
    font, lines, lh = fit_title(d, title, px - M - 50)
    y = TITLE_TOP + (TITLE_H - len(lines) * lh) // 2
    for ln in lines:
        d.text((M, y), ln, font=font, fill=TITLE)
        y += lh
    py = 70 + (430 - PHOTO) // 2
    d.ellipse((px - 8, py - 8, px + PHOTO + 8, py + PHOTO + 8), fill=RING)
    im.paste(avatar_img, (px, py), avatar_img)
    d.line((M, 500, W - M, 500), fill=RULE, width=2)
    d.text((M, 528), footer_left, font=ImageFont.truetype(SERIF, 40), fill=TITLE)
    dom = "johndschultz.com"
    fm = ImageFont.truetype(MONO, 26)
    d.text((W - M - d.textlength(dom, font=fm), 541), dom, font=fm, fill=SUB)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, "JPEG", quality=90, optimize=True)


def front_matter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    _, fm, _ = text.split("---", 2)
    return yaml.safe_load(fm) or {}


def content_base_name(path: Path) -> str:
    # Mirrors Hugo's .File.ContentBaseName: bundle dir name for index.md.
    return path.parent.name if path.name == "index.md" else path.stem


def main() -> int:
    av = avatar(PHOTO)
    made, failed = 0, []
    for section, label in SECTIONS.items():
        for path in sorted((ROOT / "content" / section).rglob("*.md")):
            if path.name == "_index.md":
                continue
            title = str(front_matter(path).get("title") or "").strip()
            if not title:
                failed.append(f"{path}: no title")
                continue
            out = OUT / section / f"{content_base_name(path)}.jpg"
            try:
                card(label, title, "John Schultz", out, av)
                made += 1
            except TitleTooLong:
                failed.append(f"{path}: title too long to fit: {title!r}")
    card("Essays and ideas", "John Schultz", "Auctions, technology and leadership", OUT / "default.jpg", av)
    print(f"og cards: {made} posts + default -> {OUT.relative_to(ROOT)}")
    for f in failed:
        print(f"ERROR {f}", file=sys.stderr)
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
