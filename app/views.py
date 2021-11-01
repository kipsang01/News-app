from flask import Blueprint,render_template,redirect,url_for,request
from .requests import  all_news, headlines, search_category, search_News,source_news
from .forms import  SearchForm

views = Blueprint('views', __name__)

@views.route('home/All-news',  methods = ['GET', 'POST'])
def all_News():
    allnews = all_news()
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        searchTerm = form.searchTerm.data
        return redirect(url_for('views.searchNews', searchTerm =searchTerm))
    return render_template('All-news.html', allnews = allnews,form=form)

@views.route('home/<sourceChannel>',  methods = ['GET', 'POST'])
def channel_News(sourceChannel):
    allchannelnews = source_news(sourceChannel)
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        searchTerm = form.searchTerm.data
        return redirect(url_for('views.searchNews', searchTerm =searchTerm))
    return render_template('All-news.html', allnews = allchannelnews,form=form)


@views.route('/' , methods = ['GET', 'POST'])
@views.route('/home' , methods = ['GET', 'POST'])
def headline_articles():
    headlinesNews = headlines() 
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        searchTerm = form.searchTerm.data
        return redirect(url_for('views.searchNews', searchTerm =searchTerm))
    return render_template('home.html', headlinesNews = headlinesNews,form = form)



@views.route('home/All-news/<category>', methods = ['GET', 'POST'])
def categoryNews(category):
    category_news = search_category(category)
    form = SearchForm()
    if request.method == 'POST' and form.validate_on_submit():
        searchTerm = form.searchTerm.data
        return redirect(url_for('views.searchNews', searchTerm =searchTerm))
    return render_template('category.html', category_news = category_news, form=form, category = category)


@views.route('home/search/<searchTerm>', methods = ['GET','POST'])
def searchNews(searchTerm):
    found_news = search_News(searchTerm)
    form = SearchForm()
    if found_news:
        if request.method == 'POST' and form.validate_on_submit():
            searchTerm = form.searchTerm.data
            return redirect(url_for('views.searchNews', searchTerm =searchTerm, form = form))
        
        return render_template('search.html', found_news = found_news, form=form, searchTerm=searchTerm)
    else:
        return render_template('error.html', form=form)


@views.errorhandler(404)
def not_found(error):
    return render_template('notFound.html', error =error)