#!/usr/bin/env python3
"""
Encrypt_password module.
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Hash a password using bcrypt.
    """
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_password


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check if a password is valid against a hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
