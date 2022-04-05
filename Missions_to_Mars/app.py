from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    destination_data = mongo.db.collection.find_one()
    return render_template("index.html", mars=destination_data)


# 4. Define what to do when a user hits the /about route
@app.route("/scraper")
def scraper():
    mars_data = scrape_mars.scrape()
    mongo.db.collection.update_one({}, {"$set": mars_data}, upsert=True)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
