from database import Database
from Models.post import Post
from Models.blog import Blog
__author__ = "Vu Hoai Nam"

class Menu(object):
    #Check user if user has blog then go to user blog else create new
    def __init__(self):
        self.user = input("Enter your author nam: ")
        self.userBlog = None
        #check user
        if self.userHasBlog():
            print("Welcome back {}".format(self.user))
        else:
            self.createNewAccount()

    def userHasBlog(self):
        author = Database.findOne(collection='blogs',query={'author':self.user})
        if author is not None:
            return True
        else:
            return False

    def createNewAccount(self):
        author = input("Author: ")
        title = input("Title: ")
        description = input("Description: ")
        blog = Blog(author = author, title = title, description = description)
        blog.saveToMongo()
        self.userBlog = blog

    def runMenu(self):
        readOrWrite = input("Choose action Read (R) - Write (W) : ")
        if readOrWrite == 'R' or readOrWrite == 'r':
            print(self.userBlog)
            print("Here your post: ")

        elif readOrWrite == 'W' or readOrWrite == 'w':
            self.userBlog.newPost()

        else:
            listPost = Database.DATABASE['post'].find({})
            for post in listPost:
                print(post)