import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except Exception:
    print("Pillow is required. Install with: python -m pip install pillow")
    sys.exit(1)

DEFAULT_EXTS = [".jpg", ".jpeg", ".png", ".webp", ".tif", ".tiff", ".bmp"]

FORMAT_ALIASES = {
    "jpg": "JPEG",
    "jpeg": "JPEG",
    "png": "PNG",
    "webp": "WEBP",
    "tif": "TIFF",
    "tiff": "TIFF",
    "bmp": "BMP",
}

EXT_FOR_FORMAT = {
    "JPEG": ".jpg",
    "PNG": ".png",
    "WEBP": ".webp",
    "TIFF": ".tif",
    "BMP": ".bmp",
}


def parse_exts(value):
    if not value:
        return DEFAULT_EXTS
    parts = [p.strip().lower() for p in value.split(",") if p.strip()]
    exts = []
    for p in parts:
        exts.append(p if p.startswith(".") else f".{p}")
    return exts


def iter_inputs(path, recursive, exts):
    p = Path(path)
    if p.is_file():
        return [p]
    if not p.is_dir():
        return []
    pattern = "**/*" if recursive else "*"
    files = [f for f in p.glob(pattern) if f.is_file() and f.suffix.lower() in exts]
    return files


def to_format(fmt_str):
    if not fmt_str:
        return None
    key = fmt_str.strip().lower()
    if key not in FORMAT_ALIASES:
        raise ValueError(f"Unsupported format: {fmt_str}")
    return FORMAT_ALIASES[key]


def png_compress_level(quality):
    q = max(1, min(95, int(quality)))
    return max(0, min(9, round((100 - q) / 10)))


def human_size(num):
    for unit in ["B", "KB", "MB", "GB"]:
        if num < 1024:
            return f"{num:.1f} {unit}"
        num /= 1024
    return f"{num:.1f} TB"


def build_output_path(src, out_dir, suffix, overwrite, out_ext):
    if overwrite:
        return src.with_suffix(out_ext)
    base = src.stem + suffix
    return Path(out_dir) / f"{base}{out_ext}"


def save_image(img, out_path, out_format, quality, keep_exif):
    save_kwargs = {}
    if keep_exif and "exif" in img.info:
        save_kwargs["exif"] = img.info["exif"]

    if out_format == "JPEG":
        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGB")
        save_kwargs.update({"quality": quality, "optimize": True, "progressive": True})
    elif out_format == "WEBP":
        save_kwargs.update({"quality": quality, "method": 6})
    elif out_format == "PNG":
        save_kwargs.update({"optimize": True, "compress_level": png_compress_level(quality)})

    img.save(out_path, format=out_format, **save_kwargs)


def main():
    parser = argparse.ArgumentParser(description="Compress images with Pillow")
    parser.add_argument("--input", required=True, help="File or folder path")
    parser.add_argument("--quality", type=int, default=70, help="1-95, higher means better quality")
    parser.add_argument("--format", default=None, help="Output format: jpg, png, webp, tif, bmp. Default keeps original")
    parser.add_argument("--output", default=None, help="Output directory. Default is input file's folder")
    parser.add_argument("--suffix", default="_compressed", help="Suffix for output filename")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite source (extension may change)")
    parser.add_argument("--recursive", action="store_true", help="Recurse into subfolders when input is a directory")
    parser.add_argument("--exts", default=None, help="Comma-separated extensions for directory input")
    parser.add_argument("--keep-exif", action="store_true", help="Preserve EXIF when possible")

    args = parser.parse_args()

    exts = parse_exts(args.exts)
    inputs = iter_inputs(args.input, args.recursive, exts)
    if not inputs:
        print("No input files found.")
        sys.exit(2)

    out_format = to_format(args.format) if args.format else None

    total_in = 0
    total_out = 0

    for src in inputs:
        out_dir = args.output or str(src.parent)
        out_dir_path = Path(out_dir)
        out_dir_path.mkdir(parents=True, exist_ok=True)

        with Image.open(src) as img:
            if out_format:
                fmt = out_format
                out_ext = EXT_FOR_FORMAT[fmt]
            else:
                fmt = img.format or FORMAT_ALIASES.get(src.suffix.lower().lstrip("."), None)
                if not fmt:
                    print(f"Skip (unknown format): {src}")
                    continue
                out_ext = src.suffix

            out_path = build_output_path(src, out_dir, args.suffix, args.overwrite, out_ext)
            save_image(img, out_path, fmt, args.quality, args.keep_exif)

        in_size = src.stat().st_size
        out_size = out_path.stat().st_size
        total_in += in_size
        total_out += out_size
        ratio = (out_size / in_size) if in_size else 0
        print(f"{src} -> {out_path} | {human_size(in_size)} -> {human_size(out_size)} ({ratio:.2f}x)")

    print(f"Total: {human_size(total_in)} -> {human_size(total_out)}")


if __name__ == "__main__":
    main()
