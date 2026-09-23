# Import Flask so Pyhton can act as a web server 
from flask import Flask, request, jsonify
# SQLite stores information
import sqlite3

db = sqlite3.connect("events.db")

# Create table with 3 columns
db.execute("CREATE TABLE IF NOT EXISTS events (course TEXT, title TEXT, date TEXT)")

# Save and close changes
db.commit()
db.close()

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running"

# When frontend sends a new event to /events, save it
@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json() # read data

    db = sqlite3.connect("events.db")

    db.execute("INSERT INTO events (course, title, date) VALUES (?, ?, ?)", (data["course"], data["title"], data["date"]))               
               
    # Save new row and close database
    db.commit()
    db.close()

    # test
    return "Event saved"

# Send back data
@app.route("/events", methods=["GET"])
def get_events():

    db = sqlite3.connect("events.db")

    rows = db.execute("SELECT course, title, date FROM events").fetchall()

    db.close()

    events = []
    for row in rows:
        events.append({"course": row[0], "title": row[1], "date":row[2]})

    return jsonify(events)