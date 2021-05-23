# Database project Group5
Using MongoDB with Python (web catalog, or similar application)

## Instructions
Before run any Python module for this file do the following steps:
- `Read the next section first`
- `Install all dependencies with pip`
- `Create the credentials files in the root folder`


## Python Modules in the project
- **`mongodb.py`**: This module is used by other modules of the project to connect with the MongoDB database and returns the MongoClient object to retrieve or insert data.
- **`main.py`**: This file if the main module used to query data form the database collection.
- **`insert_restaurants_data.py`**: This module reads from a JSON file inside the collections directory that contains all documents/data to be inserted in the collection.
- **`collections/`**: This directory contains all JSON file with the data to be inserted in the database 
- **`collections/restaurant.json`**: This files contains all data/documents used to populate the collection in the restaurants database.
- **`credentials.pwd`**: This file contains the username and password in clear text to be used to connect to the MongoDB atlas cloud cluster.
- **`requirements.txt`**: This file contains all dependencies that need to be installed before running the program.

## Installing dependencies
Use the package manage pip to install all dependencies from the project using the requirement.txt file. The file should have at least the following dependencies to connect to a MongoDB database:
- dnspython
- pymongo
```bash
 pip install -r requirements.txt
```

## Create the credentials file in the root folder
The credentials files contains the username and password to connect to the MongoDB database. The **`first line`** of the document is the **`username`** and the **`second line`** is the **`password`**, see example below:
- **File name:** `credentials.pwd`
```bash
clark.kent
Kryptonite
```
**`Don't worry, the credentials file should NOT sync with the GitHub repository. To make sure check if .gitignore file contains an exclusion for all files with .pwd extension.`**
## How to query data from the Restaurants collection
Check the last lines of the **`main.py`** module to change what you want to query. The example below is already in the **`main.py`** to be tested:
```bash
# This is a dictionary used to search restaurants by name "Wendy'S"
restaurants = {"name": "Wendy'S"}

# This line of code searches for only the first line that matches the name "Wendy'S" from the dictionary
find_one_restaurant_by_name(restaurants)

# This line of code can be used to search all documents form the collection that matches the name "Wendy'S"
find_restaurant_by_name(restaurants)
```