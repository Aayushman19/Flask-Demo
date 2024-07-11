from flask import Flask
from flask import render_template
from flask import request
import psycopg2
def get_connection():
	try:
		return psycopg2.connect(
			database="users",
			user="postgres",
			password="Postgres@1234",
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
amount = 0

@app.route('/')
def hello():
    return render_template('food.html')