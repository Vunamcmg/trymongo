import uuid
import datetime
from database import Database

__author__ = "Vu Hoai Nam"

class Post(object):
    #Init
    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None ):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.date = date
        self.id = uuid.uuid4().hex if id is None else id()
    #convert to json
    def json(self):
        return {
            'id' : self.id,
            'blog_id' : self.blog_id,
            'title': self.title,
            'author' : self.author,
            'date': self.date,
            'content':self.content
        }
    #save post to database
    def saveToMongo(self):
        Database.insert(collection='posts',data=self.json())
    #find post in database by ID
    @staticmethod
    def findPost(id):
        Database.findOne(collection='posts',query={'id':id})
    #delete post in database by ID
    @staticmethod
    def deletePost(id):
        Database.deleteOne(collection='posts',query={'id':id})
    #update post to database by ID
    #    Database.UpdateOne(collection='posts',query=self.id)