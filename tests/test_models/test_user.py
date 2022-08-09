#!/usr/bin/python3
"""Unittest cases for User"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def test_attrs_are_class_attrs(self):
        """Check for the given attributes"""
        u = User()
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_class_attrs(self):
        """Check class attributes"""
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        """Check if user is a subclass of basemodel"""
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = User()
        self.assertIsInstance(obj, User)

    def test_args(self):
        """Arguments to the instance"""
        b = User(8)
        self.assertEqual(type(b).__name__, "User")
        self.assertFalse(hasattr(b, "8"))
