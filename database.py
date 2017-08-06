import pymongo
__author__ = "Vu Hoai Nam"

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['fullstack']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def findOne(collection, query):
        return Database.DATABASE[collection].find_one(query)

    #Delete with id
    @staticmethod
    def deleteOne(collection,query):
        Database.DATABASE[collection].delete_one(query)
