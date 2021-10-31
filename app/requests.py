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
        source = articles['source["name"]']
        title = article['title']
        content = article['content']
        description = article['description']
        urlToImage = article['urlToImage']
        publishedAt = article['publishedAt']
        url = article['url']
        author = article['author']

        new_article =  News(source,title, content, description, urlToImage, publishedAt,url,author)
        top_headlines.append(new_article)
    return top_headlines

def all_news():
    all_articles = []
    allArticles = newsapi.get_everything(q='',
                                        sources='bbc-news,the-verge,nbc-news',
                                        language='en',
                                        sort_by='publishedAt',
                                        page=1)
    headlines_news =  allArticles
    articles = headlines_news['articles']
    for i in range(len(articles)):
        article = articles[i]

        source = articles['source["name"]']
        title = article['title']
        content = article['content']
        description = article['description']
        urlToImage = article['urlToImage']
        publishedAt = article['publishedAt']
        url = article['url']
        author = article['author']

        new_article =  News(source,title, content, description, urlToImage, publishedAt,url,author)
        all_articles.append(new_article)
    return all_articles


def search_category(category):
    found_articles = []
    allArticles = newsapi.get_top_headlines( q = '',
                                            country='us',
                                            category = f'{category}' )
    
    articles = allArticles['articles']
    for i in range(len(articles)):
        article = articles[i]

        source = articles['source["name"]']
        title = article['title']
        content = article['content']
        description = article['description']
        urlToImage = article['urlToImage']
        publishedAt = article['publishedAt']
        url = article['url']
        author = article['author']

        new_article =  News(source,title, content, description, urlToImage, publishedAt,url,author)
        found_articles.append(new_article)
        
    return found_articles



def search_News(searchTerm):
    found_news = []
    allArticles = newsapi.get_everything( q = f'{searchTerm}',
                                            sources='bbc-news,the-verge,nbc-news',
                                            domains='bbc.co.uk,techcrunch.com',
                                            language='en',
                                            sort_by='relevancy',
                                            page=2 )
    
    articles = allArticles['articles']
    for i in range(len(articles)):
        article = articles[i]

        source = articles['source["name"]']
        title = article['title']
        content = article['content']
        description = article['description']
        urlToImage = article['urlToImage']
        publishedAt = article['publishedAt']
        url = article['url']
        author = article['author']

        new_article =  News(source,title, content, description, urlToImage, publishedAt,url,author)
        found_news.append(new_article)
        
    return found_news
    
    
def source_News():
    
    sources = newsapi.get_sources()