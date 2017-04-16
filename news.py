import requests
import json

supported_sources = {"associated-press", "bbc-news", "bloomberg",
                    "business-insider", "cnbc", "newsweek", "reuters",
                    "the-huffington-post", "the-new-york-times",
                    "the-wall-street-journal", "the-washington-post",
                    "time", "usa-today"}
_news_api_key = "0054e75e6de34f2289c02f5520bddea5"

def get_article_data(sources=supported_sources):
    """Returns a list of JSON objects containing metadata about each article.

    :param set sources: The set of sources from which the function returns
    articles.
    """
    articles = []
    for source in sources:
        response = requests.get("https://newsapi.org/v1/articles?source="
                            + source + "&sortBy=top&apiKey=" + _news_api_key)
        if response.ok:
            try:
                data = json.loads(response.text)
                for article in data["articles"]:
                    article["source"] = source
                    articles.append(article)
            except json.JSONDecodeError as e:
                # TODO: handle response with invalid JSON encoding
                pass
            except KeyError as e:
                # TODO: handle if "articles" not in data
                pass
    return articles


def get_article_summary(article):
    """Given an article, returns a summary of the article using summary

    :param dict article: The metadata of the article"""
    pass
