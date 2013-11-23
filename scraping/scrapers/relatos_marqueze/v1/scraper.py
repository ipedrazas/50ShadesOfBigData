# -*- coding: utf-8 -*-
import re
import sys
import requests
from lxml.html import fromstring
from urlobject import URLObject
from mongoengine import connect
from dateutil.parser import parse as parse_date

sys.path.append('..')
from models import Story
from utils import retry


COLLECTION_NAME = 'relatos_marqueze_es_v1'
BASE_URL = 'http://relatos.marqueze.net/'
MONTHS = {
    'enero': '1',
    'febrero': '2',
    'marzo':'3',
    'abril': '4',
    'mayo': '5',
    'junio': '6',
    'julio': '7',
    'agosto': '8',
    'septiembre': '9',
    'octubre': '10',
    'noviembre': '11',
    'diciembre': '12'}
DATE_PATTERN = re.compile(r'\b(' + '|'.join(MONTHS.keys()) + r')\b')


class Scraper(object):
    def __init__(self, *args, **kwargs):
        self.session = requests.Session()

    def scrape(self):
        home_req = self.session.get(BASE_URL)
        home_html_tree = fromstring(home_req.content)
        page_element = home_html_tree.cssselect('.pagebar a')[-2]
        page_number = int(page_element.attrib['href'].split('/')[-2])
        insert_story = lambda s: Story.objects.get_or_create(**s) if s else None
        for page_num in xrange(1, page_number + 1):
            stories_urls = self.__parse_page(page_num)
            map(insert_story,
                map(self.__parse_story,
                    stories_urls))

    @retry(Exception, tries=5)
    def __parse_page(self, page_number):
        page_url = 'http://relatos.marqueze.net/page/%d/' % page_number
        print page_url
        page_req = self.session.get(page_url)
        # page_req.raise_for_status()
        if page_req.ok:
            page_html_tree = fromstring(page_req.content)
            stories_elements = page_html_tree.cssselect('.titulo a')
            stories_urls = [element.attrib['href'] for element in stories_elements]
            return stories_urls

    @retry(Exception, tries=5)
    def __parse_story(self, story_url):
        # print story_url
        normalize = lambda x: x.strip(' \t\n\r').encode('utf-8')
        url_obj = URLObject(story_url)
        slug = url_obj.path.segments[0]
        story_req = self.session.get(story_url, allow_redirects=False)
        # story_req.raise_for_status()
        if story_req.status_code == 200:
            story_html_tree = fromstring(story_req.content)
            story_element = story_html_tree.cssselect('.post-relatos')[0]
            story_header = story_element[0]
            title_element = story_header.cssselect('.titulo a')[0]
            title = normalize(title_element.attrib['title'])
            date = story_header.cssselect('.fecha')[0].text
            date_parsed_month = DATE_PATTERN.sub(lambda x: MONTHS[x.group()], date)
            parsed_date = parse_date(date_parsed_month.replace(' de ', '/'), dayfirst=True)
            author = story_header.cssselect('.autor a')[0].attrib['title']
            rating = story_element[1][-3:][2]
            rating_average = rating.cssselect('.average')
            if rating_average:
                rating_average = float(rating_average[0].text)
            else:
                rating_average = 0
            rating_votes = rating.cssselect('.votes')
            if rating_votes:
                rating_votes = int(rating_votes[0].text)
            else:
                rating_votes = 0
            # drop ratings
            map(lambda e: e.drop_tree(), story_element[1][-3:])
            content = normalize(story_element[1].text_content())
            categories_elements = story_element.cssselect('.post-categories li a')
            categories = [e.attrib['href'].split('/')[-2] for e in categories_elements]
            tags_elements = story_element.cssselect('.post-tags a')
            tags = [e.attrib['href'].split('/')[-2] for e in tags_elements]
            story = {
                'slug': slug,
                'title': title,
                'date': parsed_date,
                'url': story_url,
                'author': author,
                'content': content,
                'num_votes': rating_votes,
                'votes_average': rating_average,
                'categories': categories,
                'tags': tags,
            }
            return story


if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    connect(COLLECTION_NAME)
    sc = Scraper().scrape()
