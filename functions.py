import psycopg2
from flask import jsonify



def itwork():
    print('smelllyworks ya')

#Database Connection
def get_db_connection():
    conn = psycopg2.connect(
        host="10.24.24.218",
        database = "paguitars",
        user= "postgres",
        password= "Bungfodder123")
    print('smtink')

    return conn
    




#Fetch all
def handle_fetch():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT json_agg(guitars) FROM guitars;')
