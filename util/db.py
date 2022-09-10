from pymongo import MongoClient


def get_mongo_client(conf):
    mongo_url = conf["db"]["mongo"]["url"]
    return MongoClient(mongo_url)
