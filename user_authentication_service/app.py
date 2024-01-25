#!/usr/bin/env python3
"""Contains definition for a Basic Flask app"""
from auth import Auth
from flask import Flask, jsonify, request, abort, redirect


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """sets up basic route"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """Registers a new user"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return {"message": "email already registered"}, 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """Creates a session_id and logs in the user"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """Destroys a session id and redirects the user to GET /"""
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', strict_slashes=False)
def profile():
    """Returns the user's email, if they exist"""
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)
    user = AUTH.get_user_from_session_id(session_id)
    if not user:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=["POST"], strict_slashes=False)
def get_reset_password_token():
    """Generates a reset password token"""
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "email missing"}), 400
    try:
        reset_token = AUTH.get_reset_password_token(email)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "reset_token": reset_token}), 200


@app.route('/reset_password', methods=["PUT"], strict_slashes=False)
def update_password():
    """Updates a password using a reset token"""
    email = request.form.get("email")
    if not email:
        return jsonify({"error": "email missing"}), 400
    reset_token = request.form.get("reset_token")
    if not reset_token:
        return jsonify({"error": "reset token missing"})
    new_password = request.form.get("new_password")
    if not new_password:
        return jsonify({"error": "new password missing"})
    try:
        AUTH.update_password(reset_token, new_password)
    except ValueError:
        abort(403)
    return jsonify({"email": email, "message": "Password updated"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
