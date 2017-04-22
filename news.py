import requests
import json
from urllib.parse import urlencode

# THIS IS LEGACY CODE TODO: DELETE
supported_sources = {
    "associated-press" : "Associated Press",
    "bbc-news": "BBC News",
    "bloomberg": "Bloomberg",
    "business-insider": "Business Insider",
    "cnbc": "CNBC",
    "newsweek": "Newsweek",
    "reuters": "Reuters",
    "the-huffington-post": "Huffington Post",
    "the-new-york-times": "New York Times",
    "the-wall-street-journal": "Wall Street Journal",
    "the-washington-post": "Washington Post",
    "time": "Time",
    "usa-today": "USA Today"
}
_news_api_key = "0054e75e6de34f2289c02f5520bddea5"

def get_sources(language=None, category=None, country=None):
    """Returns list JSON objects containing information about sources.

    :param str language: Filter sources by language.
    Possible options: en, de, fr.
    Default: all sources returned.
    :param str category: Filter sources by categories.
    Possible options: business, entertainment, gaming, general, music, politics,
    science-and-nature, sport, technology.
    Default: all sources returned.
    :param str country: Only return new sources based in a particular country.
    Possible options: au, de, gb, in, it, us.
    Default: all sources returned.
    """
    # Construct the request url
    url = "https://newsapi.org/v1/sources"

    keys = ["apiKey", "sortBy", "language", "category", "country"]
    values = [_news_api_key, "top", language, category, country]
    params = {key: value for key, value in zip(keys, values) if value}

    url += "?" + urlencode(params)

    response = requests.get(url)

    sources = []
    if response.ok:
        try:
            data = json.loads(response.text)
            for source in data["sources"]:
                sources.append(source)
        except json.JSONDecodeError as e:
            # TODO: handle response with invalid JSON encoding
            pass
        except KeyError as e:
            # TODO: handle if "articles" not in data
            pass
    return sources


def get_article_data(source_ids=supported_sources):
    """Returns a list of JSON objects containing metadata about each article.

    :param set sources: The set of source ids from which the function returns
    articles.
    """
    articles = []
    for src in source_ids:
        response = requests.get("https://newsapi.org/v1/articles?source="
                            + src + "&sortBy=top&apiKey=" + _news_api_key)
        if response.ok:
            try:
                data = json.loads(response.text)
                for article in data["articles"]:
                    article["source"] = src
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
