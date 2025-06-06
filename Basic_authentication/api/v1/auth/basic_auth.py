#!/usr/bin/env python3
""" Basic authentication module
"""

import base64
from typing import Union, Tuple
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

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str) \
            -> str:
        """Decode the Base64 part of the
        Authrorization header for Basic Authentication
        """
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(base64_authorization_header) \
                .decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str) \
            -> Union[Tuple[str, str], Tuple[None, None]]:
        """Extracts user credentials from the Base64 decoded
        Authorization header for Basic Authentication
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        else:
            return tuple(decoded_base64_authorization_header.split(':', 1))
