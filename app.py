from flask import Flask
import psycopg2
from flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/')
def index():
    return "Smellass"


#Run App
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=5000, debug=True)