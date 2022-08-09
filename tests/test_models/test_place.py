#!/usr/bin/python3
"""Unittest cases for place"""


import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """Class Place - Unittest"""

    def setUp(self):
        self.place = Place()
        self.attr_list = ["name", "user_id", "city_id", "description",
                          "number_bathrooms", "max_guest", "number_rooms",
                          "price_by_night", "latitude", "longitude",
                          "amenity_ids"]

    def test_attrs_are_class_attrs(self):
        """Test if the attributs are class_attributes"""
        for attr in self.attr_list:
            self.assertTrue(hasattr(Place, attr))

    def test_class_attrs(self):
        """Check attributes"""
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

        for attr in self.attr_list:
            self.assertFalse(bool(getattr(self.place, attr)))

    def test_place_obj_is_a_subclass_of_basemodel(self):
        """Test if it is an object of the BaseModel class"""
        self.assertTrue(issubclass(type(self.place), BaseModel))

    def test_args(self):
        """Arguments to the instance"""
        b = Place(8)
        self.assertEqual(type(b).__name__, "Place")
        self.assertFalse(hasattr(b, "8"))
