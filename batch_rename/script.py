#!/usr/bin/env python3
from pathlib import Path


def main():
    """Main function."""
    root_path = Path(".")
    for index, file in enumerate(root_path.iterdir(), 1):
        if file.suffix.lower() == ".jpg":
            target = f"pict{index:03}_{file.stem}.jpg"
            print(f"{file} -> {target}")
            file.rename(target)


if __name__ == "__main__":
    # Execute the following lines only when this script is called directly.
    # When it is included from another script they are ignored.
    main()
