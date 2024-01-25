#!/usr/bin/env python3
"""Module that contains the Auth class"""
from user import User
from db import DB
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4
from typing import Optional


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Hashes the password and saves the user to the database"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            user = None
        if user:
            raise ValueError(f"User {email} already exists.")
        hashed_password = _hash_password(password)
        user = self._db.add_user(email, hashed_password)
        return user

    def valid_login(self, email: str, password: str) -> bool:
        """Locates a user by email and checks whether the passwrod matches
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        if user:
            encoded_password = password.encode('utf-8')
            if checkpw(encoded_password, user.hashed_password):
                return True
        return False

    def create_session(self, email: str) -> str:
        """Takes an email string, creates and returns the session ID."""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None
        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id

    def get_user_from_session_id(self, session_id: str) -> Optional[User]:
        """Retrieves a user object, if the user exists"""
        try:
            user = self._db.find_user_by(session_id=session_id)
        except NoResultFound:
            return None
        return user

    def destroy_session(self, user_id: int) -> None:
        """Destroys a session by setting the User's session_id to None"""
        try:
            self._db.find_user_by(id=user_id)
        except NoResultFound:
            return None
        self._db.update_user(user_id, session_id=None)

    def get_reset_password_token(self, email: str) -> str:
        """Generates a UUID and updates the user's reset_token database field.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            raise ValueError
        reset_token = _generate_uuid()
        self._db.update_user(user.id, reset_token=reset_token)
        return reset_token

    def update_password(self, reset_token: str, password: str) -> None:
        """Updates a password"""
        try:
            user = self._db.find_user_by(reset_token=reset_token)
        except NoResultFound:
            raise ValueError
        hashed_password = _hash_password(password)
        self._db.update_user(user.id, hashed_password=hashed_password,
                             reset_token=None)


def _generate_uuid() -> str:
    """Generates and returns a string representation of a new UUID."""
    return str(uuid4())


def _hash_password(password: str) -> bytes:
    """Returns a salted hash of the input password"""
    encoded_password = password.encode('utf-8')
    return hashpw(encoded_password, gensalt())
