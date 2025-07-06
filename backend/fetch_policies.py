# backend/fetch_policies.py

import requests
from bs4 import BeautifulSoup

def fetch_recent_bills():
    url = "https://prsindia.org/billtrack"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        bills = []

        # Find the section with latest bills
        bill_table = soup.find("table", class_="table")  # Adjust selector if needed
        if not bill_table:
            return []

        rows = bill_table.find_all("tr")[1:]  # Skip header

        for row in rows:
            cols = row.find_all("td")
            if len(cols) >= 2:
                link_tag = cols[0].find("a")
                title = link_tag.get_text(strip=True) if link_tag else "Untitled"
                link = "https://prsindia.org" + link_tag['href'] if link_tag else ""
                date = cols[1].get_text(strip=True)

                bills.append({
                    "title": title,
                    "link": link,
                    "date": date
                })

        return bills

    except Exception as e:
        print(f"❌ Error fetching bills: {str(e)}")
        return []
