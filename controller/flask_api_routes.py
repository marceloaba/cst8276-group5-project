"""
This program creates the routes for the view (web application) and provides communication
between view and model (MongoDB database)
Author: Group5 members
Course: CST8276 - Spring2021
Date: 23/07/2021
Version: 2.0
"""
from flask import Flask
from flask import request, jsonify
from controller import controller

app = Flask(__name__)


@app.route("/api/restaurants/", methods=["GET", "POST"])
def restaurant_finder():
    """
    This function accepts GET and POST requests, saves name of the restaurant, zip code and radius
    and calls the controller to query de database and returns a list of restaurants to the front-end
    """
    restaurant_name = request.args.get('restaurantName')
    zip_code = request.args.get('zipCode')
    radius_in_km = request.args.get('radius')

    results = controller.find_restaurants(restaurant_name, zip_code, radius_in_km)

    return jsonify(results)


def start_server(host_ip, debug_mode):
    """
    This function starts flask server to run the back-end
    :param host_ip: IP of the flask server
    :param debug_mode: Boolean to activate or not flask debug mode
    """
    app.run(host=host_ip, debug=debug_mode)
