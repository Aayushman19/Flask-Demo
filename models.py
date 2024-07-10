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


curr = conn.cursor()
curr.execute("select * from user_login")

data = curr.fetchall()

print(data)