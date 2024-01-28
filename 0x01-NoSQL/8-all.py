#!/usr/bin/env python3
"""
 Python function that lists all documents in a collection
"""
def list_all(mongo_collection):
    docs =  mongo_collection.find()  # Find returns a cursor object
    for doc in docs:
        # Iterate over the cursor to get each document
        return doc