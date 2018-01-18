# /usr/bin/env python3

from bs4 import BeautifulSoup
import requests

COUNT = 1000

filename = "wiki.txt"

with open(filename, "w") as f:
    for i in range(0, COUNT):
        print(i)
        respond = requests.get("https://simple.wikipedia.org/wiki/Special:Random")
        soup = BeautifulSoup(respond.text, "html.parser")
        l = soup.find_all('p')
        f.write((l[0].text))
