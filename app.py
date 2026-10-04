from flask import Flask, render_template, request, redirect, url_for, jsonify
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()

app = Flask(__name__)

# MongoDB Atlas connection
MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["assignment_db"]
collection = db["students"]


# -------------------------------
# Question 1: API Route
# -------------------------------

@app.route("/api")
def api():

    with open("backend/data.json", "r") as file:
        data = json.load(file)

    return jsonify(data)


# -------------------------------
# Question 2: Frontend Form
# -------------------------------

@app.route("/", methods=["GET", "POST"])
def form():

    error = None

    if request.method == "POST":

        try:
            name = request.form.get("name")
            email = request.form.get("email")
            course = request.form.get("course")

            data = {
                "name": name,
                "email": email,
                "course": course
            }

            collection.insert_one(data)

            return redirect(url_for("success"))

        except Exception as e:
            error = str(e)

    return render_template("form.html", error=error)


# -------------------------------
# Success Page
# -------------------------------

@app.route("/success")
def success():
    return render_template("success.html")


# -------------------------------
# Run Flask
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)