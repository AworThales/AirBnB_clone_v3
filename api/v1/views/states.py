#!/usr/bin/python3
"""states"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from datetime import datetime
import uuid


@app_views.route('/states/', methods=['GET'])
def list_states():
    '''Retrieves a list of all State objects'''
    list_states = [obj.to_dict() for obj in storage.all("State").values()]
    return jsonify(list_states)


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    '''Retrieves a State object'''
    all_stateses = storage.all("State").values()
    state_objects = [obj.to_dict() for obj in all_stateses if obj.id == state_id]
    if state_objects == []:
        abort(404)
    return jsonify(state_objects[0])


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    '''Deletes a State object'''
    all_stateses = storage.all("State").values()
    state_objects = [obj.to_dict() for obj in all_stateses if obj.id == state_id]
    if state_objects == []:
        abort(404)
    state_objects.remove(state_objects[0])
    for obj in all_stateses:
        if obj.id == state_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/states/', methods=['POST'])
def create_state():
    '''Creates a State'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    states = []
    fresh_state = State(name=request.json['name'])
    storage.new(fresh_state)
    storage.save()
    states.append(fresh_state.to_dict())
    return jsonify(states[0]), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def updates_state(state_id):
    '''Updates a State object'''
    all_stateses = storage.all("State").values()
    state_objects = [obj.to_dict() for obj in all_stateses if obj.id == state_id]
    if state_objects == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    state_objects[0]['name'] = request.json['name']
    for obj in all_stateses:
        if obj.id == state_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(state_objects[0]), 200
