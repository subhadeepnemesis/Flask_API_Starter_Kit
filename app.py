import os
import json
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///essenvia_data.sqlite'

db = SQLAlchemy(app)

class Title(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(250), nullable=True)

    def __repr__(self):
        return '<Description %r>' % self.description


@app.route('/')
def home():
    return "Test Get Set"


@app.route('/get_data', methods=['GET'])
def handle_get_data():

    resp_data = []

    try:
        title_records = Title.query.all()

        for record in title_records:
            test_dict = dict()
            test_dict["desc"] = record.description
            resp_data.append(test_dict)

        response = jsonify(success=True, data=resp_data)

    except Exception as e:
        print("Error while fetching title records: "+str(e))
        response = jsonify(success=False, msg="Error while fetching data. " + str(e))
    
    return response


@app.route('/set_data', methods=['POST'])
def handle_set_data():

    try:
        request_data = request.get_json(force=True)
        desc = request_data["desc"]

        title_record = Title(
            description=desc
        )

        db.session.add(title_record)
        db.session.commit()
        response = jsonify(success=True, msg="Record added successfully.")

    except Exception as e:
        print("Error while reading request data. " + str(e))
        response = jsonify(success=False, msg="Error while reading request data. " + str(e) + " seems to be missing.")
    
    return response


if __name__ == '__main__':
    db.create_all()

    app.run(host='0.0.0.0', port=5000, debug=True)
