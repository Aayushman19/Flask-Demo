from flask import Flask
from flask import render_template
from flask import request
import psycopg2
def get_connection():
	try:
		return psycopg2.connect(
			database="********",
			user="postgres",
			password="********",
			host="localhost",
			port=5432,
		)
	except:
		return False
conn = get_connection()
if conn:
	print("Connection to the PostgreSQL established successfully.")
else:
	print("Connection to the PostgreSQL encountered and error.")

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