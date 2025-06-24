#!/usr/bin/env python3
""" Authentication module
"""
from flask import request
from typing import List, TypeVar, Optional
import os

User = TypeVar('User')


class Auth:
    """ Auth class
    """

    def require_auth(self, path: Optional[str],
                     excluded_paths: Optional[List[str]]) -> bool:
        """ require_auth method
        """
        if path is None:
            return True
        if excluded_paths is None:
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):
                if path == excluded_path or path == excluded_path.rstrip('/'):
                    return False
            else:
                if path == excluded_path or path == excluded_path + '/':
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """ authorization_header method
        """
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> User:
        """ current_user method
        """
        return None

    def session_cookie(self, request=None):
        """ session_cookie method
        """
        if request is None:
            return None
        session_name = os.getenv('SESSION_NAME')
        if session_name is None:
            return None
        return request.cookies.get(session_name)
