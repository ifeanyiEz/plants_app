import sys
from flask import Flask, config, jsonify
from flask import render_template, request, Response, jsonify, abort
from flask import session, flash, redirect, url_for
import logging
from logging import Formatter, FileHandler, error
from models import *

logging.getLogger('flask_cors').level = logging.DEBUG

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Headers', 'GET, POST, PATCH, DELETE, OPTION')
    return response

@app.route('/plants', methods=['GET','POST'])
#@cross_origin
def get_plants():
    # Implement pagniation
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * 10
    end = start + 10

    plants = Plant.query.all()
    formatted_plants = [plant.format() for plant in plants]
    return jsonify({
        'success': True,
        'plants':formatted_plants[start:end],
        'total_plants':len(formatted_plants)
        })


@app.route('/plants/<int:plant_id>')
def get_specific_plant(plant_id):
    plant = Plant.query.filter(Plant.id == plant_id).one_or_none()
    if plant is None:
        abort(404)
    else:
        return jsonify({
            'success': True,
            'plant': plant.format()
        })


if __name__ == '__main__':
    app.run()
