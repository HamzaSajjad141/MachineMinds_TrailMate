import requests
import json
from typing import List, Dict, Optional
import logging

class ActivityAgent:
    def __init__(self, location: str, preferences: Optional[List[str]] = None, budget: Optional[float] = None, test_mode: bool = False):
        self.location = location
        self.preferences = preferences or []
        self.budget = budget
        self.activities = []
        self.test_mode = test_mode

    def load_dummy_data(self):
        try:
            with open("dummy_data/activities.json", "r") as file:
                return json.load(file)
        except Exception as e:
            logging.warning(f"Failed to load dummy data: {e}")
            return []

    def fetch_activities_from_yelp(self) -> List[Dict]:
        url = "https://api.yelp.com/v3/businesses/search"
        headers = {"Authorization": "Bearer YOUR_YELP_API_KEY"}
        params = {
            "location": self.location,
            "categories": ",".join(self.preferences),
            "limit": 10
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            data = response.json()
            results = [
                {
                    "name": item["name"],
                    "category": item["categories"][0]["title"],
                    "rating": item.get("rating"),
                    "price": item.get("price", "N/A"),
                    "address": ", ".join(item["location"]["display_address"]),
                    "url": item["url"]
                }
                for item in data.get("businesses", [])
            ]
            return results
        except Exception as e:
            logging.warning(f"Yelp API failed: {e}")
            return []

    def fallback_scrape_tripadvisor(self) -> List[Dict]:
        return [
            {"name": "Mock Beach", "category": "Beach", "cost": "Free", "rating": 4.8, "url": "https://tripadvisor.com/mockbeach"}
        ]

    def fetch_activities(self) -> List[Dict]:
        if self.test_mode:
            return self.load_dummy_data()
        results = self.fetch_activities_from_yelp()
        return results if results else self.fallback_scrape_tripadvisor()

    def filter_by_budget(self, activities: List[Dict]) -> List[Dict]:
        if not self.budget:
            return activities
        filtered = []
        for activity in activities:
            cost_symbol = activity.get("price", "")
            estimated_cost = {
                "$": 20,
                "$$": 50,
                "$$$": 100,
                "$$$$": 200
            }.get(cost_symbol, 0)
            if estimated_cost <= self.budget / 5:
                filtered.append(activity)
        return filtered

    def suggest(self) -> List[Dict]:
        results = self.fetch_activities()
        filtered = self.filter_by_budget(results)
        self.activities = filtered
        return self.activities

    def format_response(self) -> str:
        if not self.activities:
            return "Sorry, no activities found for the given location and preferences."
        output = f"🧭 **Top Activities in {self.location}**\n\n"
        for i, act in enumerate(self.activities[:5], 1):
            output += f"{i}. **{act['name']}** ({act.get('category')}) – Rating: {act.get('rating')} – Cost: {act.get('price', 'N/A')}\n"
            if act.get("address"):
                output += f"📍 Address: {act.get('address')}\n"
            output += f"🔗 [Link]({act.get('url')})\n\n"
        return output


