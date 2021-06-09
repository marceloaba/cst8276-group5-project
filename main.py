"""
This program uses mongodb.py module to connect to a Mongodb Atlas cluster and retrieves data
from a MongoDB database.
Author: Group5 members
Course: CST8276 - Spring2021
Date: 23/05/2021
Version: 2.0
"""
# Import connect_to_mongo function from mongodb module
from controller import flask_routes
from controller import restaurant_search


# Run the program
if __name__ == "__main__":
    # Just a restaurant name from the database to test the query and retrieve data from collection
    restaurants = {"name": "Wendy'S"}

    # Call find_restaurant_by_name and search first restaurant with argument name
    print("Query example to find a Restaurant in the database: ")
    restaurant_search.find_one_by_name(restaurants)
    print()

    # Call find_restaurant_by_name and search all restaurant with argument name
    # restaurant_search.find_many_by_name(restaurants)

    flask_routes.start_server("127.0.0.1", True)
