from image_editor import edit_image
from news import get_news
import instagrapi
from data_enhancer import add_newlines
from instagram_logger import login
# Read headlines from the file

with open("headlines.txt", 'r+', encoding="utf-8", errors="ignore") as headlines_txt:

    existing_headlines = headlines_txt.read().splitlines()
    ind = 0

    # Fetch news and check if it's already in the file
    while True:
        headline, description = get_news(ind)
        if headline is None:
            print("No more headlines available.")
            break
        if headline not in existing_headlines and len(headline) <= 100:
            # Process and save the headline
            edit_image(headline, 35, 350, 1002, "your_image.jpg")  # Headline editor
            edit_image("WRECK NEWS", 43, 15, 1000, "output_image.jpg")
            edit_image(add_newlines(description or "No description available.", 40), 60, 340, 150, "output_image.jpg")
            headlines_txt.write(f"{headline}\n")
            break
        ind += 1

bot = instagrapi.Client()
username = open("username.txt", "r")
password = open("password.txt", 'r')
login(username.read().strip(), password.read().strip())
post = bot.photo_upload("output_image.jpg", f"{headline}")
bot.logout()