# -*- coding: utf-8 -*-
import re
import sys
import requests
from lxml.html import fromstring
from urlobject import URLObject
from dateutil.parser import parse as parse_date
from mongoengine import connect

sys.path.append('..')
from models import Story


COLLECTION_NAME = 'relatoseroticos_es_v1'
BASE_URL = 'http://www.relatoseroticos.es/nuevos_relatos.php'


class Scraper(object):
    def __init__(self, *args, **kwargs):
        self.session = requests.Session()

    def scrape(self):
        home_req = self.session.get(BASE_URL)
        home_html_tree = fromstring(home_req.content)
        num_pages_el = home_html_tree.cssselect('.nonselec a')[-1]
        num_pages = int(num_pages_el.text)
        insert_story = lambda s: Story.objects.get_or_create(**s) if s else None
        for num_page in xrange(1, num_pages + 1):
            stories_urls = self.__parse_page(num_page)
            map(insert_story,
                map(self.__parse_story,
                    stories_urls))

    def __parse_page(self, num_page):
        page_url = '%s?pag=%d' % (BASE_URL, num_page)
        page_req = self.session.get(page_url)
        page_html_tree = fromstring(page_req.content)
        stories_el = page_html_tree.cssselect('.detalles a')
        stories_urls = [story_el.attrib['href'] for story_el in stories_el]
        return stories_urls

    def __get_story_id(self, story_url):
        url_obj = URLObject(story_url)
        if url_obj.path.segments:
            story_id = url_obj.path.segments[-1].split('_')[1].strip('.html')
            return int(story_id)

    def __parse_story(self, story_url):
        print story_url
        normalize = lambda x: x.strip(' \t\n\r').encode('utf-8')
        story_id = self.__get_story_id(story_url)
        if story_id:
            story_req = self.session.get(story_url)
            if story_req.ok:
                story_html_tree = fromstring(story_req.content)
                story_title_el = story_html_tree.cssselect('.usuario')[0]
                story_title = normalize(story_title_el.text_content())
                story_author_el = story_html_tree.cssselect('.email')[0]
                story_author = normalize(story_author_el.text_content())
                story_date_el = story_html_tree.cssselect('.bg_medio span')[0]
                story_date = parse_date(story_date_el.text_content(), fuzzy=True, dayfirst=True)
                story_category_el = story_html_tree.cssselect('.bg_medio span a')[0]
                story_category = URLObject(story_category_el.attrib['href']).path.segments[0]
                story_text_opc_el = story_html_tree.cssselect('.tx_opc')[0]
                story_text_opc = normalize(story_text_opc_el.text_content())
                story_content_el = story_html_tree.cssselect('.bg_medio p')[0]
                story_content = normalize(story_content_el.text_content())
                story_average_votes_el = story_html_tree.cssselect('.star')
                story_average_votes = float(story_average_votes_el[0].text_content())
                story_num_votes_el =story_html_tree.cssselect('.opciones_relato div')[-2]
                story_data = map(int, re.findall(r'\d+', story_num_votes_el.text_content()))
                story_visits = story_data[0]
                story_num_votes = story_data[1]
                story = {
                    'uid': story_id,
                    'url': story_url,
                    'title': story_title,
                    'author': story_author,
                    'date': story_date,
                    'category': story_category,
                    'text_opc': story_text_opc,
                    'content': story_content,
                    'votes_average': story_average_votes,
                    'num_votes': story_num_votes,
                    'visits': story_visits
                }
                return story


if __name__ == '__main__':
    connect(COLLECTION_NAME)
    sc = Scraper().scrape()
