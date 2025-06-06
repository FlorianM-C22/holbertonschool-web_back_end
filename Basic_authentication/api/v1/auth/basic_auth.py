#!/usr/bin/env python3
""" Basic authentication module
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ Basic authentication class
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Extracts the Base64 part of
        the Authorization header for Basic Authentication
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.partition('Basic ')[2]
