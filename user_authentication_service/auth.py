#!/usr/bin/env python3
"""
Auth module
"""

import bcrypt
from db import DB


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()


def _hash_password(password: str) -> str:
    """Hash a password
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
