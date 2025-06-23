import requests
import feedparser
from bs4 import BeautifulSoup

def getnews(count=5):
    rss_url = "https://www.geo.tv/rss/1/0"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(rss_url, headers=headers)
    feed = feedparser.parse(response.text)

    headlines = []
    descriptions = []

    for entry in feed.entries[:count]:
        headlines.append(entry.title)
        desc_html = entry.get("description", "")
        descriptions.append(BeautifulSoup(desc_html, "html.parser").text.strip())

    return headlines, descriptions
