#!/usr/bin/python3
"""t ydhdty hj"""
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS

app = Flask(__name__)


cors = CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """Close storage"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Error handler for 404 not found."""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """ Main Function """
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
