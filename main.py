from scraper import fetch_page


def main():
    url = "https://example.com"

    print(f"Fetching: {url}")

    html = fetch_page(url)

    print("Page fetched successfully.")
    print(f"Downloaded {len(html)} characters.")


if __name__ == "__main__":
    main()