#!/usr/bin/env python3
"""
Basic Flask app for user authentication service.

This module provides a Flask web application with endpoints for user
registration, login/logout, profile management, and password reset
functionality. The app uses the Auth class for all authentication
operations and maintains user sessions through cookies.

Routes:
    GET /: Welcome message
    POST /users: Register a new user
    POST /sessions: Login user
    DELETE /sessions: Logout user
    GET /profile: Get user profile
    POST /reset_password: Get password reset token
    PUT /reset_password: Update password with reset token
"""


from flask import Flask, jsonify, request, abort, redirect
from auth import Auth

app = Flask(__name__)

AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """
    Welcome endpoint.

    Returns:
        JSON response with welcome message.
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """
    User registration endpoint.

    Expects form data with 'email' and 'password' fields.
    Creates a new user account if the email is not already registered.

    Returns:
        JSON response with user email and success message (200),
        or error message if email already exists (400).
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": user.email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    User login endpoint.

    Expects form data with 'email' and 'password' fields.
    Validates user credentials and creates a session if valid.

    Returns:
        JSON response with user email and login message (200),
        or 401 error if credentials are invalid.
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie("session_id", session_id)
    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    User logout endpoint.

    Expects session_id cookie to identify the user session.
    Destroys the user session and redirects to home page.

    Returns:
        Redirect to home page (/) if successful,
        or 403 error if session is invalid.
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    AUTH.destroy_session(user.id)
    return redirect('/')


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    User profile endpoint.

    Expects session_id cookie to identify the user.
    Returns the user's email address if session is valid.

    Returns:
        JSON response with user email (200),
        or 403 error if session is invalid.
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user is None:
        abort(403)
    return jsonify({"email": user.email}), 200


@app.route('/reset_password', methods=['POST'], strict_slashes=False)
def get_reset_password_token():
    """
    Password reset token generation endpoint.

    Expects form data with 'email' field.
    Generates a reset token for the user if email exists.

    Returns:
        JSON response with email and reset token (200),
        or 403 error if email is not registered.
    """
    email = request.form.get('email')
    try:
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except ValueError:
        abort(403)


@app.route('/reset_password', methods=['PUT'], strict_slashes=False)
def update_password():
    """
    Password update endpoint.

    Expects form data with 'email', 'reset_token', and 'new_password' fields.
    Updates the user's password using the provided reset token.

    Returns:
        JSON response with email and success message (200),
        or 403 error if reset token is invalid.
    """
    email = request.form.get('email')
    reset_token = request.form.get('reset_token')
    new_password = request.form.get('new_password')
    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except ValueError:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
