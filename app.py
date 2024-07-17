from flask import Flask
from flask import render_template
from flask import request
import psycopg2
import requests

app = Flask(__name__)
def get_connection():
	try:
		return psycopg2.connect(
			database="users",
			user="postgres",
			password="",
			host="localhost",
			port=5432,
		)
	except:
		return False
	
url = "https://beverages-and-desserts.p.rapidapi.com/desserts/%7Bid%7D"

headers = {
	"x-rapidapi-key": "70eb31faa0msh7d050807db2aaa4p1212bejsnbc5a59d3a4c6",
	"x-rapidapi-host": "beverages-and-desserts.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())
	
@app.route('/')
def home():
	return render_template('home.html')

@app.route('/bill')
def index():
	conn = get_connection()
	if not conn:
		return f"db not connected"
	curr = conn.cursor()
	curr.execute('select * from restaurant_billing')
	orders = curr.fetchall()
	curr.close()
	conn.close()
	return render_template('food.html', orders = orders)
