#!/usr/bin/env python3
"""Generates simple SVG-based PNG icons for InvoiceSnap PWA"""
import subprocess, sys

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'Pillow', '--break-system-packages', '-q'])
    from PIL import Image, ImageDraw, ImageFont

def make_icon(size):
    img = Image.new('RGBA', (size, size), (10, 10, 15, 255))
    draw = ImageDraw.Draw(img)
    # gradient-ish background circle
    margin = size // 8
    draw.rounded_rectangle([margin, margin, size-margin, size-margin],
                            radius=size//5, fill=(108, 99, 255, 255))
    # white receipt emoji-like symbol
    inner = size // 3
    draw.rectangle([inner, inner, size-inner, size-inner], fill=(255,255,255,80))
    img.save(f'/home/claude/pwa/icon-{size}.png')
    print(f'✓ icon-{size}.png created')

make_icon(192)
make_icon(512)
