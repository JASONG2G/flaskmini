from flask import Flask, jsonify, request
import uuid
from passlib.hash import sha256_crypt
from app import db


class User:

    def signup(self):
        #print(request.form)

        # create the user object
        user = {
            "_id": uuid.uuid4.hex(),
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # encrypt the password
        user['password'] = sha256_crypt.encrypt(user['password'])

        # check for existing email address
        if db.user.find_one({ "email": user["email"]}):
            return jsonify({"error": " Email address already in use"}), 400
        
        if db.user.insert_one(user):
            return jsonify(user), 200

        # jsonify user and return status code 200
        return jsonify({"error": "Signup failed"}), 400