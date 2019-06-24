from pymongo import MongoClient
import os
import urllib.parse

client = MongoClient(
    os.environ.get("MONGO_PROTO")
    + os.environ.get("MONGO_USER")
    + urllib.parse.quote_plus(
        os.environ.get("MONGO_PASS"))
    + os.environ.get("MONGO_STRING"))
db = client['file_manager']
collection = db['files']
