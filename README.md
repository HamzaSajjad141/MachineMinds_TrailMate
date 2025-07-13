# 🏨 Booking.com Scraper (Playwright + BeautifulSoup)

This project is a Python-based web scraper that extracts hotel accommodation data from [Booking.com](https://www.booking.com) using **Playwright** and **BeautifulSoup**. It allows you to search by city, check-in date, number of guests, price range, and duration of stay.

---

## 🚀 Features

- Extracts hotel listings based on user-defined input
- Headless browsing (no browser window pops up)
- Captures:
  - **Hotel name**
  - **Location**
  - **Rating**
  - **Image URL**
  - **Check-in / Check-out dates**
  - **Stay duration**
- Results are printed in clean **JSON format**

---

## 📦 Requirements

- Python 3.7+
- [Playwright](https://playwright.dev/python/)
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/)

### Install Dependencies

pip install playwright beautifulsoup4
playwright install

## How It Works
- Launches a headless Chromium browser using Playwright

- Loads the Booking.com search results page with your filters

- Waits for JavaScript content to load

- Parses hotel listings using BeautifulSoup

- Extracts selected fields from the HTML

- Displays results as formatted JSON in the terminal

## 📝 Usage
Update and run the following example in scraper.py:

scrape_booking<br>
(<br>
    &nbsp;&nbsp;city="Islamabad",<br>
    &nbsp;&nbsp;checkin="2025-08-01",<br>
    &nbsp;&nbsp;guests=2,<br>
    &nbsp;&nbsp;max_price=1500,<br>
    &nbsp;&nbsp;days=3,<br>
    &nbsp;&nbsp;limit=10<br>
)<br>


## 📤 Output Example

[<br>
    &nbsp;{<br>
        &nbsp;&nbsp;"name": "Serena Hotel",<br>
        &nbsp;&nbsp;"location": "Khayaban-e-Suharwardy, Islamabad",<br>
        &nbsp;&nbsp;"image_url": "https://cf.bstatic.com/xdata/images/hotel/square240/12345.jpg",<br>
        &nbsp;&nbsp;"rating": "9.1",<br>
        &nbsp;&nbsp;"check_in": "2025-08-01",<br>
        &nbsp;&nbsp;"check_out": "2025-08-04",<br>
        &nbsp;&nbsp;"days": 3<br>
   &nbsp; }<br>
]<br>


## ✅ How to Run It
Run this in your terminal:

- pip install -r requirements.txt
- python -m playwright install

## ⚙️ Function Parameters
**Parameter	Type	Description**
- city	string	Destination city
- checkin	string	Check-in date (YYYY-MM-DD)
- guests	int	Number of adults
- max_price	int	Booking price filter (1–5 Booking levels)
- days	int	Number of nights
- imit	int	Max number of listings to extract

## 📌 Notes
Headless mode is enabled by default<br>
Set headless=False in launch() if you want to debug in a visible browser.

Scraper uses fallback logic to handle missing or optional data.


## 📁 Project Structure

booking-scraper/<br>
├── scraper.py          # Main scraping script<br>
├── README.md           # Project documentation<br>


## 📜 License
This project is intended for educational and research purposes only.
Please ensure your use complies with Booking.com’s Terms of Service.


## 💡 Author
Built by Machine Minds 🧠<br>
For the LeadWithAI Hackathon<br>