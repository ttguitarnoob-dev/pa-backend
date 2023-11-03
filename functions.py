import psycopg2
from flask import jsonify
import psycopg2.extras



def itwork():
    print('smelllyworks ya')

#Database Connection
def get_db_connection():
    conn = psycopg2.connect(
        host="10.24.24.218",
        database = "paguitars",
        user= "postgres",
        password= "Bungfodder123")
    return conn






#Fetch all
def handle_fetch():
    print('fetching all')
    db = get_db_connection()
    cur = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute('SELECT * FROM guitars;')
    guitar_data = cur.fetchall()
    cur.close()
    db.close()
    return jsonify(guitar_data)

#Fetch one by id
def handle_fetch_one(id):
    print(f"fetching guitar {id}")
    db = get_db_connection()
    cur = db.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    cur.execute(f"SELECT * FROM guitars WHERE id = {id} ")
    data = cur.fetchall()
    cur.close()
    db.close()
    return jsonify(data)
    
