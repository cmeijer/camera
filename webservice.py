#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask_cors import CORS

import detections_dao
import images_dao
import wlan_dao
from settings import webservice_host as host

"""
This is a webservice for storing and retrieving information about observations.
/images

/detections


tables:
- images                [filename.jpg, datetime]

- detections            [id, filename.jpg, objecttypeid, boundingbox]

- devices               [mac, description]

- connections           ['ip', mac_column, time_column, 'description']
"""

app = Flask(__name__)
CORS(app)


@app.route('/images')
def get_images():
    return jsonify(images_dao.get_all_images())


@app.route('/detections')
def get_detections():
    return jsonify(detections_dao.get_last_detections())


@app.route('/connections')
def get_connections():
    return jsonify((wlan_dao.get_all_connections()))


if __name__ == '__main__':
    app.run(debug=True, port=80, host=host)
