#!/usr/bin/env python3
""" Module of Session authentication views
"""

from api.v1.views import app_views
from flask import jsonify, request, make_response
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login() -> str:
    """ POST /api/v1/auth_session/login
    Return:
      - User object JSON represented
      - 400 if email or password missing
      - 404 if no user found
      - 401 if wrong password
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or email == "":
        return jsonify({"error": "email missing"}), 400

    if not password or password == "":
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = make_response(jsonify(user.to_json()))
    session_name = getenv('SESSION_NAME')
    response.set_cookie(session_name, session_id)

    return response
