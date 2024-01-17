#!/usr/bin/env python3
"""
Contains a `hash_password` function that returns a salted,
hashed password, which is a byte string.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Function that takes in a password string and returns
    a salted, hashed password, which is a byte string.
    """
    encoded_password = password.encode('utf-8')
    return (bcrypt.hashpw(encoded_password, bcrypt.gensalt()))
