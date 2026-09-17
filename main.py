from scraper import fetch_page
from parser import parse_page
from cleaner import clean_links, clean_text_items


def main():
    url = "https://example.com"

    print(f"Fetching: {url}")

    html = fetch_page(url)
    data = parse_page(html)

    data["headings"] = clean_text_items(data["headings"])
    data["links"] = clean_links(data["links"])

    print("Page fetched successfully.")
    print(f"Downloaded {len(html)} characters.")

    print("\nExtracted Data")
    print("--------------")
    print(f"Title: {data['title']}")
    print(f"Headings: {len(data['headings'])}")
    print(f"Links: {len(data['links'])}")

    for link in data["links"]:
        print(f"  - {link}")


if __name__ == "__main__":
    main()