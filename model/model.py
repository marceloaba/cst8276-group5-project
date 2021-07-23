"""
This program connects to a MongoDB Atlas cloud cloud cluster and returns a MongoClient object
to be used by other modules.
Author: Group5 members
Course: CST8276 - Spring2021
Date: 23/07/2021
Version: 3.0
"""
# Import MongoClient from pymongo driver
from pymongo import MongoClient
import sys
import os.path

username = str()
password = str()
client = MongoClient()


def get_credentials_from_file(credentials_file):
    """
    This function reads the credentials.pwd file and save first line in the username variable
    and second line in the password variable.
    """
    # Change the scope username and password variables to global
    global username
    global password
    try:
        # Open and reads the credentials.pwd file and save the lines in the username and password
        with open(os.path.dirname(__file__) + credentials_file) as credential_file:
            credentials = credential_file.readlines()
            username = credentials[0].strip()
            password = credentials[1].strip()

            credential_file.close()
    except FileNotFoundError as error:
        print(error)
        sys.exit(1)


def connect_to_database(database, credentials_file):
    """
    This function connects to mongodb using the credentials in the credentials file
    and saves the connection in the client variable.
    """
    # Change the scope of client variable to global and calls get_credentials_from_file method
    global client
    get_credentials_from_file(credentials_file)

    # It only try to connect if user and password is not empty or it is just an empty space
    if (username and password != "") and (len(username) and len(password) > 1):
        client = MongoClient(
            f'mongodb+srv://{username}:{password}@cluster0.xmirl.mongodb.net/{database}?retryWrites=true&w=majority',
            ssl=True, ssl_cert_reqs='CERT_NONE')
    else:
        print("User name and/or password is empty, please check the credentials.pwd file")
        sys.exit(1)

    return client


def query_restaurants_by_name_and_location(collection, restaurant_name, radius, lat, lon):
    """
    This method search restaurants in the database based on name, radius and location
    :param collection: MongoDB collection used to search the restaurants
    :param restaurant_name: Name of the restaurant, it does not need to be exact
    :param radius: Max distance in meters to search restaurant around
    :param lat: Latitude of the zipcode
    :param lon: Longitude of the zipcode
    """
    results = collection.find(
        {'location': {'$nearSphere': {'$geometry': {'type': "Point",
                                                    'coordinates': [float(lon), float(lat)]},
                                      '$maxDistance': radius}},
         'name': {'$regex': restaurant_name, "$options": "i"}},
        {"_id": 0})

    return results


def query_restaurants_by_location(collection, radius, lat, lon):
    """
    This method search restaurants in the database based on radius and location when
    no name is provided.
    :param collection: MongoDB collection used to search the restaurants
    :param radius: Max distance in meters to search restaurant around
    :param lat: Latitude of the zipcode
    :param lon: Longitude of the zipcode
    """
    results = collection.find(
        {'location': {'$nearSphere': {'$geometry': {'type': "Point",
                                                    'coordinates': [float(lon), float(lat)]},
                                      '$maxDistance': radius}}}, {"_id": 0})

    return results
