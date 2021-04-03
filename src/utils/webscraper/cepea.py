import pandas
from .getsoup import get_soup
from .search_event import search

def format_text(element):
    text = element.text.title()
    return text

def format_oxvalues(data):
    return str(data/100).replace('.', ',')

events = {}
titles = []
dates = []

url = "https://www.cepea.esalq.usp.br/br/indicador/boi-gordo.aspx"

soup = get_soup(url)
found_table = search(soup, "table", "id", "imagenet-indicador1")

data_frame = pandas.read_html(str(found_table))[0]

#Data treatment
(data_frame['Valor R$*']) = [format_oxvalues(value) for value in (data_frame['Valor R$*'])]
(data_frame['Valor US$*']) = [format_oxvalues(value) for value in (data_frame['Valor US$*'])]
data_frame = data_frame.rename(columns = {'Unnamed: 0': 'Data'}, inplace = False)

#Final value
ox_table = data_frame.loc[0]




