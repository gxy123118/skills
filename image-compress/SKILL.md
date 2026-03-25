---
name: image-compress
description: Compress and re-encode images with a specified quality value using Python and Pillow. Use when asked to reduce image size, batch-compress folders, or change output format while keeping the original format by default.
---

# Image Compress

## Overview

Compress images by re-encoding at a chosen quality. Default keeps the original format and writes a new file with a `_compressed` suffix. Use `scripts/compress_image.py`.

## Quick Start

- Install Pillow: `python -m pip install pillow`
- Single file, keep format: `python scripts/compress_image.py --input "C:\path\photo.jpg" --quality 70`
- Change format: `python scripts/compress_image.py --input "C:\path\photo.png" --quality 80 --format webp`
- Batch folder: `python scripts/compress_image.py --input "C:\path\photos" --recursive --exts jpg,png --quality 75`

## Workflow

1. Confirm input type (file or folder) and desired output location.
2. Choose quality value (1-95). Default 70.
3. Decide output format (keep original unless user specifies).
4. Decide output naming: default `_compressed` suffix or `--overwrite` to replace.
5. Run script and report before/after sizes.

## Script: scripts/compress_image.py

Options:
- `--input` file or folder path
- `--quality` 1-95
- `--format` `jpg|png|webp|tif|bmp` (optional)
- `--output` output directory (optional)
- `--suffix` output suffix (default `_compressed`)
- `--overwrite` overwrite original (extension may change)
- `--recursive` recurse subfolders for folder input
- `--exts` comma-separated extensions for folder input
- `--keep-exif` preserve EXIF when possible

Notes:
- JPEG/WebP use `quality`. PNG uses `compress_level` derived from the quality value.
- JPEG output converts RGBA or palette images to RGB.

## Troubleshooting

- If Pillow is missing, install with `python -m pip install pillow`.
- For offline install, use a local `.whl` for your Python version.
