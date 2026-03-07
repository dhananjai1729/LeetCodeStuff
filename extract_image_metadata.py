"""
Extract metadata from an image file using Pillow and exifread.
Usage: python3 extract_image_metadata.py <image_path>
"""

import sys
import os
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
import exifread


def get_gps_info(exif_data: dict) -> dict:
    """Parse GPS info from EXIF data."""
    gps_info = {}
    raw_gps = exif_data.get("GPSInfo")
    if not raw_gps:
        return gps_info
    for key, val in raw_gps.items():
        tag_name = GPSTAGS.get(key, key)
        gps_info[tag_name] = val
    return gps_info


def extract_with_pillow(image_path: str) -> dict:
    """Extract basic image info and EXIF data using Pillow."""
    metadata = {}
    with Image.open(image_path) as img:
        metadata["filename"] = os.path.basename(image_path)
        metadata["format"] = img.format
        metadata["mode"] = img.mode
        metadata["width"], metadata["height"] = img.size
        metadata["file_size_bytes"] = os.path.getsize(image_path)

        exif_data = img._getexif()
        if exif_data:
            exif = {}
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                if tag == "GPSInfo":
                    exif["GPSInfo"] = get_gps_info(exif_data)
                else:
                    exif[tag] = value
            metadata["exif"] = exif
        else:
            metadata["exif"] = {}
    return metadata


def extract_with_exifread(image_path: str) -> dict:
    """Extract detailed EXIF tags using exifread."""
    tags = {}
    with open(image_path, "rb") as f:
        raw_tags = exifread.process_file(f, details=False)
        for tag, value in raw_tags.items():
            tags[tag] = str(value)
    return tags


def print_metadata(metadata: dict, exif_tags: dict) -> None:
    print("=" * 50)
    print("BASIC IMAGE INFO")
    print("=" * 50)
    for key in ("filename", "format", "mode", "width", "height", "file_size_bytes"):
        print(f"  {key:<20}: {metadata.get(key, 'N/A')}")

    exif = metadata.get("exif", {})
    if exif:
        print("\n" + "=" * 50)
        print("EXIF DATA (Pillow)")
        print("=" * 50)
        for tag, value in exif.items():
            if tag == "GPSInfo":
                print(f"  {'GPSInfo':<30}:")
                for k, v in value.items():
                    print(f"    {str(k):<28}: {v}")
            else:
                print(f"  {str(tag):<30}: {value}")

    if exif_tags:
        print("\n" + "=" * 50)
        print("EXIF TAGS (exifread)")
        print("=" * 50)
        for tag, value in sorted(exif_tags.items()):
            print(f"  {tag:<40}: {value}")
    else:
        print("\n  No additional EXIF tags found via exifread.")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_image_metadata.py <image_path>")
        sys.exit(1)

    image_path = sys.argv[1]
    if not os.path.isfile(image_path):
        print(f"Error: File not found: {image_path}")
        sys.exit(1)

    print(f"\nExtracting metadata from: {image_path}\n")

    metadata = extract_with_pillow(image_path)
    exif_tags = extract_with_exifread(image_path)
    print_metadata(metadata, exif_tags)


if __name__ == "__main__":
    main()
