import json
import pymongo


def save_to_file(data, filename):
    """
    Save results to a local JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def save_to_mongo(data, mongo_uri):
    """
    Save results to a MongoDB collection.
    """
    
    client = pymongo.MongoClient(mongo_uri)
    db = client["crawler_db"]
    collection = db["crawl_results"]
    collection.insert_one(data)

