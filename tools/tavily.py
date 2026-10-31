from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()
client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))


def tavilySearch(query):
    response = client.search(query=query, max_results=5)
    results = []
    for i, r in enumerate(response["results"], 1):
        title = r.get("title", "Unknown")
        url = r.get("url", "")
        snippet = r.get("content", "").strip()
        # Keep only the first 300 characters to avoid wall-of-text
        if len(snippet) > 300:
            snippet = snippet[:300].rsplit(" ", 1)[0] + "..."

        results.append(f"{i}. **{title}**\n   {url}\n   {snippet}")

    return "\n\n".join(results)


# FUNCTION PURPOSE:
# This function performs a web search using the Tavily Search API.
# It accepts a search query, sends it to Tavily with a maximum of 5 results,
# and receives the API response as a Python dictionary containing search results.
# Each result is a dictionary with fields such as title, URL, content and score.
# The function iterates through the results using enumerate() to maintain result numbering,
# extracts the title, URL and content using dictionary.get() with default
# values(that unknown and empty spaces are default values),
# and removes unnecessary whitespace using strip().
# To avoid passing excessively long content to the LLM (reducing token consumption),
# it truncates each content snippet to 300 characters without cutting a word midway.
# Finally, it formats each result into a readable string containing its number, title,
# URL and content, combines all results using join(), and returns a single formatted string.
# This output can be passed to an LLM or used as a LangChain tool in a LangGraph agent
# to provide external, up-to-date information for answering user queries..
