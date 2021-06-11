"""
This program creates the routes for the view (web application) and provides communication
between view and model (MongoDB database)
Author: Group5 members
Course: CST8276 - Spring2021
Date: 03/06/2021
Version: 1.0
"""
from flask import Flask
from flask import render_template, request, jsonify
from controller import restaurant_search
import bson.json_util as bson

app = Flask(__name__, template_folder="../view/templates")


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/", methods=["GET", "POST"])
def restaurant_finder_html_form():
    restaurant_name = request.form['restaurantName']
    if restaurant_name != "":
        restaurant_prepared_statement = {"name": restaurant_name}
        results = restaurant_search.find_many_by_name(restaurant_prepared_statement)
        if len(results) == 0:
            results = {"Response": 0}
    return jsonify(results)


@app.route("/api/restaurants/", methods=["GET", "POST"])
def restaurant_finder():
    restaurant_name = request.args.get("name")
    if restaurant_name != "":
        restaurant_prepared_statement = {"name": restaurant_name}
        results = restaurant_search.find_many_by_name(restaurant_prepared_statement)
        if len(results) == 0:
            results = {"Response": 0}
    return jsonify(results)


def start_server(host_ip, debug_mode):
    app.run(host=host_ip, debug=debug_mode)
