#!/usr/bin/env python3
"""
Basic_auth module
"""

from api.v1.auth.auth import Auth
import base64
from models.user import User
from typing import TypeVar


class BasicAuth(Auth):
    """ BasicAuth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Return:
        - the Base64 part of the Authorization header
        """
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None

        if authorization_header.startswith('Basic '):
            return authorization_header.partition('Basic ')[2]

        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """ Return:
        - the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None

        try:
            decode = base64.b64decode(
                base64_authorization_header).decode('utf-8')
            return decode

        except (TypeError, ValueError):
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """ Return:
        the user email and password from the Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None

        email, _, password = decoded_base64_authorization_header.partition(':')

        return email, password

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """ Return:
        the User instance based on his email and password
        """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None

        try:
            users = User.search({"email": user_email})
        except Exception:
            return None
        if not users:
            return None

        user = users[0]

        if not user.is_valid_password(user_pwd):
            return None

        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """ that overloads Auth and retrieves
        the User instance for a request
        """
        header = self.authorization_header(request)
        if header is None:
            return None

        extract64 = self.extract_base64_authorization_header(header)
        if extract64 is None:
            return None

        decode64 = self.decode_base64_authorization_header(extract64)
        if decode64 is None:
            return None

        email, password = self.extract_user_credentials(decode64)
        if email is None or password is None:
            return None

        user = self.user_object_from_credentials(email, password)

        return user
