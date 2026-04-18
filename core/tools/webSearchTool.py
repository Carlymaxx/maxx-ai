import requests
import os
import html

class WebSearchTool:
    def __init__(self):
        self.api_key = os.getenv("GOOGLE_API_KEY")
        self.search_engine_id = os.getenv("GOOGLE_SEARCH_ENGINE_ID")

    def search(self, query, num_results=5):
        if not self.api_key or not self.search_engine_id:
            return self._duckduckgo_fallback(query, num_results)

        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": self.api_key,
                "cx": self.search_engine_id,
                "q": query,
                "num": num_results
            }
            response = requests.get(url, params=params, timeout=10)
            data = response.json()

            if "items" in data:
                results = []
                for item in data["items"]:
                    results.append(f"- {item['title']}: {item['link']}")
                return "\n".join(results)
            return "No results found"
        except Exception as e:
            return self._duckduckgo_fallback(query, num_results)

    def _duckduckgo_fallback(self, query, num_results):
        try:
            url = "https://html.duckduckgo.com/html/"
            data = {"q": query}
            response = requests.post(url, data=data, timeout=10)
            results = []
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            for result in soup.select(".result__snippet")[:num_results]:
                title = result.find_previous("a")
                if title:
                    results.append(f"- {html.unescape(title.text)}: {title.get('href', '')}")
            return "\n".join(results) if results else "No results found"
        except Exception as e:
            return f"Search failed: {str(e)}"

web_search_tool = WebSearchTool()