__author__ = 'stopkran'

import urllib


def download_page(url):
    return urllib.urlopen(url).read()