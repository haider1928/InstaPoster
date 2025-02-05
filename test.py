from PIL import Image, ImageDraw, ImageFont
from newsapi import NewsApiClient
import instagrapi
import requests
import time

# Define your Instagram credentials here
INSTAGRAM_USERNAME = "wreck._.it._.ralph"
INSTAGRAM_PASSWORD = "haiderchangedit@1"

# Function to add newlines to text
def add_newlines(text, interval):
    chunks = [text[i:i+interval] for i in range(0, len(text), interval)]
    return '-\n\n'.join(chunks)

# Function to get the latest news
def get_news(index): 
    newsapi = NewsApiClient(api_key='bed5ceda36b94e4d862e061e7db54301')
    headlines = newsapi.get_top_headlines(language='en', country='us')

    if index < len(headlines['articles']):
        return headlines['articles'][index]['title'], headlines['articles'][index]['description']
    else:
        return None, None

# Function to edit the image with text
def edit_image(text, size, x, y, imagepath):
    image = Image.open(imagepath)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size)
    position = (x, y)
    draw.text(position, text, fill="white", font=font)
    image.save('output_image.jpg')

# Function to get weather forecast for Lahore
def get_weather():
    # OpenWeatherMap API Key
    api_key = "your_openweathermap_api_key"
    url = f"http://api.openweathermap.org/data/2.5/weather?q=Lahore&appid={api_key}&units=metric"
    
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        main = data['main']
        weather_description = data['weather'][0]['description']
        temperature = main['temp']
        humidity = main['humidity']
        weather_report = f"Weather: {weather_description}\nTemp: {temperature}°C\nHumidity: {humidity}%"
        return weather_report
    else:
        return "Weather data not available"

# Function to handle Instagrapi login and session check
def check_login_and_post():
    bot = instagrapi.Client()

    # Login using username and password
    status = bot.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)  # Using bot.login() with username and password

    # If not logged in, re-login
    if not status:
        bot.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)  # Re-login if session is not valid
        print("Re-logged in successfully!")

    return bot

# Read headlines from the file
with open("headlines.txt", 'r+') as headlines_txt:
    existing_headlines = headlines_txt.read().splitlines()
    ind = 0

    # Start the continuous loop
    while True:
        # Fetch news and check if it's already in the file
        while True:
            headline, description = get_news(ind)
            if headline is None:
                print("No more headlines available.")
                break
            if headline not in existing_headlines and len(headline) <= 100:
                # Process and save the headline
                edit_image(headline, 35, 350, 1002, "your_image.jpg")
                edit_image("WRECK NEWS", 43, 15, 1000, "output_image.jpg")
                edit_image(add_newlines(description or "No description available.", 40), 60, 340, 150, "output_image.jpg")
                headlines_txt.write(f"{headline}\n")
                break
            ind += 1

        # Get weather and edit weather image
        weather_info = get_weather()
        edit_image(weather_info, 30, 30, 50, "weather.jpg")
        
        # Check if logged in and upload images
        bot = check_login_and_post()

        # Upload news image
        post = bot.photo_upload("output_image.jpg", f"{headline}")
        print(f"Uploaded news image: {headline}")

        # Upload weather image
        post = bot.photo_upload("output_image.jpg", "Weather Update for Lahore")
        print("Uploaded weather image.")

        # Sleep for 6 hours
        print("Sleeping for 6 hours...")
        time.sleep(21600)  # 6 hours = 21600 seconds
