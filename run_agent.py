import functools, operator, requests, os, json
from bs4 import BeautifulSoup
from duckduckgo_search import DDGS
from langchain.agents import AgentExecutor
from langchain_core.messages import BaseMessage, HumanMessage


from crewai_tools import ScrapeWebsiteTool

# To enable scrapping any website it finds during it's execution
tool = ScrapeWebsiteTool()

# Initialize the tool with the website URL, so the agent can only scrap the content of the specified website
tool = ScrapeWebsiteTool(website_url='https://docs.crewai.com/tools/ScrapeWebsiteTool/#installation')

# Extract the text from the site
text = tool.run()
print(text)