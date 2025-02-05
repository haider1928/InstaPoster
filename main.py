from PIL import Image, ImageDraw, ImageFont 
from newsapi import NewsApiClient
import instagrapi

# ✅ Function to format text with newlines
def add_newlines(text, interval):
    chunks = [text[i:i+interval] for i in range(0, len(text), interval)]
    return '-\n\n'.join(chunks)

# ✅ Function to fetch news headlines
def get_news(index): 
    newsapi = NewsApiClient(api_key='bed5ceda36b94e4d862e061e7db54301')

    # Fetch top headlines
    headlines = newsapi.get_top_headlines(language='en', country='us')

    # Ensure index is within bounds
    if index < len(headlines['articles']):
        return headlines['articles'][index]['title'], headlines['articles'][index]['description']
    else:
        return None, None

# ✅ Function to edit image with text
def edit_image(text, max_size, x, y, imagepath):
    try:
        image = Image.open(imagepath)
        draw = ImageDraw.Draw(image)

        # 🔹 Try loading Arial, otherwise use default font
        font_size = max_size
        while font_size > 20:  # Prevents going too small
            try:
                font = ImageFont.truetype("arial.ttf", font_size)
                break  # If font loads successfully, exit loop
            except IOError:
                font_size -= 2  # Reduce font size if Arial isn't found

        draw.text((x, y), text, fill="white", font=font)
        image.save('output_image.jpg')

    except Exception as e:
        print(f"Error editing image: {e}")

# ✅ Read headlines safely with encoding fix
try:
    with open("headlines.txt", 'r+', encoding="utf-8", errors="ignore") as headlines_txt:
        existing_headlines = headlines_txt.read().splitlines()
        ind = 0

        while True:
            headline, description = get_news(ind)
            if headline is None:
                print("No more headlines available.")
                break
            if headline not in existing_headlines and len(headline) <= 100:
                # 🖼️ Apply text to image with increased font size
                edit_image(headline, 55, 350, 950, "your_image.jpg")  # Headline
                edit_image("WRECK NEWS", 65, 15, 980, "output_image.jpg")  # Logo
                edit_image(add_newlines(description or "No description available.", 40), 70, 340, 120, "output_image.jpg")  # Description

                headlines_txt.write(f"{headline}\n")
                break
            ind += 1

except Exception as e:
    print(f"Error reading headlines.txt: {e}")

# ✅ Instagram Bot Setup
try:
    bot = instagrapi.Client()
    login = bot.login("wreck._.it._.ralph", "haiderchangedit@1")
    post = bot.photo_upload("output_image.jpg", f"{headline}")
    bot.logout()

except Exception as e:
    print(f"Instagram bot error: {e}")
