from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)
food_orders = []

@app.route('/')
def hello():
    return render_template("food.html", message = "Order Now!")

@app.route("/order", methods = ['POST'])
def order():
    food = request.form["food"]
    food_orders.append(food)
    return f"Your {food} is ready!"

@app.route('/bill', methods = ['GET'])
def bill():
    return food_orders