from bs4 import BeautifulSoup
import requests

def get_informations(url):

    html_res = requests.get(url).text

    soup = BeautifulSoup(html_res, "html.parser")

    for spans in soup.findAll('h1', attrs={'class' : 'title'}) :
        movieTitle = spans.text.strip()

    for spans in soup.findAll('span'):

        if "min" in spans.text.strip():
            duration = spans.text.strip()
    fDuration = ''.join(c for c in duration if c.isdigit())

    for spans in soup.findAll(itemprop="image"):
        poster = spans["src"]

    return [movieTitle, fDuration, poster]

