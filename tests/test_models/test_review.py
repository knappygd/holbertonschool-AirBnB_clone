#!/usr/bin/python3
"""
    Unittest of Review
"""
import unittest
import pycodestyle
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):

    def test_subclass(self):
        self.assertTrue(issubclass(Review, BaseModel))

    def test_pep8(self):
        syntaxis = pycodestyle.StyleGuide(quit=True)
        test = syntaxis.check_files(['models/review.py'])
        self.assertEqual(test.total_errors, 0, "Found style errors")

    def test_attributes(self):
        review = Review()
        self.assertTrue(isinstance(review, BaseModel))
        self.assertTrue(review, "place_id")
        self.assertIs(type(review.place_id), str)
        self.assertEqual(review.place_id, "")
        self.assertTrue(review, "user_id")
        self.assertIs(type(review.user_id), str)
        self.assertEqual(review.user_id, "")
        self.assertTrue(review, "text")
        self.assertIs(type(review.text), str)
        self.assertEqual(review.text, "")

    if __name__ == '__main__':
        unittest.main()
