from bs4 import BeautifulSoup


def parse_page(html):
    """
    Parse HTML and extract basic webpage information.

    Args:
        html (str): Raw webpage HTML.

    Returns:
        dict: Structured webpage information.
    """
    soup = BeautifulSoup(html, "html.parser")

    title = soup.title.get_text(strip=True) if soup.title else None

    headings = [
        heading.get_text(strip=True)
        for heading in soup.find_all(["h1", "h2", "h3"])
    ]

    links = [
        link.get("href")
        for link in soup.find_all("a", href=True)
    ]

    return {
        "title": title,
        "headings": headings,
        "links": links,
    }