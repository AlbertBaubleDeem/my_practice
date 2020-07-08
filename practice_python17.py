import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features="html.parser")
readable = soup.decode(pretty_print=True)

title = soup.find_all(name='h2')
title_t = []
for i in range(len(title)):
    title_t.append(title[i].text)

for i in range(len(title_t)):
    print(title_t[i])

print(len(title_t))