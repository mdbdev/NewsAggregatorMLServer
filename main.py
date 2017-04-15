import news
import scoring
import database
import numpy as np


articles = news.get_article_data()

titles = [article["title"] if article["title"] else "" for article in articles]
descriptions = [article["description"] if article["description"] else ""
                for article in articles]

title_scores = scoring.calc_similarity_scores(titles)
description_scores = scoring.calc_similarity_scores(descriptions)

scores = np.sqrt(np.square(title_scores) + np.square(description_scores))

popularities = scoring.calc_popularity(scores)

for popularity, article in zip(popularities, articles):
    article["popularity"] = popularity

# Clear the database of old articles
# TODO: make this more elegant -- this briefly stop service
database.clearAllArticles()
for article in articles:
    database.addArticle(article)
