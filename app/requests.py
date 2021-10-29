from config import Api_Key
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key= Api_Key)

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin')
                                        #   sources='bbc-news,the-verge',
                                        #   category='business',
                                        #   language='en',
                                        #   country='us')

# /v2/everything
def all_news():
    all_articles = newsapi.get_everything(q='',
                                        sources='bbc-news,the-verge',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
    return all_articles

# /v2/top-headlines/sources
sources = newsapi.get_sources()