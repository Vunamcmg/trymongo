import uuid
from Models.post import Post
import datetime

from database import Database

__author__ = "Vu Hoai Nam"

class Blog(object):
    #init
    def __init__(self, author, title, description,id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id
     #create post of blog
    def newPost(self):
        title = input("Title: ")
        content = input("Content: ")
        date = datetime.datetime.utnow()
        post = Post(blog_id = self.id,
                    title=title,
                    content = content,
                    author=self.author,
                    date=date)
        post.saveToMongo()
    #convert to json
    def json(self):
        return {
            'author':self.author,
            'title':self.title,
            'description':self.description,
            'id':self.id
        }
    #Save blog to database
    def saveToMongo(self):
        return Database.insert(collection='blogs',data=self.json())
    # find blog in Database
    @staticmethod
    def findBlog(self):
        return Database.find(collection='blogs',query=self.id)
    # list post with post author(blog_id)
    def listPost(self):
        return Database.find(collection='post', query=self.id)
    # find post with blogid
    @staticmethod
    def listPost(id):
        return Database.find(collection='post',query={'blog_id':id})