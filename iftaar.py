import requests
from bs4 import BeautifulSoup

# URL of the website (change it according to your location)
url = "https://hamariweb.com/islam/lahore_prayer-timing5.aspx" 

# Send a GET request
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find the Maghrib (Iftar) time
#maghrib_time = soup.find("span", {"class": "c_table timer_table"})

print(f"Iftar time in Lahore: {soup}")
