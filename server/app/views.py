from app import queryIndex
from app import app
from flask import render_template, flash, redirect
from .forms import SearchForm

@app.route('/index', methods = ['GET','POST'])
def index():
    form = SearchForm()
    query = ""
    res = []
    if form.validate_on_submit():
        res = queryIndex.query(form.query.data)
    return render_template("index.html",
                           title = "Search Sonnets",
                           form = form,
                           query = query,
                           res = res)

