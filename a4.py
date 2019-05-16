import json
import os
import pymongo

with open("a.json", "r") as read_file:
    data = json.load(read_file)


data = json.dumps(data, indent=2)
print(data)
print('\n'*2)

db.createcollection(cat)

#mid = cat.insert(data)

