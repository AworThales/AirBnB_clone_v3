#!/usr/bin/python3
"""citi"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.city import City
from models.state import State
from datetime import datetime
import uuid


@app_views.route('/states/<state_id>/citi', methods=['GET'])
@app_views.route('/states/<state_id>/citi/', methods=['GET'])
def list_cities_of_state(state_id):
    '''Retrieves a list of all City objects'''
    all_stateses = storage.all("State").values()
    state_objects = [obj.to_dict() for obj in all_stateses if obj.id == state_id]
    if state_objects == []:
        abort(404)
    list_citi = [obj.to_dict() for obj in storage.all("City").values()
                   if state_id == obj.state_id]
    return jsonify(list_citi)


@app_views.route('/states/<state_id>/citi', methods=['POST'])
@app_views.route('/states/<state_id>/citi/', methods=['POST'])
def create_city(state_id):
    '''Creates a City'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    all_stateses = storage.all("State").values()
    state_objects = [obj.to_dict() for obj in all_stateses if obj.id == state_id]
    if state_objects == []:
        abort(404)
    citi = []
    fresh_city = City(name=request.json['name'], state_id=state_id)
    storage.new(fresh_city)
    storage.save()
    citi.append(fresh_city.to_dict())
    return jsonify(citi[0]), 201


@app_views.route('/citi/<city_id>', methods=['GET'])
def get_city(city_id):
    '''Retrieves a City object'''
    all_cities = storage.all("City").values()
    city_objects = [obj.to_dict() for obj in all_cities if obj.id == city_id]
    if city_objects == []:
        abort(404)
    return jsonify(city_objects[0])


@app_views.route('/citi/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    '''Deletes a City object'''
    all_cities = storage.all("City").values()
    city_objects = [obj.to_dict() for obj in all_cities if obj.id == city_id]
    if city_objects == []:
        abort(404)
    city_objects.remove(city_objects[0])
    for obj in all_cities:
        if obj.id == city_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/citi/<city_id>', methods=['PUT'])
def updates_city(city_id):
    '''Updates a City object'''
    all_cities = storage.all("City").values()
    city_objects = [obj.to_dict() for obj in all_cities if obj.id == city_id]
    if city_objects == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    city_objects[0]['name'] = request.json['name']
    for obj in all_cities:
        if obj.id == city_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(city_objects[0]), 200
