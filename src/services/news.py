import requests
from bs4 import BeautifulSoup
from newsapi import NewsApiClient
from src.config import Config
from src.utils.logger import get_logger

logger = get_logger(__name__)


class NewsService:
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    }

    @staticmethod
    def _fetch_headlines_from_api() -> list[dict]:
        if not Config.NEWS_API_KEY:
            return []

        try:
            client = NewsApiClient(api_key=Config.NEWS_API_KEY)
            response = client.get_top_headlines(language='en', page_size=10)

            articles = response.get('articles', []) if isinstance(response, dict) else []
            headlines = []
            for article in articles:
                title = article.get('title', '').strip()
                description = article.get('description', '').strip() if article.get('description') else ''
                if title:
                    headlines.append({'title': title, 'description': description or 'No description available.'})

            if headlines:
                logger.info(f"Fetched {len(headlines)} headlines from NewsAPI.")
            return headlines
        except Exception as e:
            logger.warning(f"NewsAPI fetch failed: {e}")
            return []

    @staticmethod
    def get_headlines() -> list[dict]:
        """Retrieves news headlines from NewsAPI when configured, otherwise scrapes Dawn."""
        headlines = NewsService._fetch_headlines_from_api()
        if headlines:
            return headlines

        url = "https://www.dawn.com/latest-news"
        try:
            res = requests.get(url, headers=NewsService.HEADERS, timeout=10)
            res.raise_for_status()

            soup = BeautifulSoup(res.text, 'html.parser')
            headlines = []

            for story in soup.select('.story'):
                title_tag = story.select_one('.story__title a')
                desc_tag = story.select_one('.story__excerpt')

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
