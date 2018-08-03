class BookViewModel:    #处理单个书数据
    def __init__(self,book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages'] or ''
        self.price = book['price']
        self.summary = book['summary'] or ''
        self.image = book['image']
        self.author = '、'.join(book['author'])
        
class BookCollection:   #处理多个书数据
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''
        
    def fill(self,dogBook,keyword):
        self.total = dogBook.total
        self.keyword = keyword
        self.books = [BookViewModel() for book in dogBook.books]
#class BookViewModel:
#    
#    @classmethod
#    def package_single(cls,data,keyword):    #单本书的情况
#        returned = {
#            'books' : [],
#            'total' : 0,
#            'keyword' : keyword 
#        }
#        if data:
#            returned['total']=1
#            returned['books']=[cls.__cut_book_data(data)]
#        return returned
#            
#    @classmethod
#    def package_collection(cls,data,keyword):   #多本书的情况
#        returned = {
#            'books' : [],
#            'total' : 0,
#            'keyword' : keyword
#        }
#        if data:
#            returned['total']=data['total']
#            returned['books']=[cls.__cut_book_data(book) for book in data['books']]
#        return returned
#    
#    @classmethod
#    def __cut_book_data(cls,data): #裁剪/装饰数据成网页需要的样子
#        book = {
#            'title':data['title'],
#            'publisher':data['publisher'],
#            'pages':data['pages'] or '',
#            'price':data['price'],
#            'summary':data['summary'] or '',
#            'image':data['image'],
#            'author':'、'.join(data['author'])
#        }
#        return book