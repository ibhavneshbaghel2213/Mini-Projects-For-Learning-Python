# Wikipedia Data Scraping Automation

This Python script automates the process of scraping data from Wikipedia and organizes it into a structured JSON format. The script utilizes the BeautifulSoup (`bs4`) library for parsing HTML and the Selenium library for web automation.

## Features

- **Data Scraping:** The script extracts information from Wikipedia pages.
- **Structured JSON Output:** The scraped data is organized into specific JSON keys for easy analysis and usage.

## How to use :

- In line **107** put the URL of your Wikipedia page.
- Copy the XPATH which selects all the links present in the table on the Wikipedia page.
- paste your XPath in line **111** in links variable.
- Now run The script and get structured data.

## Prerequisites

Before running the script, make sure to install the required libraries:

```bash
pip install beautifulsoup4 selenium
