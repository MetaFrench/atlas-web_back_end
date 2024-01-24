#!/usr/bin/env python3
"""
Main module for the API
"""
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.register_blueprint(app_views)

# Enable Cross-Origin Resource Sharing (CORS) for the entire API
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

# Initialize authentication based on the selected AUTH_TYPE
auth = None
auth_type = getenv("AUTH_TYPE", "basic")

# Determine the authentication type and initialize the corresponding authentication instance
if auth_type == "auth":
    from api.v1.auth.auth import Auth
    auth = Auth()
elif auth_type == "basic_auth":
    from api.v1.auth.basic_auth import BasicAuth
    auth = BasicAuth()
elif auth_type == "session_auth":
    from api.v1.auth.session_auth import SessionAuth
    auth = SessionAuth()

# Error handlers for specific HTTP status codes


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Forbidden handler """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Unauthorized handler """
    return jsonify({"error": "Unauthorized"}), 401

# Before each request, perform authentication and set the current user for the request


@app.before_request
def before_request():
    """ Filters requests to error handlers """
    # List of paths that do not require authentication
    path_list = ['/api/v1/status/',
                 '/api/v1/unauthorized',
                 '/api/v1/forbidden',
                 '/api/v1/auth_session/login/']

    # Check if authentication is required for the current request
    if not auth.require_auth(request.path, path_list):
        return

    # Check for authorization header or session cookie, otherwise return 401 Unauthorized
    if not auth.authorization_header(request) and not auth.session_cookie(request):
        abort(401)

    # Check if the current user is authenticated, otherwise return 403 Forbidden
    if auth.current_user(request) is None:
        abort(403)

    # Set the current user for the request
    request.current_user = auth.current_user(request)


# Run the application
if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
