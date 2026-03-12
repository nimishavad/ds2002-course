import os
from pymongo import MongoClient

MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():

    client = MongoClient(MONGODB_ATLAS_URL)

    db = client["bookstore"]
    authors = db["authors"]

    total = authors.count_documents({})

    print("Bookstore Author Report")
    print("----------------------")
    print(f"Total authors: {total}\n")

    for author in authors.find({}, {"name": 1, "nationality": 1}):
        print(f"Name: {author.get('name')}")
        print(f"Nationality: {author.get('nationality')}")
        print()

    client.close()


if __name__ == "__main__":
    main()
