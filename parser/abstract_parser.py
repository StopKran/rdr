__author__ = 'stopkran'

from BeautifulSoup import BeautifulSoup


"""abstract parser"""

class abstract_parser:

    content_url_pattern = "www.aaa.ru/"

    def parse_content_page(raw_page, container):
        return container

    def parse_digest_page(raw_page, url_pattern):
        urls = []
        return urls