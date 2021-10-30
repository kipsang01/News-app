from config import Api_Key
from newsapi import NewsApiClient
from .models import News

# Init
newsapi = NewsApiClient(api_key= Api_Key)

def headlines():
    top_headlines =[]
    headlines = newsapi.get_top_headlines()

    headlines_news =  headlines
    articles = headlines_news['articles']
    for i in range(len(articles)):
        article = articles[i]

        title = article['title']
        content = article['content']
        description = article['description']
        urlToImage = article['urlToImage']
        publishedAt = article['publishedAt']
        url = article['url']
        author = article['author']

        new_article =  News(title, content, description, urlToImage, publishedAt,url,author)
        top_headlines.append(new_article)
    return top_headlines

def all_news():
    all_articles = []
    allArticles = newsapi.get_everything(q='',
                                        sources='bbc-news,the-verge',
                                        language='en',
                                        sort_by='relevancy',
                                        page=1)
    headlines_news =  allArticles
    articles = headlines_news['articles']
    for i in range(len(articles)):
        article = articles[i]

        title = article['title']
        content = article['content']
        description = article['description']
        urlToImage = article['urlToImage']
        publishedAt = article['publishedAt']
        url = article['url']
        author = article['author']

        new_article =  News(title, content, description, urlToImage, publishedAt,url,author)
        all_articles.append(new_article)
    return all_articles


def search_news(searchTerm):
    found_articles = newsapi.get_everything(q =searchTerm , sort_by= 'popularity')
    
# /v2/top-headlines/sources
sources = newsapi.get_sources()