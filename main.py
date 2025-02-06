from image_editor import edit_image
from news import getnews
import instagrapi
from data_enhancer import add_newlines
from instagram_logger import login, logout, login_by_session_id
# Read headlines from the file
news_api_key = open("newsapikey.txt", 'r').read()
with open("headlines.txt", 'r+', encoding="utf-8", errors="ignore") as headlines_txt:

    existing_headlines = headlines_txt.read().splitlines()
    ind = 0

    # Fetch news and check if it's already in the file
    while True:
        headline, description = getnews(ind, news_api_key)
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
#bot = login(username.read().strip(), password.read().strip())
bot = login_by_session_id("52416138425%3AkOglGMcWfjdiHp%3A25%3AAYdzvUj70YPkgtRjOsilN7pX3lWEtEVIXYf9EHrsoQ")
post = bot.photo_upload("output_image.jpg", f"{headline}")
#status = logout(bot=bot)