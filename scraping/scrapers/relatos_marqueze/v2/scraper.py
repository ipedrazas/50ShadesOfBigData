import grequests
from pymongo import MongoClient
from lxml.html import fromstring
import time

# https://github.com/acdha/webtoolbox/blob/master/bin/http_bench.py
class Scraper(object):
    def scrape(self):
        home_req = self.session.get('http://relatos.marqueze.net/')
        home_html_tree = fromstring(home_req.content)
        page_element = home_html_tree.cssselect('.pagebar a')[-2]
        last_page_number = int(page_element.attrib['href'].split('/')[-2])
        pages = range(1, last_page_number + 1)
        pages_urls = ['http://relatos.marqueze.net/page/%d/' % page_number for page_number in pages]
        rs = (grequests.get(u) for u in pages_urls)
        for r in grequests.imap(rs, size=20):
            if r.ok:
                print r.url
            else:
                print 'NOOOOOOOOOOOO' * 20

        '''
        for page_num in xrange(1, last_page_number + 1):
            stories_urls = self.__parse_page(page_num)
            rs = (grequests.get(u) for u in stories_urls)
            map(self.__store_story,
                map(self.__parse_story,
                    filter(
                        lambda r: r.ok,
                        grequests.map(rs))))
        '''
    def __store_story(self, story):
        self.store.insert(story)

    def __parse_page(self, page_number):
        page_url = 'http://relatos.marqueze.net/page/%d/' % page_number
        print page_url
        page_req = self.session.get(page_url)
        time.sleep(1)
        page_html_tree = fromstring(page_req.content)
        stories_elements = page_html_tree.cssselect('.titulo a')
        stories_urls = [element.attrib['href'] for element in stories_elements]
        return stories_urls

    def __parse_story(self, story_data):
        print story_data.url
        story_html_tree = fromstring(story_data.content)
        story_element = story_html_tree.cssselect('.post-relatos')[0]
        story_header = story_element[0]
        title_element = story_header.cssselect('.titulo a')[0]
        title = title_element.attrib['title']
        canonical_url = title_element.attrib['href']
        date = story_header.cssselect('.fecha')[0].text
        # TODO: extract month and year and set them in the atts.
        month = 0
        year = 0
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
        content = story_element[1].text_content().strip()
        categories_elements = story_element.cssselect('.post-categories li a')
        categories = [e.attrib['href'].split('/')[-2] for e in categories_elements]
        tags_elements = story_element.cssselect('.post-tags a')
        tags = [e.attrib['href'].split('/')[-2] for e in tags_elements]
        story = {
            'title': title.encode('utf-8'),
            'canonical_url': canonical_url,
            'author': author,
            'date': date,
            'content': content.encode('utf-8'),
            'categories': categories,
            'tags': tags,
            'rating': {
                'average': rating_average,
                'votes': rating_votes
            }
        }
        return story


if __name__ == "__main__":
    sc = Scraper().scrape()
