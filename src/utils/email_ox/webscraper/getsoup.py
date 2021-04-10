import requests
from bs4 import BeautifulSoup

def get_soup(url):
    html = requests.get(url)

    if html.status_code != 200:
        print(">> Falha na requisição! <<")
    else:
        html_content = html.content

    soup = BeautifulSoup(html_content, 'html.parser')

    return soup