# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:36:09 2018

@author: 伍凌锐
"""
from app.libs.myhttp import HTTP
from flask import current_app
class dogBook:  #模型层 MVC M层
    per_page=15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'
    
    def __init__(self):     #定义两个实例变量
        self.total = 0
        self.books = []
        
    def __fill_single(self,data):    #私有（__）实例方法
        if data:
            self.total = 1
            self.books.append(data)
            
    #构建以isbn号查找的api请求URL,并获取返回的结果
    def search_by_isbn(self,isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)
        return result
    
    def __fill_collection(self,data):    #私有（__）实例方法
        if data:
            self.total = data['total']
            self.books = data['books']
            
    #构建以关键字查找的api请求URL,并获取返回的结果
    def search_by_keyword(self,keyword,page=1):
        url = self.keyword_url.format(keyword,current_app.config['PER_PAGE'],self.calculate_start(page))
        result = HTTP.get(url)
        self.__fill_collection(result)
        return result
    
    def calculate_start(self,page):
        return (page-1)*current_app.config['PER_PAGE'] 
    
    @property
    def first(self):
        return self.books[0] if self.total >= 1 else None