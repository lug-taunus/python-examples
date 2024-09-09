#!/usr/bin/env python3
import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup


def main():
    """Main function."""
    root_path = Path(".")
    response = requests.get(
        "https://commons.wikimedia.org/wiki/Commons:Picture_of_the_day"
    )
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    img_tags = soup.find_all(name="img", src=re.compile("\.jpg$"))
    images = [tag["src"] for tag in img_tags]
    for image in images:
        filename = image.split("/")[-1]
        path = root_path / filename
        print(f"- Downloading {filename}")
        download = requests.get(image)
        download.raise_for_status()
        path.write_bytes(download.content)


if __name__ == "__main__":
    main()
