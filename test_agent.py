import os
from dotenv import load_dotenv
load_dotenv()


from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent
from langchain_tool import activity_agent_tool  # Make sure this matches your filename

# Initialize the language model
llm = ChatOpenAI(temperature=0, model="gpt-4o")  # Requires OpenAI API key

# Register your tools
tools = [activity_agent_tool]

# Initialize LangChain agent
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

# Test query
query = "Find adventurous beach activities in Bali for under $100"
response = agent.run(query)

# Print the results
print(response)