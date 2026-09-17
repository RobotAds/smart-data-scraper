# Smart Data Scraper

A lightweight Python command-line tool for extracting, cleaning, and exporting structured data from public web pages.

## Overview

Smart Data Scraper retrieves a webpage, parses its HTML content, cleans the extracted data, and exports the results to both JSON and CSV.

The project uses a modular pipeline so that webpage retrieval, parsing, data cleaning, and exporting remain separate components.

## Features

- Fetch public webpages using HTTP requests
- Extract page titles, headings, and links
- Remove duplicate and unwanted data
- Export results to JSON
- Export results to CSV
- Accept target URLs from the command line
- Handle invalid URLs and failed requests gracefully

## How It Works

```text
URL
 |
 v
scraper.py
 |
 v
parser.py
 |
 v
cleaner.py
 |
 v
exporter.py
 |
 +----> JSON
 |
 +----> CSV
```

## Project Structure

```text
smart-data-scraper/
|
|-- main.py
|-- scraper.py
|-- parser.py
|-- cleaner.py
|-- exporter.py
|-- requirements.txt
|-- README.md
|
`-- data/
```

### Modules

**main.py**  
Coordinates the scraping pipeline and command-line interface.

**scraper.py**  
Retrieves HTML content from the requested webpage.

**parser.py**  
Parses HTML and extracts titles, headings, and links.

**cleaner.py**  
Removes empty values, duplicate entries, and unwanted links.

**exporter.py**  
Writes cleaned results to JSON and CSV files.

## Installation

Clone the repository:

```bash
git clone https://github.com/RobotAds/smart-data-scraper.git
cd smart-data-scraper
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the scraper and provide a public webpage URL:

```bash
python main.py https://example.com
```

Example output:

```text
Fetching: https://example.com
Page fetched successfully.
Downloaded 559 characters.

Extracted Data
--------------
Title: Example Domain
Headings: 1
Links: 1

Exported Files
--------------
JSON: data\results.json
CSV:  data\results.csv
```

Generated data files are stored in the `data` directory and excluded from version control.

## Built With

- Python
- Requests
- Beautiful Soup

## Project Status

Version 1 provides a working modular scraping pipeline with command-line input, structured data extraction, cleaning, export functionality, and request error handling.