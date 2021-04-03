import requests
from bs4 import BeautifulSoup


def search(soup, tag, identifier, desc):
    event_found = soup.findAll(tag, {identifier: desc})
    return event_found