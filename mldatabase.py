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

# https://newsapi.org/ News API key
newsAPIKey = "0054e75e6de34f2289c02f5520bddea5"

# News sources IDs
associatedPressID = "associated-press"
bbcNewsID = "bbc-news"
bloombergID = "bloomberg"
businessInsiderID = "business-insider"
cnbcID = "cnbc"
newsweekID = "newsweek"
reutersID = "reuters"
huffingtonPostID = "the-huffington-post"
newYorkTimesID = "the-new-york-times"
wallStreetJournalID = "the-wall-street-journal"
washingtonPostID = "the-washington-post"
timeID = "time"
usaTodayID = "usa-today"

sources = [associatedPressID, bbcNewsID, bloombergID, businessInsiderID, cnbcID, newsweekID, reutersID, huffingtonPostID, newYorkTimesID, wallStreetJournalID, washingtonPostID, timeID, usaTodayID]

# Writing to Articles
for source in sources:
	data = requests.get("https://newsapi.org/v1/articles?source=" + source + "&sortBy=top&apiKey=" + newsAPIKey)
	articles = data.json()['articles']
	for a in articles:
		db.child("articles").push(a)

# Add allSources
# sources: list of Strings
def addAllSources(sources):
	db.child("allSources").set(sources)

# Add allTopics
# topics: list of Strings
def addAllTopics(topics):
	db.child("allTopics").set(topics)

# Clear All Articles
def clearAllArticles():
	db.child("articles").remove()

# Write an Article
# dictionary: dictionary of article data
def writeAnArticle(dictionary):
	db.child("articles").push(dictionary)
