import requests
from bs4 import BeautifulSoup
import random
def get_hadith():
# Choose a random page from Sunnah.com (change collection as needed)
    hadith_collections = ["bukhari", "muslim", "tirmidhi"]
    collection = random.choice(hadith_collections) 
    if hadith_collections == "muslim" # Randomly pick a collection
        page = random.randint(1, 56)
    elif hadith_collections == "bukhari":
        page = random.randint(1, 97)
    elif hadith_collections == "tirmidhi":
        page = random.randint(1, 49)  # Adjust the page range based on availability

    # Construct URL
    url = f"https://sunnah.com/{collection}/{page}"

    # Fetch HTML data
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract Hadith texts
    hadiths = soup.find_all("div", class_="text_details")

    if hadiths:
        random_hadith = random.choice(hadiths).text.strip()
        return random_hadith
    else:
        print("No Hadith found. Check the URL or page range.")

