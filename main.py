from scraper import fetch_page
from parser import parse_page


def main():
    url = "https://example.com"

    print(f"Fetching: {url}")

    html = fetch_page(url)
    data = parse_page(html)

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