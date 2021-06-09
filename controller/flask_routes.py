"""
This program creates the routes for the view (web application) and provides communication
between view and model (MongoDB database)
Author: Group5 members
Course: CST8276 - Spring2021
Date: 03/06/2021
Version: 1.0
"""
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder="../view/templates")


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/restaurants")
def restaurant_finder():
    return render_template("restaurant_finder.html")


def start_server(host_ip, debug_mode):
    app.run(host=host_ip, debug=debug_mode)
