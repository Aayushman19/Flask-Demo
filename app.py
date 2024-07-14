from flask import Flask
from flask import render_template
from flask import request
import psycopg2

app = Flask(__name__)
def get_connection():
	try:
		return  psycopg2.connect(
			database="users",
			user="postgres",
			password="Postgres@1234",
			host="localhost",
			port=5432,
		)
	except:
		return False

@app.route('/')
def hello():
	conn = get_connection()
	if conn:
		return f"Connection established Successfully"
	else:
		return f"Unable to Connect"