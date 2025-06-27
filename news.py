import requests
from bs4 import BeautifulSoup

def get_dawn_headlines():
    url = "https://www.dawn.com/latest-news"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
    }

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    headlines = []
    stories = soup.select(".story")

    for story in stories:
        title_tag = story.select_one(".story__title a")
        desc_tag = story.select_one(".story__excerpt")

        if title_tag and desc_tag:
            title = title_tag.get_text(strip=True)
            description = desc_tag.get_text(strip=True)
            headlines.append({
                'title': title,
                'description': description
            })

    return headlines





