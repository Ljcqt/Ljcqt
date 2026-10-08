import requests
from bs4 import BeautifulSoup
import json
import os

USERNAME = "Ljcqt"

def fetch_contributions():
    url = f"https://github.com/users/{USERNAME}/contributions"
    print(f"Récupération des données depuis {url}...")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Erreur HTTP {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    days = []
    for day in soup.find_all('td', class_='ContributionCalendar-day'):
        date = day.get('data-date')
        count = day.get('data-count')
        level = day.get('data-level')
        if date:
            days.append({
                "date": date,
                "count": int(count) if count else 0,
                "level": int(level) if level else 0
            })

    os.makedirs("data", exist_ok=True)
    with open("data/contributions.json", "w", encoding="utf-8") as f:
        json.dump(days, f, indent=2)
    print(f"Succès ! {len(days)} jours de contributions enregistrés dans data/contributions.json")

if __name__ == "__main__":
    fetch_contributions()