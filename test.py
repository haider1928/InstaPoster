import requests
import feedparser
from bs4 import BeautifulSoup

# Geo News English RSS feed
url = 'https://www.geo.tv/rss/1/0'

# Fake browser headers (Geo blocks bot-like requests)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
    'Accept': 'application/rss+xml',
}

# Request the feed
response = requests.get(url, headers=headers)

# Parse RSS feed
feed = feedparser.parse(response.content)

# Show top 5 headlines
for entry in feed.entries[:5]:
    title = entry.title
    link = entry.link
    description_html = entry.description
    description = BeautifulSoup(description_html, 'html.parser').text  # Clean description

    print(f"📰 {title}\n📄 {description.strip()}\n🔗 {link}\n")
