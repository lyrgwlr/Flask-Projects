# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 10:10:13 2018

@author: 伍凌锐
"""

def get_isbn_or_key(q):
    if q.isdigit() and len(q) == 13:
        return 'isbn'
    short_q = q.replace('-','')
    if '-' in q and len(short_q) == 10 and short_q.isdigit:
        return 'isbn'
    return 'key'