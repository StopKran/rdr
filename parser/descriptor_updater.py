import json
import hashlib
from config import config
from pymongo import Connection

__author__ = 'stopkran'


path = "parsers/habrahabr/descriptor.json"


fin = open(path, "r")
loading_json = json.loads(fin.read())

loading_json["_id"] = hashlib.md5(loading_json["name"]).hexdigest()

connection = Connection(config.server_url, config.port)
db = connection[config.db_name]
db.descriptors.save(loading_json)




