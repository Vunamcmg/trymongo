from menu import Menu
from database import Database
__author__ = "Vu Hoai Nam"

try:
    Database.initialize()
except:
    print("Can't connect to database")

print("Welcome to social blog")
menu = Menu()
menu.runMenu()