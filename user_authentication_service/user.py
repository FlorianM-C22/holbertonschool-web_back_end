#!/usr/bin/env python3
"""
This module defines the User class for the users table in the database.
The User class represents a user with email, hashed password, session ID,
and reset token.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    """
    SQLAlchemy User model for the users table.

    Attributes:
        id (int): Primary key for the user.
        email (str): User's email address, must be unique and not null.
        hashed_password (str): Hashed password for authentication, not null.
        session_id (str): Optional session identifier for the user.
        reset_token (str): Optional token for password reset functionality.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
