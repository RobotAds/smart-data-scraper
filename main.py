import sys

import requests

from scraper import fetch_page
from parser import parse_page
from cleaner import clean_links, clean_text_items
from exporter import export_csv, export_json


def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    print(f"Fetching: {url}")

    # Fetch webpage
    try:
        html = fetch_page(url)
    except requests.RequestException as error:
        print("\nError: Unable to fetch the webpage.")
        print(f"Reason: {error}")
        print("Please check the URL and try again.")
        sys.exit(1)

    # Parse webpage
    data = parse_page(html)

    # Clean extracted data
    data["headings"] = clean_text_items(data["headings"])
    data["links"] = clean_links(data["links"])

    # Export cleaned data
    json_path = export_json(data)
    csv_path = export_csv(data)

    # Display scrape results
    print("Page fetched successfully.")
    print(f"Downloaded {len(html)} characters.")

    print("\nExtracted Data")
    print("--------------")
    print(f"Title: {data['title']}")
    print(f"Headings: {len(data['headings'])}")
    print(f"Links: {len(data['links'])}")

    for link in data["links"]:
        print(f"  - {link}")

    # Display export locations
    print("\nExported Files")
    print("--------------")
    print(f"JSON: {json_path}")
    print(f"CSV:  {csv_path}")


if __name__ == "__main__":
    main()