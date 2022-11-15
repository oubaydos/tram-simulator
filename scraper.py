import codecs

import requests
from bs4 import BeautifulSoup


def scrape(line: str) -> list:
    url = f"https://www.tag.fr/ftp/fiche_horaires/fiche_horaires_2014/PARCOURS_{line.upper()}.HTML"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    selected = soup.select("body > p > ul > li")
    temp = [str(i.text)[str(i.text).index(" ") + 1:] for i in selected]
    res = []
    for i in temp:
        if i not in res:
            res.append(i)
    return res


print(scrape("A"), scrape("B"), scrape("C"), scrape("D"), scrape("E"), file=open('output.txt', 'w'), sep="\n")
