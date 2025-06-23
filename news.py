from newsapi import NewsApiClient
def getnews(index, apikey): 
    newsapi = NewsApiClient(api_key=apikey)

    # Fetch top headlines
    headlines = newsapi.get_top_headlines(q="Pakistan", sort_by="publishedAt", language="en")

    # Ensure the index is within bounds
    if index < len(headlines['articles']):
        return headlines['articles'][index]['title'], headlines['articles'][index]['description']
    else:
        return None, None