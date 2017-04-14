import pyrebase
import requests
import json
from pprint import pprint


config = {
	"apiKey": "AIzaSyAglITviKSqyNKQYDc3nhZRgT3idcyoQa4",
    "authDomain": "news-aggregator-e71a5.firebaseapp.com",
    "databaseURL": "https://news-aggregator-e71a5.firebaseio.com",
    # "projectId": "news-aggregator-e71a5",
    "storageBucket": "news-aggregator-e71a5.appspot.com",
    "serviceAccount": "news-aggregator-e71a5-firebase-adminsdk-1txak-bb3a09d80b.json"

    # messagingSenderId: "876871468874"
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

for source in sources:
	data = requests.get("https://newsapi.org/v1/articles?source=" + source + "&sortBy=top&apiKey=" + newsAPIKey)
	db.child("news").child(source).set(data.json())


