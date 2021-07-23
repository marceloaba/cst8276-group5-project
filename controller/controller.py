"""
This program uses model.py module to connect to a Mongodb Atlas cluster and retrieves data
from a MongoDB database.
Author: Group5 members
Course: CST8276 - Spring2021
Date: 23/05/2021
Version: 2.0
"""
from model import model
from geopy.geocoders import Nominatim

# Defining database and collection name to connect to mongodb cluster
database_name = "restaurants_db"
collection_name = "restaurants"
credentials_file = "/../credentials.pwd"
# Connect to mongodb with mongodb module
client = model.connect_to_database(database_name, credentials_file)
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

    return restaurant_list


def geopy_find_coordinates(zip_code):
    """
    This method finds the coordinates (latitude and longitude) of a zip code using GeoPy
    :param zip_code: Zip code used to search the coordinates by GeoPy
    """

    if zip_code != '':
        geo_locator = Nominatim(user_agent='myapplication')
        coordinates = geo_locator.geocode(zip_code, country_codes="US")
        # If geopy cannot find the coordinates for the zip code we set a default zipcode from Manhattan New York
        if coordinates is None:
            coordinates = geo_locator.geocode("10019", country_codes="US")
            return coordinates
        else:
            return coordinates


def find_restaurants(restaurant_name, zip_code, radius_in_km):
    """
    This method finds all documents using restaurant name, radius near lat and lon
    :param restaurant_name: Name of the restaurant Ex: {"name": "Wendy'S"}
    :param radius_in_km: Radius in km used to find restaurants
    :param zip_code: Zipcode used by GeoPy to discover the coordinates
    """
    restaurant_list = list()
    meters_per_km = 1000
    maximum_distance_in_meters = int(radius_in_km) * meters_per_km
    coordinates = geopy_find_coordinates(zip_code)
    lat = coordinates.raw['lat']
    lon = coordinates.raw['lon']

    if restaurant_name == '':
        restaurants = model.query_restaurants_by_location(collection, maximum_distance_in_meters, lat, lon)
    else:
        restaurants = model.query_restaurants_by_name_and_location(collection, restaurant_name, maximum_distance_in_meters, lat, lon)

    # Loop through the cursor and print each restaurant found and prints
    for restaurant in restaurants:
        restaurant_list.append(restaurant)
        print(restaurant)

    return restaurant_list

