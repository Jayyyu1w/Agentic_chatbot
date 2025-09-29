import os
import getpass
from typing import Literal
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import DuckDuckGoSearchAPIWrapper

class SearchTool:
    """
    搜尋工具，提供Tavily與duckduckgo搜尋
    """
    def __init__(self, search_engine=Literal["tavily", "duckduckgo"], search_results=5):
        if search_engine == "tavily":
            if not os.environ.get("TAVILY_API_KEY"):
                os.environ["TAVILY_API_KEY"] = getpass.getpass("Enter your Tavily API key: ")
            self.search_engine = TavilySearchResults(max_results=search_results)
        elif search_engine == "duckduckgo":
            wrapper = DuckDuckGoSearchAPIWrapper(region="tw-tzh", max_results=search_results)
            self.search_engine = DuckDuckGoSearchRun(api_wrapper=wrapper)

    def search(self, query):
        return self.search_engine.invoke(query)