import requests
from bs4 import BeautifulSoup
import random

# Choose a random page from Sunnah.com (change collection as needed)
hadith_collections = ["bukhari", "muslim", "tirmidhi"]
collection = random.choice(hadith_collections)  # Randomly pick a collection
page = random.randint(1, 10)  # Adjust the page range based on availability

# Construct URL
url = f"https://sunnah.com/{collection}/{page}"

# Fetch HTML data
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract Hadith texts
hadiths = soup.find_all("div", class_="text_details")

if hadiths:
    random_hadith = random.choice(hadiths).text.strip()
    print(f"📖 Random Hadith from {collection.capitalize()}:\n")
    print(random_hadith)
else:
    print("No Hadith found. Check the URL or page range.")
