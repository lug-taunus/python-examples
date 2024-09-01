#!/usr/bin/env python3
from pathlib import Path


def main():
    """Main function."""
    root_path = Path(".")
    files = sorted(root_path.glob("*.[jJ][pP][gG]"))
    for index, file in enumerate(files, 1):
        target = f"pict{index:03}_{file.stem}.jpg"
        print(f"{file} -> {target}")
        file.rename(target)


if __name__ == "__main__":
    # Execute the following lines only when this script is called directly.
    # When it is included from another script they are ignored.
    main()
