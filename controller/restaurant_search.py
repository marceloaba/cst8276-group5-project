"""
This program uses mongodb.py module to connect to a Mongodb Atlas cluster and retrieves data
from a MongoDB database.
Author: Group5 members
Course: CST8276 - Spring2021
Date: 23/05/2021
Version: 2.0
"""
# Import connect_to_mongo function from mongodb module
from flask import jsonify

from controller import flask_routes
from model.mongodb import connect_to_mongodb


# Defining database and collection name to connect to mongodb cluster
database_name = "restaurants_db"
collection_name = "restaurants"
credentials_file = "/../credentials.pwd"
# Connect to mongodb with mongodb module
client = connect_to_mongodb(database_name, credentials_file)
# Defining database to work with
db = client[database_name]
# Defining collection to work with
collection = db[collection_name]


def find_one_by_name(restaurant_name):
    """
    This method finds the first document in the database that has the restaurant
    :param restaurant_name: Name of the restaurant Ex: {"name": "Wendy'S"}
    """
    # Finds ONLY the first document with restaurant name and prints
    restaurant = collection.find_one(restaurant_name)
    print(restaurant)


def find_many_by_name(restaurant_name):
    """
    This method finds ALL documents in the database that has restaurant name
    :param restaurant_name: Name of the restaurant Ex: {"name": "Wendy'S"}
    """
    # Finds all documents with restaurant name
    results = collection.find(restaurant_name, {"_id": 0})
    restaurant_list = list()
    # Loop through the cursor and print each restaurant found and prints
    for restaurant in results:
        restaurant_list.append(restaurant)
        # print(restaurant)

    return restaurant_list