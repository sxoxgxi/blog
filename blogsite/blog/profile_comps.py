import requests
import random


random_comments = ["Wow thats some nice stuff", "this is some nice stuff",
                   "Thanks for sharing", "you helped me a lot", "nice blog ❤️😍", "cool 😎😎"]


def get_quote() -> tuple:
    """Gets a quote from zenquotes

    Returns:
        tuple: Contains a random quote and the quote's author name
    """
    response = requests.get("http://zenquotes.io/api/quotes")
    data = response.json()[0]
    author = data['a']
    quote = data['q']
    return quote, author


def random_comment() -> str:
    return random.choice(random_comments)
