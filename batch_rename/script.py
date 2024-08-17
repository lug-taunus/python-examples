#!/usr/bin/env python3
from pathlib import Path


def main():
    """Main function."""
    index = 1
    for file in Path(".").iterdir():
        if file.suffix.lower() == ".jpg":
            target = f"pict{index:03}_{file.stem}.jpg"
            print(f"{file} -> {target}")
            file.rename(target)
            index += 1


if __name__ == "__main__":
    # Execute the following lines only when this script is called directly.
    # When it is included from another script they are ignored.
    main()
