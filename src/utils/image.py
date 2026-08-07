import textwrap
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
from src.utils.logger import get_logger

logger = get_logger(__name__)

class ImageEditor:
    @staticmethod
    def _get_font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        try:
            return ImageFont.truetype("arial.ttf", size)
        except IOError:
            logger.warning("arial.ttf not found. Using default font.")
            return ImageFont.load_default()

    @staticmethod
    def wrap_text(text: str, width: int) -> str:
        """Wraps text intelligently to a specific width without breaking words mid-stream."""
        if not text:
            return ""
        lines = textwrap.wrap(text, width=width)
        return "\n".join(lines)

    @staticmethod
    def add_text_to_image(
        image_path: Path,
        output_path: Path,
        texts_to_add: list[dict],
        save: bool = True
    ) -> bool:
        """
        Adds multiple text elements to an image.
        
        texts_to_add format:
        [
            {"text": "Hello", "size": 35, "x": 100, "y": 200, "wrap_width": None},
            ...
        ]
        """
        try:
            if not image_path.exists():
                logger.error(f"Image not found: {image_path}")
                return False

            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)

            for item in texts_to_add:
                text_content = item.get("text", "")
                wrap_width = item.get("wrap_width")
                
                if wrap_width:
                    text_content = ImageEditor.wrap_text(text_content, wrap_width)

                font = ImageEditor._get_font(item.get("size", 30))
                position = (item.get("x", 0), item.get("y", 0))
                
                draw.text(position, text_content, fill="white", font=font)

            if save:
                output_path.parent.mkdir(parents=True, exist_ok=True)
                image.save(output_path)
                logger.info(f"Image saved to {output_path.name}")
                
            return True
        except Exception as e:
            logger.error(f"Failed to edit image: {e}")
            return False
