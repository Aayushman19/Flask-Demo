from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
food_orders = []

@app.route('/')
def hello():
    return render_template("food.html")

@app.route("/bill", methods = ['POST'])
def bill():
    food = request.form["food"]
    food_orders.append(food)
    return render_template("bill.html", orders = food_orders)