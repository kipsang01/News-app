from config import Api_Key
from newsapi import NewsApiClient

# Init
newsapi = NewsApiClient(api_key= Api_Key)

def headlines():
    
    top_headlines = newsapi.get_top_headlines()
                                        #   sources='bbc-news,the-verge',
                                        #   category='business',
                                        #   language='en',
                                        #   country='us')
                                        
    return top_headlines

def all_news():
    all_articles = newsapi.get_everything(q='',
                                        sources='bbc-news,the-verge',
                                        language='en',
                                        sort_by='relevancy',
                                        page=2)
    return all_articles

# /v2/top-headlines/sources
sources = newsapi.get_sources()