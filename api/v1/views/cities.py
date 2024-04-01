#!/usr/bin/python3
"""Tgfhghggfx hfgh dgf"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models.state import State
from models import storage
from models.city import City


@app_views.route('/states/<state_id>/cities', methods=['GET'],
                 strict_slashes=False)
def get_cities(state_id):
    """get"""
    state = storage.get(State, state_id)
    if state is None:
        return abort(404)
    return jsonify([city.to_dict() for city in state.values()])


@app_views.route('/cities/<city_id>', methods=['GET'],
                 strict_slashes=False)
def get_city(city_id):
    """Get"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """sdg sr gtsrth ig"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    storage.save()
    return jsonify({}), 200


@app_views.route('states/<state_id>/cities', methods=['POST'],
                 strict_slashes=False)
def create_city(state_id):
    """h sortiulsehtlui nkh"""
    data_dict = request.get_json(silent=True)
    if not data_dict:
        abort(400, description="Not a JSON")
    if 'name' not in data_dict:
        abort(400, description="Missing name")
    new_city = City(**data_dict)
    new_city.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('cities/<city_id>', methods=['PUT'], strict_slashes=False)
def update_city(city_id):
    """Update"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    data_dict = request.get_json(silent=True)
    if not data_dict:
        abort(400, description="Not a JSON")
    for key, value in data_dict.items():
        if key not in ("id", "created_at", "updated_at"):
            setattr(city, key, value)
    city.save()
    return jsonify(city.to_dict()), 200
