import requests


def fetch_page(url):
    """
    Fetch the HTML content of a public webpage.

    Args:
        url (str): The webpage URL to request.

    Returns:
        str: The webpage HTML.

    Raises:
        requests.RequestException: If the request fails.
    """
    headers = {
        "User-Agent": "SmartDataScraper/1.0"
    }

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    response.raise_for_status()

    return response.text