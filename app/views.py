from flask import Blueprint,render_template
from .requests import  all_news, headlines, search_category

views = Blueprint('views', __name__)

@views.route('/All-news')
def allNews():
    allnews = all_news()
    return render_template('All-news.html', allnews = allnews)


@views.route('/')
@views.route('/home')
def headline_articles():
    headlinesNews = headlines()
    
    return render_template('home.html', headlinesNews = headlinesNews)

@views.route('/home/<category>')
def categoryNews(category):
    category_news = search_category(category)
    print(category_news)
    return render_template('category.html', category_news = category_news)

