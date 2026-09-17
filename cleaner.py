def clean_text_items(items):
    """
    Clean and deduplicate text items while preserving order.

    Args:
        items (list): Text values to clean.

    Returns:
        list: Cleaned, unique text values.
    """
    cleaned = []

    for item in items:
        if not item:
            continue

        item = item.strip()

        if item and item not in cleaned:
            cleaned.append(item)

    return cleaned


def clean_links(links):
    """
    Remove empty, duplicate, and fragment-only links.

    Args:
        links (list): Extracted webpage links.

    Returns:
        list: Cleaned, unique links.
    """
    cleaned = []

    for link in links:
        if not link:
            continue

        link = link.strip()

        if not link or link.startswith("#"):
            continue

        if link not in cleaned:
            cleaned.append(link)

    return cleaned