# 🏡 Airbnb Scraper

This is an **asynchronous web scraper** built with **Python and Playwright** to extract Airbnb listings for a specific location, guest count, price range, and date range.

---

## 🚀 Features

- ✅ Uses **Playwright (Chromium)** for browser automation
- ✅ Handles pagination with smooth scrolling and click fixes  
- ✅ Scrapes listing titles, prices, ratings, area, URLs   
- ✅ Asynchronous for fast, modern scraping  
- ✅ Output is a clean JSON object  

---

## 📂 Project Structure

```
MachineMinds_TrailMate/
│
├── airbnb_scraper.py        # Main scraping script
├── requirements.txt         # Python dependencies
├── .gitignore               # Files ignored by Git
└── README.md                # You're here!
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/airbnb-scraper.git
cd airbnb-scraper
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### 4. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 5. Install Playwright browser binaries

```bash
playwright install chromium
```

---

## ▶️ How to Run

In `airbnb_scraper.py`, update your input variables:

```python
location = "Istanbul"
guests = 4
max_price = 1500
check_in = "2025-09-15"
check_out = "2025-09-20"
limit = 10
```

Then run:

```bash
python airbnb_scraper.py
```

---

## 🧠 Code Overview

- `scrape_airbnb()`: Main async function to launch a browser, visit the Airbnb search page, and extract listings
- Extracts:
  - Title, subtitle, price
  - URL and area
  - Rating, reviews, and date range
- Returns a structured JSON list

---

## 📦 Sample Output

```json
[
  {
    "title": "Apartment in Istanbul",
    "subtitle": "Spacious & Peaceful Flat with Sea View",
    "price": "$1,319 for 5 nights",
    "url": "https://www.airbnb.com/rooms/961550",
    "location": "Istanbul",
    "area": "Fatih",
    "rating": "4.9",
    "reviews": "112",
    "check_in": "2025-09-15",
    "check_out": "2025-09-20",
    "nights": 5
  }
]
```
---

## 📝 Notes

- This tool is intended for **educational and personal use**
- Airbnb may update their HTML structure — update selectors if needed
- Always use responsibly and respect website terms of service

---

## 💡 Author

Built by **Machine Minds** 🧠  
For the **LeadWithAI Hackathon**  

