import csv
import json
from pathlib import Path


def export_json(data, filename="data/results.json"):
    """
    Export scraped data to a JSON file.
    """
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    return path


def export_csv(data, filename="data/results.csv"):
    """
    Export scraped links to a CSV file.
    """
    path = Path(filename)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["title", "link"])

        for link in data["links"]:
            writer.writerow([data["title"], link])

    return path