import sys
from src.config import Config
from src.utils.logger import get_logger
from src.utils.image import ImageEditor
from src.services.news import NewsService
from src.services.hadith import HadithService
from src.services.instagram import InstagramService

logger = get_logger("InstaPoster")

def load_existing_headlines() -> list[str]:
    """Load previously posted headlines to avoid duplicates."""
    if not Config.HEADLINES_FILE.exists():
        return []
    try:
        with open(Config.HEADLINES_FILE, "r", encoding="utf-8") as file:
            return file.read().splitlines()
    except Exception as e:
        logger.error(f"Could not load existing headlines: {e}")
        return []

def save_headline(headline: str):
    """Save the newly posted headline to the log file."""
    try:
        with open(Config.HEADLINES_FILE, "a", encoding="utf-8") as file:
            file.write(f"{headline}\n")
    except Exception as e:
        logger.error(f"Could not save headline {headline}: {e}")

def process_news() -> tuple[str, bool]:
    """Fetches news, creates the image, and returns the headline caption."""
    existing_headlines = load_existing_headlines()
    headlines = NewsService.get_dawn_headlines()
    
    selected_news = None
    for item in headlines:
        title = item["title"]
        if title not in existing_headlines and len(title) <= 100:
            selected_news = item
            break

    if not selected_news:
        logger.warning("No new suitable headlines available.")
        return "", False

    headline = selected_news["title"]
    description = selected_news.get("description", "No description available.")

    # Apply text styles using coordinates logic extracted from previous state
    texts = [
        {"text": headline, "size": 35, "x": 350, "y": 1002, "wrap_width": None}, 
        {"text": "WRECK NEWS", "size": 43, "x": 15, "y": 1000, "wrap_width": None},
        {"text": description, "size": 60, "x": 340, "y": 150, "wrap_width": 40}
    ]

    success = ImageEditor.add_text_to_image(
        image_path=Config.NEWS_TEMPLATE,
        output_path=Config.OUTPUT_NEWS_IMG,
        texts_to_add=texts
    )
    
    if success:
        logger.info(f"News image generated for: {headline}")
        return headline, True
    return "", False

def process_hadith() -> tuple[str, bool]:
    """Fetches hadith, creates the image, and returns the caption."""
    hadith_text, url = HadithService.get_hadith(max_length=300)
    
    if not hadith_text:
        logger.error("Failed to fetch hadith text.")
        return "", False

    texts = [
        {"text": hadith_text, "size": 30, "x": 20, "y": 200, "wrap_width": 46}
    ]

    success = ImageEditor.add_text_to_image(
        image_path=Config.HADITH_TEMPLATE,
        output_path=Config.OUTPUT_HADITH_IMG,
        texts_to_add=texts
    )

    if success:
        logger.info("Hadith image generated successfully.")
        # Ensure tags or links are formatted explicitly
        return f"{hadith_text}\n\nReference: {url}", True
    return "", False

def main():
    logger.info("Starting up InstaPoster Pipeline...")
    
    # 1. Pipeline processing Phase
    headline_caption, news_success = process_news()
    hadith_caption, hadith_success = process_hadith()

    if not news_success and not hadith_success:
        logger.error("Nothing engineered to post. Exiting pipeline...")
        sys.exit(1)

    # 2. Authentication Phase
    insta = InstagramService(username=Config.INSTAGRAM_USERNAME, password=Config.INSTAGRAM_PASSWORD)
    
    if not insta.login():
        logger.error("Authentication failed. Aborting script execution.")
        sys.exit(1)

    # 3. Execution Phase
    if news_success:
        logger.info("Publishing News component to Instagram...")
        if insta.upload_post(Config.OUTPUT_NEWS_IMG, headline_caption):
            save_headline(headline_caption)

    if hadith_success:
        logger.info("Publishing Hadith component to Instagram...")
        insta.upload_post(Config.OUTPUT_HADITH_IMG, hadith_caption)

    insta.logout()
    logger.info("Pipeline finalized successfully.")

if __name__ == "__main__":
    main()
