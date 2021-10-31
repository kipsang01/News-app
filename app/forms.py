from flask_wtf import FlaskForm
from  wtforms import  StringField, SubmitField
from  wtforms.validators import  Required

class SearchForm(FlaskForm):
    searchTerm = StringField('search',validators=[Required()])
    
    submit = SubmitField('Search')