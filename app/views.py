from flask import Blueprint,render_template
from .requests import  all_news, headlines

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
