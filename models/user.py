#!/usr/bin/python3
"""Instantiates the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines the class User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
