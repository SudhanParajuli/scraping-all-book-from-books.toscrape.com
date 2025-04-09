# Book Scraper

A simple web scraping script that extracts book data from [Books to Scrape](http://books.toscrape.com/), a website that provides a demo of catalog-style content for scraping practice. This script collects various book details, including the title, description, category, availability, rating, price, and more, and saves the results into an Excel file.

## Features

- Scrapes multiple pages of books data.
- Extracts details such as:
  - Title
  - Description
  - Category
  - Availability
  - Rating
  - Price
  - UPC (Universal Product Code)
  - Image URL
- Saves the extracted data to an Excel file (`books.xlsx`).
- Uses `requests` to fetch page content, `BeautifulSoup` to parse HTML, and `pandas` to save the data.

## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pandas` library
- `lxml` parser for BeautifulSoup (optional but recommended)

To install the required libraries, run:

```bash
pip install requests beautifulsoup4 pandas lxml
