# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:36:09 2018

@author: 伍凌锐
"""
from myhttp import HTTP

class dogBook:
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start{}'
    
    @classmethod
    def search_by_isbn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result
    
    @classmethod
    def search_by_keyword(cls,keyword,count=15,start=0):
        url = cls.keyword_url.format(keyword,count,start)
        result = HTTP.get(url)
        return result