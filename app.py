from flask import Flask
from flask import render_template
from flask import request
import psycopg2

app = Flask(__name__)
def get_connection():
	try:
		return psycopg2.connect(
			database="users",
			user="postgres",
			password="**********",
			host="localhost",
			port=5432,
		)
	except:
		return False

@app.route('/')
def index():
	conn = get_connection()
	if not conn:
		return f"db not connected"
	curr = conn.cursor()
	curr.execute('select * from restaurant_billing')
	orders = curr.fetchall()
	curr.execute("select count(*) from restaurant_billing")
	length = curr.fetchone()
	curr.close()
	conn.close()
	return render_template('food.html', orders = orders)
