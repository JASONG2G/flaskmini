from flask import Flask
from app import app # from app module import app object
from user.models import User # from user dir import User class


@app.route('/user/signup/', methods=['POST'])
def signup():
    return  User().signup()

