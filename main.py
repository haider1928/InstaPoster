from PIL import Image, ImageDraw, ImageFont 
from newsapi import NewsApiClient
import instagrapi
def add_newlines(text, interval):
    # Split the text into chunks of the specified interval
    chunks = [text[i:i+interval] for i in range(0, len(text), interval)]
    # Join the chunks with '\n'
    return '-\n\n'.join(chunks)

def get_news(index): 
    newsapi = NewsApiClient(api_key='bed5ceda36b94e4d862e061e7db54301')

    # Fetch top headlines
    headlines = newsapi.get_top_headlines(language='en', country='us')

    # Ensure the index is within bounds
    if index < len(headlines['articles']):
        return headlines['articles'][index]['title'], headlines['articles'][index]['description']
    else:
        return None, None

def edit_image(text, size, x, y, imagepath):
    # Load an image
    image = Image.open(imagepath)

    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Define the text and font
    try:
        font = ImageFont.truetype("arial.ttf", size)
    except IOError:
        font = ImageFont.load_default()

    # Define text position
    position = (x, y)

    # Draw the text on the image
    draw.text(position, text, fill="white", font=font)

    # Save the image with the text
    image.save('output_image.jpg')

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

login = bot.login("wreck._.it._.ralph", "vapoursaintgood@1")
post = bot.photo_upload("output_image.jpg", f"{headline}")
bot.logout()