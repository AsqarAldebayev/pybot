import sqlite3
from sqlite3 import Error
from time import sleep, ctime

def post_sql_query(sql_query):
	with sqlite3.connect('user_info.db') as connection:
		cursor = connection.cursor()
		try:
			cursor.execute(sql_query)
		except Error:
			pass
		result = cursor.fetchall()
		return result

def create_tables():
	users_query = '''CREATE TABLE IF NOT EXISTS INFORM
						(user_id INTEGER PRIMARY KEY NOT NULL,
						user_name TEXT,
						username TEXT,
						reg_date TEXT);'''
	post_sql_query(users_query)


def register_user(u_id, user_name, username):
	user_check_query = f'SELECT * FROM INFORM WHERE user_id = {u_id};'
	user_check_data = post_sql_query(user_check_query)
	if not user_check_data:
		insert_to_db_query = f'INSERT INTO INFORM (user_id, user_name, username, reg_date) VALUES ({u_id}, "{user_name}", "{username}", "{ctime()}");'
		post_sql_query(insert_to_db_query )


create_tables()


def show_data():
	for row in post_sql_query("SELECT * FROM inform ORDER BY user_id"):
		print(row)