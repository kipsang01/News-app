from flask import Blueprint,render_template
from .requests import  all_news

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    
    news = []
    contents = []
    description = []
    images =[]
    pub_Date =[]
    links = []
    authors = []

    popular =  all_news()
    articles = popular['articles']
    # 
    for i in range(len(articles)):
        article = articles[i]
        
        news.append(article['title'])
        contents.append(article['content'])
        description.append(article['description'])
        images.append(article['urlToImage'])
        pub_Date.append(article['publishedAt'])
        links.append(article['url'])
        authors.append(article['author'])
        
        
        allnews = zip(news,contents, description,images, pub_Date,authors, links)
    
    
    return render_template('home.html', allnews = allnews)