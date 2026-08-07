import instagrapi
from pathlib import Path
from src.utils.logger import get_logger

logger = get_logger(__name__)

class InstagramService:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        self.bot = instagrapi.Client()
        self.is_logged_in = False

    def login(self) -> bool:
        if not self.username or not self.password:
            logger.error("Instagram credentials are not provided. Please set them in your .env file.")
            return False

        try:
            logger.info(f"Attempting to log in as {self.username}...")
            self.bot.login(username=self.username, password=self.password)
            self.is_logged_in = True
            logger.info("Successfully logged into Instagram.")
            return True
        except Exception as e:
            logger.error(f"Failed to login to Instagram: {e}")
            return False

    def upload_post(self, image_path: Path, caption: str) -> bool:
        if not self.is_logged_in:
            logger.error("Cannot upload post. Not logged in.")
            return False

        if not image_path.exists():
            logger.error(f"Image for upload not found: {image_path}")
            return False

        try:
            logger.info(f"Uploading {image_path.name} to Instagram...")
            self.bot.photo_upload(image_path, caption)
            logger.info("Successfully uploaded media.")
            return True
        except Exception as e:
            logger.error(f"Failed to upload media: {e}")
            return False

    def logout(self):
        if self.is_logged_in:
            try:
                self.bot.logout()
                logger.info("Logged out successfully.")
            except Exception as e:
                logger.error(f"Failed to logout safely: {e}")
