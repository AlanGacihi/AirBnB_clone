#!/usr/bin/python3
"""Unittest cases for Amenity"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attr_is_a_class_attr(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = Amenity()
        self.assertIsInstance(obj, Amenity)

    def test_args(self):
        """Arguments to the instance"""
        b = Amenity(8)
        self.assertEqual(type(b).__name__, "Amenity")
        self.assertFalse(hasattr(b, "8"))
