import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

WORDS_RETURN = 10


def stream_crawl_most_common_words(url, num_words=WORDS_RETURN, exclude=None):
    """
    :param url (str): The URL of the webpage from which to extract text.
    :param num_words: (int, optional): The number of most common words to return. The default value is set via Config.WORDS_RETURN.
    :param exclude: (list of str, str, or optional):
        A list of words to exclude from the analysis.
        This can help in removing common but unimportant words (e.g., "the", "and").
        If None, no words are excluded. The default value is None.
        str input is also acceptable in python str is also considered a list
    :return: list of (str, int) tuples:
     Returns a list where each tuple contains a word and its corresponding count,
     sorted by frequency in descending order.

    :Raises:
    HTTPError: If the request to the URL fails
    (e.g., network problem, invalid URL, HTTP error status codes like 404, 500, etc.).

    """
    # Validate and prepare the exclude list
    if exclude is None:
        exclude = set()
    elif isinstance(exclude, list):
        exclude = set(exclude)

    # Fetch the content from the URL
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad requests

    # Use BeautifulSoup to extract text
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()

    # Use regular expressions to split the text into words
    words = re.findall(r'\w+', text.lower())

    # Filter out the excluded words
    words = [word for word in words if word not in exclude]

    # Count the words and return the most common ones
    counter = Counter(words)
    most_common = counter.most_common(num_words)

    return most_common
