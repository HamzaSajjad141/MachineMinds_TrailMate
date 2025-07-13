from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
from urllib.parse import quote
from datetime import datetime, timedelta
import json

def scrape_booking(city, checkin, guests, max_price, days, limit):
    results = []

    # Calculate checkout
    checkin_date = datetime.strptime(checkin, "%Y-%m-%d")
    checkout_date = checkin_date + timedelta(days=days)
    checkin_str = checkin_date.strftime("%Y-%m-%d")
    checkout_str = checkout_date.strftime("%Y-%m-%d")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  
        page = browser.new_page(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            viewport={"width": 1280, "height": 800}
        )

        encoded_city = quote(city)
        url = f"https://www.booking.com/searchresults.html?ss={encoded_city}&checkin_year_month_monthday={checkin_str}&checkout_year_month_monthday={checkout_str}&group_adults={guests}"
        if 1 <= max_price <= 5:
            url += f"&nflt=price%3D{max_price}"

        page.goto(url, wait_until="networkidle", timeout=60000)

        # Accept cookie if present
        try:
            page.locator('button:has-text("Accept")').first.click(timeout=5000)
        except:
            pass

        # Scroll and wait for JS-rendered listings
        page.wait_for_timeout(5000)
        page.evaluate("window.scrollBy(0, 3000)")
        page.wait_for_timeout(5000)


        html = page.content()
        soup = BeautifulSoup(html, "html.parser")
        hotels = soup.select('div[data-testid="property-card"]')


        for i, hotel in enumerate(hotels):
            if i >= limit:
                break

            name = hotel.select_one('div[data-testid="title"]')
            name = name.get_text(strip=True) if name else "N/A"

            location = hotel.select_one('span[data-testid="address"]')
            location = location.get_text(strip=True) if location else "N/A"

            # ✅ Price — fallback-safe
            # price_tag = hotel.select_one('span[data-testid="price-and-discounted-price"]') or \
            # hotel.select_one('span[data-testid="price"]') or \
            # hotel.select_one('div[data-testid*="price"] span')

            # if price_tag:
            #     price = price_tag.get_text(strip=True)
            # else:
            #  # Fallback: Look for span with currency and digits
            #     price = "N/A"
            #     for span in hotel.find_all("span"):
            #         span_text = span.get_text(strip=True)
            #         if any(sym in span_text for sym in ["PKR", "Rs", "$", "€"]) and any(c.isdigit() for c in span_text):
            #             price = span_text
            #             break


            # price = hotel.select_one('span[data-testid="price-and-discounted-price"]').get_text(strip=True) if hotel.select_one('span[data-testid="price-and-discounted-price"]') else "N/A"


            image_tag = hotel.select_one('img')
            image_url = image_tag['src'] if image_tag and image_tag.has_attr('src') else "N/A"

            rating = hotel.select_one('div[data-testid="review-score"]').get_text(strip=True) if hotel.select_one('div[data-testid="review-score"]') else "N/A"

            results.append({
                "name": name,
                "location": location,
                # "price": price,
                "image_url": image_url,
                "rating": rating,
                "check_in": checkin_str,
                "check_out": checkout_str,
                "days": days
            })

        browser.close()

    print(json.dumps(results, indent=4, ensure_ascii=False))


# Example usage
scrape_booking(city="Islamabad", checkin="2025-08-01", guests=2, max_price=1500, days=3, limit=10)


