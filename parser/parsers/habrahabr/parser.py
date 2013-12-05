from BeautifulSoup import BeautifulSoup
from abstract_parser import abstract_parser

__author__ = 'stopkran'


"""parce habrahabr pages"""

class parser(abstract_parser):

    content_url_pattern = "habrahabr.ru/post/"
    content_page_url = "habrahabr.ru"

    @staticmethod
    def parse_content_page(raw_page):
        soup = BeautifulSoup(raw_page)
        page_json = {}
        page_json["name"] = soup.title.string
        post = soup.find("div", {"class": "content html_format"})
        page_json["content"] = post.prettify()
        tags=[tag.string for tag in soup.find("ul", {"class": "tags"}).findAll("a")]

        page_json["tags"] = tags

        return page_json

    @staticmethod
    def parse_digest_page(raw_page, url_pattern=content_url_pattern):
        soup = BeautifulSoup(raw_page)
        urls =[tag["href"] for tag in soup.findAll("a", {"class": "post_title"})]

        return urls



