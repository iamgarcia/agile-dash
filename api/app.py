import uuid

from dotenv import dotenv_values
from flask import Flask, request, jsonify
from pymongo import MongoClient
import bcrypt


app = Flask(__name__)

config = dotenv_values('.env')

client = MongoClient(config['ATLAS_URI'])
db = client[config['DB_NAME']]
users = db[config['COL1_NAME']]
projects = db[config['COL2_NAME']]


@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    user = users.find_one({'email': data['email']})

    if user is None:
        # Hash the user's password.
        encoded_pw = data['password'].encode()
        hashpw = bcrypt.hashpw(encoded_pw, bcrypt.gensalt())

        # Replace the user's string password with the hashed password.
        data['password'] = hashpw

        # Insert the document into the users collection.
        users.insert_one(data)

        return 'Account was successfully created.', 200

    return 'This email address is already in use.', 401


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users.find_one({'email': data['email']})

    if user:
        encoded_pw = data['password'].encode()

        if bcrypt.checkpw(encoded_pw, user['password']):
            # Generate a session ID.
            session_id = str(uuid.uuid4())

            # Add the session ID to the user.
            user['session_id'] = session_id

            # Create query that matches the user document to update.
            filter = {'_id': user['_id']}

            # The modifications to apply to the user document.
            new_values = {'$set': {'session_id': user['session_id']}}

            # Update the user document that matches the filter with
            # the modifications.
            users.update_one(filter, new_values)

            res = {
                'status_code': 200,
                'message': 'Login successful.',
                'session_id': user['session_id'],
                'user_id': str(user['_id'])
            }

            return jsonify(res)

    res = {
        'status_code': 400,
        'message': 'Please provide a valid email address and password.',
        'session_id': None,
        'user_id': None
    }

    return jsonify(res)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
