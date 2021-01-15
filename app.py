from flask import Flask, render_template
# from dotenv import load_dotenv
from pymongo import MongoClient
# load_dotenv()
import os

app = Flask(__name__)
# database
client= MongoClient("mongodb+srv://admin:admin@cluster0.jajki.mongodb.net/mydb?retryWrites=true&w=majority")
#os.getenv('MONGO_URI')
db = client.mydb
#os.getenv('DB_NAME')
# routes
# here because routes import app first.
from user import routes


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')

