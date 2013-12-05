import page_downloader
from page_container import page_container
from parsers.habrahabr import parser


__author__ = 'stopkran'


"""
url = "http://habrahabr.ru/post/202406/"

tmp_raw_page = page_downloader.download_page(url)
container = page_container()
container.url = url
container.site_name = "habrahabr"
container = parser.parse_content_page(tmp_raw_page, container)

container.print_content()
"""


url = "http://habrahabr.ru/posts/top/"

tmp_raw_page = page_downloader.download_page(url)

print parser.parse_digest_page(tmp_raw_page, "abacaba")

