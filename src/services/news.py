import requests
from bs4 import BeautifulSoup
from src.utils.logger import get_logger

logger = get_logger(__name__)

class NewsService:
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    @staticmethod
    def get_dawn_headlines() -> list[dict]:
        """Scrapes the latest news headlines from Dawn news."""
        url = "https://www.dawn.com/latest-news"
        try:
            res = requests.get(url, headers=NewsService.HEADERS, timeout=10)
            res.raise_for_status()
            
            soup = BeautifulSoup(res.text, 'html.parser')
            headlines = []
            
            for story in soup.select(".story"):
                title_tag = story.select_one(".story__title a")
                desc_tag = story.select_one(".story__excerpt")
                
                if title_tag and desc_tag:
                    headlines.append({
                        'title': title_tag.get_text(strip=True),
                        'description': desc_tag.get_text(strip=True)
                    })
            
            logger.info(f"Fetched {len(headlines)} headlines from Dawn.")
            return headlines
        except Exception as e:
            logger.error(f"Failed to fetch headlines: {e}")
            return []
