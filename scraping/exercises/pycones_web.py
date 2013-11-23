# -*- coding: utf-8 -*-
import pprint
import requests
from bs4 import BeautifulSoup


url = 'http://2013.es.pycon.org'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')

clean_str = lambda s: s.encode('utf-8').strip()

pretty_soup = soup.prettify()
# print clean_str(pretty_soup)

title = soup.title.string
# print clean_str(title)

urls = set([str(link.get('href')) for link in soup.find_all('a')])
# print urls

twitter_handles = filter(lambda l: 'twitter' in l, urls)
# pprint.pprint(twitter_handles)

informacion = soup.find(id='informacion')
# print clean_str(informacion.get_text())

titles = [title.string for title in soup.find_all('span', 'paper-title')]
# pprint.pprint(titles)
