#!/usr/bin/env python3
"""Module that contains SessionAuth class definition."""
from api.v1.auth.auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Allows 'in-memory' Session ID storing"""

    # Dictionary to store user_id mapped to session_id
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a Session ID for a `user_id`"""
        # Check if user_id is a non-empty string
        if user_id is None or not isinstance(user_id, str):
            return None
        # Generate a new session_id using uuid
        session_id = str(uuid.uuid4())
        # Store the user_id in the dictionary with the session_id as the key
        self.user_id_by_session_id[session_id] = user_id
        # Return the generated session_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Method for retrieving a User ID"""
        # Check if session_id is a non-empty string
        if session_id is None or not isinstance(session_id, str):
            return None
        # Retrieve user_id from the dictionary using session_id as the key
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Overloads current_user; returns a User based on a
        cookie value.
        """
        # Check if request is provided
        if request is None:
            return None

        # Extract session_id from the request's session cookie
        session_id = self.session_cookie(request)
        if session_id is None:
            return None

        # Retrieve user_id using session_id
        user_id = self.user_id_for_session_id(session_id)
        if user_id is None:
            return None

        # Retrieve the User object using user_id
        user = User.get(user_id)
        return user

    def destroy_session(self, request=None):
        """Deletes the user session / logout"""
        # Check if request is provided
        if not request:
            return False

        # Extract session_id from the request's session cookie
        session_id = self.session_cookie(request)
        if not session_id:
            return False

        # Retrieve user_id using session_id
        user_id = self.user_id_for_session_id(session_id)
        if not user_id:
            return False

        # Remove the session_id from the dictionary
        self.user_id_by_session_id.pop(session_id)
        return True
