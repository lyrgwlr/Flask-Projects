from app.models.base import Base,db
from sqlalchemy import Column,Integer,String,Boolean,Float,SmallInteger
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from app import login_manager
from app.libs.helper import get_isbn_or_key
from app.spider.searchbook import dogBook
from app.models.wish import Wish
from app.models.gift import Gift

class User(Base,UserMixin):
    id = Column(Integer,primary_key=True)
#    status = Column(SmallInteger,default=1)
    nickname = Column(String(24),nullable=False)
    phone_number = Column(String(18),unique=True)
    email = Column(String(50),unique=True,nullable=False)
    password = Column(String(128),nullable=False)
    confirmed = Column(Boolean,default=False)
    beans = Column(Float,default=0)
    send_counter = Column(Integer,default=0)
    receive_counter = Column(Integer,default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))
    
    def check_password(self,raw):
        return check_password_hash(self.password,raw)
    
#    @property
#    def password(self):     #getter
#        return self._password
#    
#    @password.setter    #setter
#    def password(self,raw):
#        self._password = generate_password_hash(raw)
    def can_save_to_list(self,isbn):
        if get_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = dogBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        #不允许一个用户同时赠送多本相同图书
        #不允许一个用户同时是赠送者和索要者
        gifting = Gift.query.filter_by(uid=self.id,isbn=isbn,launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id,isbn=isbn,launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False
    
        
@login_manager.user_loader
def get_user(uid):
    return User.query.get(int(uid))