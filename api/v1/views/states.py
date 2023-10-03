#!/usr/bin/python3
''' new view for State object_state'''

from api.v1.views import app_views
from flask import Flask
from flask import Flask, abort
from os import name
from flask import request
from models.state import State


@app_views.route('/status', methods=['GET'] strict_slashes=False)
def toGet():
    '''getting thing'''
    object_state = storage.all('State')
    list_state = []
    for state in object_state.values():
        list_state.append(state.to_dict())
    return jsonify(list_state)


@app_views.route('/states/<string:stateid>', methods=['GET'],
                 strict_slashes=False)
def toGetid():
    '''Updates a State object id'''
    object_state = storage.get('State', 'state_id')
    if object_state is None:
        abort(404)
    return jsonify(object_state.to_dict()), 'OK'


@app_views.route('/states/', methods=['POST'],
                 strict_slashes=False)
def posting():
    '''Creates a State'''
    res = request.get_json()
    if res id None:
        abort(400, {'Not a JSON'})
    if "name" not in res:
        abort(400, {'Missing name'})
    stateObject = State(name=res['name'])
    storage.new(stateObject)
    storage.save()
    return jsonify(stateObject.to_dict()), '201'


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def putinV():
    '''vladimir'''
    res = request.get_json()
    if res id None:
        abort(400, {'Not a JSON'})
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    ignoreKeys = ['id', 'created_at', 'updated_at']
    for key in res.items():
        if key not in ignoreKeys:
            setattr(stateObject, key)
    storage.save()
    return jsonify(stateObject.to_dict()), '200'


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleting():
    ''' to delete an onbject'''
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    storage.delete(stateObject)
    storage.save()
    return jsonify({}), '200'

