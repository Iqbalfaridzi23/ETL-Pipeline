import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

def extract_products(pages=50):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        products = []

        for page in range(1, pages + 1):
            url = f"https://fashion-studio.dicoding.dev/?page={page}"
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')
            items = soup.select('.collection-card')
            print(f"Page {page} - Found {len(items)} products")

            for item in items:
                detail = item.select_one('.product-details')
                if not detail:
                    continue

                title_elem = item.select_one("h3.product-title")
                price_elem = item.select_one(".price")
                paragraphs = detail.select("p")

                title = title_elem.get_text(strip=True) if title_elem else ''
                price = price_elem.get_text(strip=True) if price_elem else ''
                rating, colors, size, gender = '', '', '', ''

                for p in paragraphs:
                    text = p.get_text(strip=True)
                    if text.startswith("Rating:"):
                        rating = text.replace("Rating:", "").replace("⭐", "").strip()
                    elif "Color" in text:
                        colors = text
                    elif "Size:" in text:
                        size = text
                    elif "Gender:" in text:
                        gender = text

                products.append({
                    'title': title,
                    'Price': price,
                    'Rating': rating,
                    'Colors': colors,
                    'Size': size,
                    'Gender': gender
                })

            if len(products) >= 1000:
                break

        df = pd.DataFrame(products[:1000])
        df['Timestamp'] = datetime.now().isoformat()
        return df

    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch page: {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"[ERROR] Unexpected error during extraction: {e}")
        return pd.DataFrame()
