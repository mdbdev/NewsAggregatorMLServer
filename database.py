import pyrebase
import requests
import json
from pprint import pprint


config = {
	"apiKey": "AIzaSyAZcr4Y7dS97h_ZJ1aCyl2JEUyRecYkhEM",
    "authDomain": "newsnowtest.firebaseapp.com",
    "databaseURL": "https://newsnowtest.firebaseio.com",
    "storageBucket": "newsnowtest.appspot.com",
    "serviceAccount": "newsnowtest-firebase-adminsdk-r2185-e476e5c430.json"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Add all sources
# sources: list of Strings
def setSources(sources):
	db.child("allSources").set(sources)

# Add all topics
# topics: list of Strings
def setTopics(topics):
	db.child("allTopics").set(topics)

# Clear all articles
def clearAllArticles():
	db.child("articles").remove()

# Write an article
# dictionary: dictionary of article data
def addArticle(dictionary):
	db.child("articles").push(dictionary)
