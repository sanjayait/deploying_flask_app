"""
model.py
-------
Implements the model for our website by simulating a database

NOTE: although this is nice a simple example,dont do this in real-world
production setting. Having a global object for application data is asking for
trouble. Instead, use a real database layer, like
https://flask-sqlalchemy.palletsprojects.com/.
"""

import json
def loadDB():
    with open("flaskcardDB.json") as f:
        return json.load(f)

def saveDB():
    with open("flaskcardDB.json", 'w') as f:
        return json.dump(db, f)

db = loadDB()