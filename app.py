from flask import Flask, request
import psycopg2
from flask_cors import CORS
from functions import *


#Init App
app = Flask(__name__)
CORS(app)
itwork()

#ROUTES

#Home
@app.route('/')
def home():
    return "Welcome Home"

#Guitars Index
@app.route('/guitars')
def guitars():
    data = handle_fetch()
    return data

#Show
@app.route('/guitars/<id>')
def guitar(id):
    id = id
    data = handle_fetch_one(id)
    return data

#Create
@app.route('/guitars', methods=["POST"])
def create_guitar():
    poo = request.get_json()
    print('nameee?', poo, int("334"))
    handle_create(poo)
    return "creaated"

#Run App
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug=True)