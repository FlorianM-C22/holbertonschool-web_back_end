#!/usr/bin/env python3
""" Basic authentication module
"""
from flask import request
from typing import List, TypeVar, Optional

User = TypeVar('User')


class Auth:
    """ Auth class
    """

    def require_auth(self, path: Optional[str], excluded_paths: Optional[List[str]]) -> bool:
        """ require_auth method
        """
        if path is None:
            return True
        if excluded_paths is None:
            return True

        for excluded_path in excluded_paths:
            # Make comparison slash tolerant
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
        return None

    def current_user(self, request=None) -> User:
        """ current_user method
        """
        return None
