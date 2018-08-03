# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 12:08:31 2018

@author: 伍凌锐
"""
from app.libs import helper
from app.spider.searchbook import dogBook
from flask import jsonify,request
from . import web
from app.forms.book import SearchForm
from app.view_models.book import BookViewModel,BookCollection
@web.route('/book/search')
def search():
    """
        q:common search/isbn    
        page
    """
    form = SearchForm(request.args)
    books = BookCollection()
    
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = helper.get_isbn_or_key(q)
        dog_book = dogBook()
        
        if isbn_or_key == 'isbn':
            dog_book.search_by_isbn(q)
        else:
            dog_book.search_by_isbn(q,page)
            
        books.fill(dog_book,q)
        return jsonify(books)
    else:
        return jsonify(form.errors)