# Image Fetcher

## Task

Download all thumbnails from the Wikimedia Commons **Picture of the day** article.

## Details

You will need two external Python libraries:

- [requests](https://pypi.org/project/requests/) - HTTP library
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) - Web/Screen-scraping library

With those you can download a webpage from a URL and search for all `<img>` tags in the HTML content.
Then download all thumbnails referenced in the `src` attribute of the `<img>` tag and name the files according to the
image URLs last part.

## Prerequisites

- Change to the project directory `image_fetcher`
- Create a [virtual environment](https://docs.python.org/3/library/venv.html):

  ```shell
  python3 -m venv .venv
  ```

- Activate the virtual environment shell:

   ```shell
   . .venv/bin/activate
   ```

- Install requirements:

  ```shell
  pip install -r requirements.txt
  ```
