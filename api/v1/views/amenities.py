#!/usr/bin/python3
"""amenity"""
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from flask import jsonify, abort, request
from datetime import datetime
import uuid


@app_views.route('/amenity/', methods=['GET'])
def list_amenities():
    '''Retrieves a list of all Amenity objects'''
    list_ameniti = [obj.to_dict() for obj in storage.all("Amenity").values()]
    return jsonify(list_ameniti)


@app_views.route('/amenity/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    '''Retrieves an Amenity object'''
    all_amenit = storage.all("Amenity").values()
    amenity_objects = [obj.to_dict() for obj in all_amenit
                   if obj.id == amenity_id]
    if amenity_objects == []:
        abort(404)
    return jsonify(amenity_objects[0])


@app_views.route('/amenity/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    '''Deletes an Amenity object'''
    all_amenit = storage.all("Amenity").values()
    amenity_objects = [obj.to_dict() for obj in all_amenit
                   if obj.id == amenity_id]
    if amenity_objects == []:
        abort(404)
    amenity_objects.remove(amenity_objects[0])
    for obj in all_amenit:
        if obj.id == amenity_id:
            storage.delete(obj)
            storage.save()
    return jsonify({}), 200


@app_views.route('/amenity/', methods=['POST'])
def create_amenity():
    '''Creates an Amenity'''
    if not request.get_json():
        abort(400, 'Not a JSON')
    if 'name' not in request.get_json():
        abort(400, 'Missing name')
    amenity = []
    fresh_amenity = Amenity(name=request.json['name'])
    storage.new(fresh_amenity)
    storage.save()
    amenity.append(fresh_amenity.to_dict())
    return jsonify(amenity[0]), 201


@app_views.route('/amenity/<amenity_id>', methods=['PUT'])
def updates_amenity(amenity_id):
    '''Updates an Amenity object'''
    all_amenit = storage.all("Amenity").values()
    amenity_objects = [obj.to_dict() for obj in all_amenit
                   if obj.id == amenity_id]
    if amenity_objects == []:
        abort(404)
    if not request.get_json():
        abort(400, 'Not a JSON')
    amenity_objects[0]['name'] = request.json['name']
    for obj in all_amenit:
        if obj.id == amenity_id:
            obj.name = request.json['name']
    storage.save()
    return jsonify(amenity_objects[0]), 200
