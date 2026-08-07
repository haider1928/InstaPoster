import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    # Paths
    DATA_DIR = BASE_DIR / "data"
    ASSETS_DIR = BASE_DIR / "assets"
    OUTPUT_DIR = BASE_DIR / "output"
    
    HEADLINES_FILE = DATA_DIR / "headlines.txt"
    NEWS_TEMPLATE = ASSETS_DIR / "your_image.jpg"
    HADITH_TEMPLATE = ASSETS_DIR / "hadith.jpg"
    OUTPUT_NEWS_IMG = OUTPUT_DIR / "output_image.jpg"
    OUTPUT_HADITH_IMG = OUTPUT_DIR / "output_hadith.jpg"
    
    # API / Credentials
    INSTAGRAM_USERNAME = os.getenv("instagram_username", "")
    INSTAGRAM_PASSWORD = os.getenv("instagram_password", "")
    NEWS_API_KEY = os.getenv("newsapi", "")
    
    @classmethod
    def setup_directories(cls):
        cls.DATA_DIR.mkdir(exist_ok=True)
        cls.ASSETS_DIR.mkdir(exist_ok=True)
        cls.OUTPUT_DIR.mkdir(exist_ok=True)

Config.setup_directories()
