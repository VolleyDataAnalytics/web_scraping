# Web Scraping Tools Setup Guide

## Overview
This project sets up and configures three popular web scraping tools: **BeautifulSoup, Scrapy, and Selenium**. The objective is to ensure a seamless environment for extracting data from websites, including static and dynamic pages.

## 🚀 Project Goals
- Install and configure **BeautifulSoup, Scrapy, and Selenium**.
- Set up necessary dependencies like browser drivers for Selenium.
- Create and test simple scripts demonstrating each tool’s functionality.
- Provide a detailed setup guide for future reference.

---

## 📌 Environment Setup
Before starting, ensure you have **Python** installed. Then, set up a virtual environment:
```bash
python -m venv webscraping_env
source webscraping_env/bin/activate  # macOS/Linux
webscraping_env\Scripts\activate    # Windows
```

Next, install the required libraries:
```bash
pip install beautifulsoup4 scrapy selenium
```
For **Selenium**, also install the browser driver:
- **Chrome**: [Download ChromeDriver](https://sites.google.com/chromium.org/driver/)
- **Firefox**: [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)

Ensure the driver path is correctly set in your system.

---

## 🛠️ Tool Breakdown & Test Scripts

### 1️⃣ BeautifulSoup - Parsing Static HTML
**Purpose**: Extract data from simple HTML pages.

```python
from bs4 import BeautifulSoup
import requests

URL = "http://example.com"
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.title.text)  # Extract and print the title of the webpage
```

Run the script:
```bash
python beautifulsoup_test.py
```

---

### 2️⃣ Scrapy - Web Crawling & Data Extraction
**Purpose**: Scrape structured data from multiple pages efficiently.

#### Step 1: Create a Scrapy Project
```bash
scrapy startproject myproject
```

#### Step 2: Define an Item
Edit `items.py`:
```python
import scrapy
class QuoteItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
```

#### Step 3: Create a Spider
Create `quotes_spider.py` inside `spiders/`:
```python
import scrapy
from myproject.items import QuoteItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ['http://quotes.toscrape.com']

    def parse(self, response):
        for quote in response.css('div.quote'):
            item = QuoteItem()
            item['text'] = quote.css('span.text::text').get()
            item['author'] = quote.css('small.author::text').get()
            yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
```

#### Step 4: Run the Spider
```bash
scrapy crawl quotes -o quotes.json
```

---

### 3️⃣ Selenium - Interacting with Dynamic Content
**Purpose**: Extract data from JavaScript-rendered pages.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver (Ensure driver is installed)
driver = webdriver.Chrome()
driver.get("http://example.com")

print(driver.title)  # Print webpage title
driver.quit()
```

Run the script:
```bash
python selenium_test.py
```
