# import asyncio
# from playwright.async_api import async_playwright
# import json
# import re
# from datetime import datetime

# async def scrape_airbnb(location: str, guests: int, max_price: int, check_in: str, check_out: str, limit: int = 5):
#     listings = []

#     search_url = (
#         f"https://www.airbnb.com/s/{location}/homes"
#         f"?adults={guests}&price_max={max_price}"
#         f"&check_in={check_in}&check_out={check_out}"
#     )

#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
#         context = await browser.new_context()
#         page = await context.new_page()

#         await page.goto(search_url, timeout=60000)
#         await page.wait_for_timeout(8000)  # Wait for initial load

#         # Scroll a bit to trigger lazy loading
#         await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#         await page.wait_for_timeout(3000)

#         cards = await page.query_selector_all("div[itemprop='itemListElement']")
#         cards = cards[:limit]

#         for card in cards:
#             try:
#                 # Title
#                 title_el = await card.query_selector("div[data-testid='listing-card-title']")
#                 title = (await title_el.inner_text()).strip() if title_el else "N/A"

#                 subtitle = "N/A"
#                 try:
#                     full_text = await card.inner_text()
#                     lines = [line.strip() for line in full_text.split("\n") if line.strip()]
#                     if title in lines:
#                         title_index = lines.index(title)
#                         if title_index + 1 < len(lines):
#                             subtitle = lines[title_index + 1]
#                 except:
#                     pass

#                 # Price
#                 price = "N/A"
#                 price_elements = await card.query_selector_all("span:has-text('$')")
#                 if price_elements:
#                     price_text = await price_elements[-1].inner_text()
#                     price = price_text.strip().replace('\n', ' ')

#                 # Link
#                 link_element = await card.query_selector("a")
#                 relative_link = await link_element.get_attribute("href") if link_element else None
#                 url = f"https://www.airbnb.com{relative_link}" if relative_link else "N/A"

#                 # Area
#                 area = "Unknown"
#                 area_el = await card.query_selector("div:has-text(' in ')")
#                 if area_el:
#                     area_text = await area_el.inner_text()
#                     if " in " in area_text:
#                         area = area_text.split(" in ")[-1].split("\n")[0].strip()

#                 # Rating and Reviews
#                 rating = "N/A"
#                 reviews = "N/A"
#                 rating_el = await card.query_selector("span:has-text('('):has-text(')')")
#                 if rating_el:
#                     rating_text = await rating_el.inner_text()
#                     match = re.match(r"(\d+\.\d+)\s*\((\d+)\)", rating_text)
#                     if match:
#                         rating, reviews = match.groups()
#                     else:
#                         rating_only = re.search(r"\d+\.\d+", rating_text)
#                         review_count = re.search(r"\((\d+)\)", rating_text)
#                         if rating_only:
#                             rating = rating_only.group()
#                         if review_count:
#                             reviews = review_count.group(1)

#                 listings.append({
#                     "title": title,
#                     "subtitle": subtitle,
#                     "price": price,
#                     "url": url,
#                     "location": location,
#                     "area": area,
#                     "rating": rating,
#                     "reviews": reviews,
#                     "check_in": check_in,
#                     "check_out": check_out,
#                     "nights": (datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")).days
#                 })
#             except Exception as e:
#                 print(f"Error parsing listing: {e}")

#         await browser.close()
#         return listings


# async def main():
#     location = "Pakistan"
#     guests = 5
#     max_price = 1500
#     check_in = "2025-09-15"
#     check_out = "2025-09-20"
#     limit = 10

#     print("Fetching listings...")
#     data = await scrape_airbnb(location, guests, max_price, check_in, check_out, limit)
#     print(json.dumps(data, indent=4, ensure_ascii=False))


# # Run it
# if __name__ == "__main__":
#     asyncio.run(main())



# import asyncio
# from playwright.async_api import async_playwright
# import json
# import re
# from datetime import datetime

# async def scrape_airbnb(location: str, guests: int, max_price: int, check_in: str, check_out: str, limit: int = 20):
#     listings = []

#     search_url = (
#         f"https://www.airbnb.com/s/{location}/homes"
#         f"?adults={guests}&price_max={max_price}"
#         f"&check_in={check_in}&check_out={check_out}"
#     )

#     async with async_playwright() as p:
#         browser = await p.chromium.launch(headless=True)
#         context = await browser.new_context()
#         page = await context.new_page()

#         await page.goto(search_url, timeout=60000)
#         await page.wait_for_timeout(5000)

#         while len(listings) < limit:
#             await page.wait_for_timeout(2000)

#             cards = await page.query_selector_all("div[itemprop='itemListElement']")

#             for card in cards:
#                 if len(listings) >= limit:
#                     break
#                 try:
#                     # Title
#                     title_el = await card.query_selector("div[data-testid='listing-card-title']")
#                     title = (await title_el.inner_text()).strip() if title_el else "N/A"

#                     subtitle = "N/A"
#                     try:
#                         full_text = await card.inner_text()
#                         lines = [line.strip() for line in full_text.split("\n") if line.strip()]
#                         if title in lines:
#                             title_index = lines.index(title)
#                             if title_index + 1 < len(lines):
#                                 subtitle = lines[title_index + 1]
#                     except:
#                         pass

#                     # Price
#                     price = "N/A"
#                     price_elements = await card.query_selector_all("span:has-text('$')")
#                     if price_elements:
#                         price_text = await price_elements[-1].inner_text()
#                         price = price_text.strip().replace('\n', ' ')

#                     # Link
#                     link_element = await card.query_selector("a")
#                     relative_link = await link_element.get_attribute("href") if link_element else None
#                     url = f"https://www.airbnb.com{relative_link}" if relative_link else "N/A"

#                     # Area
#                     area = "Unknown"
#                     area_el = await card.query_selector("div:has-text(' in ')")
#                     if area_el:
#                         area_text = await area_el.inner_text()
#                         if " in " in area_text:
#                             area = area_text.split(" in ")[-1].split("\n")[0].strip()

#                     # Rating and Reviews
#                     rating = "N/A"
#                     reviews = "N/A"
#                     rating_el = await card.query_selector("span:has-text('('):has-text(')')")
#                     if rating_el:
#                         rating_text = await rating_el.inner_text()
#                         match = re.match(r"(\d+\.\d+)\s*\((\d+)\)", rating_text)
#                         if match:
#                             rating, reviews = match.groups()
#                         else:
#                             rating_only = re.search(r"\d+\.\d+", rating_text)
#                             review_count = re.search(r"\((\d+)\)", rating_text)
#                             if rating_only:
#                                 rating = rating_only.group()
#                             if review_count:
#                                 reviews = review_count.group(1)

#                     listings.append({
#                         "title": title,
#                         "subtitle": subtitle,
#                         "price": price,
#                         "url": url,
#                         "location": location,
#                         "area": area,
#                         "rating": rating,
#                         "reviews": reviews,
#                         "check_in": check_in,
#                         "check_out": check_out,
#                         "nights": (datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")).days
#                     })
#                 except Exception as e:
#                     print(f"Error parsing listing: {e}")

#             # Try to click next page if needed
#             if len(listings) < limit:
#                 next_btn = await page.query_selector("a[aria-label='Next']")  # Airbnb pagination next button
#                 if next_btn:
#                     await next_btn.click()
#                     await page.wait_for_timeout(5000)
#                 else:
#                     break  # No more pages

#         await browser.close()
#         return listings

# async def main():
#     location = "Pakistan"
#     guests = 5
#     max_price = 1500
#     check_in = "2025-09-15"
#     check_out = "2025-09-20"
#     limit = 36

#     print("Fetching listings...")
#     data = await scrape_airbnb(location, guests, max_price, check_in, check_out, limit)
#     print(json.dumps(data, indent=4, ensure_ascii=False))

# if __name__ == "__main__":
#     asyncio.run(main())

############################################updatecode#################################################################

import asyncio
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError
import json
import re
from datetime import datetime

async def scrape_airbnb(location: str, guests: int, max_price: int, check_in: str, check_out: str, limit: int = 20):
    listings = []

    search_url = (
        f"https://www.airbnb.com/s/{location}/homes"
        f"?adults={guests}&price_max={max_price}"
        f"&check_in={check_in}&check_out={check_out}"
    )

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        print(f"Navigating to {search_url}")
        await page.goto(search_url, timeout=60000)

        # Wait for listing cards to load
        await page.wait_for_selector("div[itemprop='itemListElement']", timeout=15000)

        while len(listings) < limit:
            try:
                await page.wait_for_selector("div[itemprop='itemListElement']", timeout=10000)
                cards = await page.query_selector_all("div[itemprop='itemListElement']")

                for card in cards:
                    if len(listings) >= limit:
                        break

                    try:
                        title_el = await card.query_selector("div[data-testid='listing-card-title']")
                        title = (await title_el.inner_text()).strip() if title_el else "N/A"

                        subtitle = "N/A"
                        full_text = await card.inner_text()
                        lines = [line.strip() for line in full_text.split("\n") if line.strip()]
                        if title in lines:
                            idx = lines.index(title)
                            if idx + 1 < len(lines):
                                subtitle = lines[idx + 1]

                        price = "N/A"
                        price_elements = await card.query_selector_all("span:has-text('$')")
                        if price_elements:
                            price = (await price_elements[-1].inner_text()).strip().replace('\n', ' ')

                        link_element = await card.query_selector("a")
                        relative_link = await link_element.get_attribute("href") if link_element else None
                        url = f"https://www.airbnb.com{relative_link}" if relative_link else "N/A"

                        area = "Unknown"
                        area_el = await card.query_selector("div:has-text(' in ')")
                        if area_el:
                            area_text = await area_el.inner_text()
                            if " in " in area_text:
                                area = area_text.split(" in ")[-1].split("\n")[0].strip()

                        rating = "N/A"
                        reviews = "N/A"
                        rating_el = await card.query_selector("span:has-text('('):has-text(')')")
                        if rating_el:
                            rating_text = await rating_el.inner_text()
                            match = re.match(r"(\d+\.\d+)\s*\((\d+)\)", rating_text)
                            if match:
                                rating, reviews = match.groups()
                            else:
                                rating_only = re.search(r"\d+\.\d+", rating_text)
                                review_count = re.search(r"\((\d+)\)", rating_text)
                                if rating_only:
                                    rating = rating_only.group()
                                if review_count:
                                    reviews = review_count.group(1)

                        listings.append({
                            "title": title,
                            "subtitle": subtitle,
                            "price": price,
                            "url": url,
                            "location": location,
                            "area": area,
                            "rating": rating,
                            "reviews": reviews,
                            "check_in": check_in,
                            "check_out": check_out,
                            "nights": (datetime.strptime(check_out, "%Y-%m-%d") - datetime.strptime(check_in, "%Y-%m-%d")).days
                        })

                    except Exception as e:
                        print(f"Error parsing listing: {e}")

                # Try to click next page if needed
                if len(listings) < limit:
                    next_btn = await page.query_selector("a[aria-label='Next']")
                    if next_btn:
                        try:
                            await next_btn.scroll_into_view_if_needed()
                            await next_btn.click(force=True)
                            await page.wait_for_selector("div[itemprop='itemListElement']", timeout=10000)
                        except PlaywrightTimeoutError as e:
                            print("Timeout while clicking next page. Exiting.")
                            break
                    else:
                        print("No more pages.")
                        break

            except Exception as e:
                print(f"Error while scraping page: {e}")
                break

        await browser.close()
        return listings


async def main():
    location = "United States"
    guests = 5
    max_price = 1500
    check_in = "2025-09-15"
    check_out = "2025-09-20"
    limit = 36

    print("Fetching listings...")
    data = await scrape_airbnb(location, guests, max_price, check_in, check_out, limit)
    print(json.dumps(data, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    asyncio.run(main())

