#!/usr/bin/python3
from flask import Flask, jsonify, request, abort
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


@app.route('/images', methods=['POST'])
def create_image():
    if not request.json or 'filename' not in request.json or 'time' not in request.json:
        abort(400)
    filename = request.json['filename']
    seconds = request.json['time']
    image = {
        'filename': filename,
        'time': seconds,
    }
    images_dao.save_or_update(filename, seconds)
    return jsonify({'image': image}), 201


@app.route('/detections')
def get_detections():
    return jsonify(detections_dao.get_last_detections())


@app.route('/detections', methods=['POST'])
def create_detection():
    if not request.json or 'filename' not in request.json or 'objecttypeid' not in request.json:
        abort(400)
    filename = request.json['filename']
    object_type = request.json['objecttypeid']
    bounding_box = request.json.get('boundingbox', '')
    id = detections_dao.save_or_update(filename, object_type, bounding_box)
    detection = {
        'id': id,
        'filename': filename,
        'objecttypeid': object_type,
        'boundingbox': bounding_box,
    }
    return jsonify({'detection': detection}), 201


@app.route('/connections')
def get_connections():
    return jsonify((wlan_dao.get_all_connections()))


@app.route('/connections', methods=['POST'])
def create_connection():
    if not request.json or 'ip' not in request.json or 'time' not in request.json:
        abort(400)
    mac = request.json.get('mac','')
    time = request.json['time']
    ip = request.json['ip']
    description = request.json.get('description', '')
    wlan_dao.save_or_update(ip, mac, time, description)
    connection = {
        'ip': ip,
        'mac': mac,
        'time': time,
        'description': description
    }
    return jsonify({'connection': connection}), 201


if __name__ == '__main__':
    app.run(debug=True, port=80, host=host)
