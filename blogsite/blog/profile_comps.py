from http.client import REQUEST_URI_TOO_LONG
import requests


def get_quote() -> tuple:
    response = requests.get("http://zenquotes.io/api/quotes")
    data = response.json()[0]
    author = data['a']
    quote = data['q']
    return quote, author
