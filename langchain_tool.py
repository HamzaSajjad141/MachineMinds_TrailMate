from langchain.tools import Tool
from activity_agent import ActivityAgent  # Make sure this import matches your file name

def activity_tool_function(location: str, preferences: str = "", budget: float = None) -> str:
    # Convert comma-separated preferences to a list
    pref_list = [p.strip() for p in preferences.split(",")] if preferences else []
    
    # Create agent in test_mode to use dummy data
    agent = ActivityAgent(location=location, preferences=pref_list, budget=budget, test_mode=True)
    agent.suggest()
    return agent.format_response()

# Register LangChain Tool
activity_agent_tool = Tool.from_function(
    name="activity_agent",
    func=activity_tool_function,
    description=(
        "Find and recommend tourist activities based on location, preferences, and budget. "
        "Returns top options with ratings, cost, and links. Useful for planning fun and budget-friendly trips."
    )
)