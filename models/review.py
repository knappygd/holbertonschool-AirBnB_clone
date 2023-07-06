#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Defines the class Review.

    Attributes:
        place_id: The id of the place.
        user_id: The id of the user.
        text: The content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
