#!/usr/bin/env python3
"""
Contains functions for hashing passwords and validating them.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hashes the provided password with a generated salt
    and returns the resulting byte string.
    """
    encoded_password = password.encode('utf-8')
    return bcrypt.hashpw(encoded_password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Validates whether the provided password matches the
    previously hashed password.
    """
    encoded_password = password.encode('utf-8')
    return bcrypt.checkpw(encoded_password, hashed_password)
