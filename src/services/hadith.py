import random
import requests
from bs4 import BeautifulSoup
from src.utils.logger import get_logger

logger = get_logger(__name__)

class HadithService:
    @staticmethod
    def get_hadith(max_length: int = 300, max_retries: int = 5) -> tuple[str, str]:
        """
        Fetches a random Hadith from sunnah.com.
        Retries to ensure we find a valid Hadith within length constraints.
        """
        collections = {
            "bukhari": 97,
            "muslim": 56,
            "tirmidhi": 49
        }
        
        for attempt in range(max_retries):
            collection = random.choice(list(collections.keys()))
            max_page = collections[collection]
            page = random.randint(1, max_page)
            url = f"https://sunnah.com/{collection}/{page}"
            
            try:
                response = requests.get(url, timeout=10)
                if response.status_code != 200:
                    continue
                    
                soup = BeautifulSoup(response.text, "html.parser")
                hadiths = soup.find_all("div", class_="text_details")
                
                if hadiths:
                    random_hadith = random.choice(hadiths).get_text(strip=True)
                    if len(random_hadith) <= max_length:
                        logger.info(f"Found Hadith of length {len(random_hadith)} (attempt {attempt + 1})")
                        return random_hadith, url
            except requests.RequestException as e:
                logger.warning(f"Request failed for {url}: {e}")
                
        logger.error("Failed to fetch a suitable Hadith after multiple attempts.")
        return "", ""
