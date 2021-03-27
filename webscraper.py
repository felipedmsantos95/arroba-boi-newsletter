import pandas
from getsoup import get_soup
from search_event import search

def format_text(element):
    text = element.text.title()
    return text

events = {}
titles = []
dates = []

url = "https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx"

soup = get_soup(url)
found_table = search(soup, "table", "id", "imagenet-indicador1")

print(found_table)