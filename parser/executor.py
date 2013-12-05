import hashlib
from pymongo import Connection
from config import config
import page_downloader
from parsers.habrahabr.parser import parser

__author__ = 'stopkran'

def get_parser_json(parser_name, db):
    descriptor_json = db.descriptors.find({"name": parser_name})[0]
    return descriptor_json


def execute(parser_name):
    connection = Connection(config.server_url, config.port)
    db = connection[config.db_name]

    parser_json = get_parser_json(parser_name, db)
    import_string = "from parsers." + parser_json["path"] + "." + parser_json["file_name"] + " import " + parser_json["class_name"]
    exec import_string
    digest_page = page_downloader.download_page("http://habrahabr.ru")
    posts = parser.parse_digest_page(digest_page)


    for post_url in posts:
        post_hash = hashlib.md5(post_url).hexdigest()
        post_cursor = db.habrahabr.find({"_id":post_hash})
        if post_cursor.count() < 1:
            page_json = parser.parse_content_page(page_downloader.download_page(post_url))
            page_json["_id"] = post_hash
            db.habrahabr.save(page_json)




execute("habrahabr")