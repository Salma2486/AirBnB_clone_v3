#!/usr/bin/python3
"""Tgfhghggfx hfgh dgf"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models.state import State
from models import storage


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """get"""
    s = storage.all(State)
    return jsonify([state.to_dict() for state in s.values()])


@app_views.route('/states/<state_id>', methods=['GET'])
def get_state(state_id):
    """Get"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    return jsonify(state.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'])
def delete_state(state_id):
    """sdg sr gtsrth ig"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    storage.delete(state)
    storage.save()
    return jsonify({}), 200


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def create_state():
    """h sortiulsehtlui nkh"""
    data_dict = request.get_json(silent=True)
    if not data_dict:
        abort(400, description="Not a JSON")
    if 'name' not in data_dict:
        abort(400, description="Missing name")
    new_state = State(**data_dict)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['PUT'])
def update_state(state_id):
    """Update"""
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    data_dict = request.get_json(silent=True)
    if not data_dict:
        abort(400, description="Not a JSON")
    for key, value in data_dict.items():
        if key not in ("id", "created_at", "updated_at"):
            setattr(state, key, value)
    state.save()
    return jsonify(state.to_dict()), 200
