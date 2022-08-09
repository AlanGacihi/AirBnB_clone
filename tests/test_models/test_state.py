#!/usr/bin/python3
"""Unittest cases for Amenity"""

import unittest
from models.state import State
import pep8
import os


class Test_State(unittest.TestCase):
    """"Class State -Unittest """

    def test_setUp(self):
        """SetUps tests"""
        pass

    def test_tearDown(self):
        """"Restart tests"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_pep8_base_model(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_pep8_tests_base(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(
            ['tests/test_models/test_state.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_docstring(self):
        """Checks if docstring exists"""
        self.assertTrue(len(State.__doc__) > 1)
        self.assertTrue(len(State.__init__.__doc__) > 1)
        self.assertTrue(len(State.__str__.__doc__) > 1)
        self.assertTrue(len(State.save.__doc__) > 1)
        self.assertTrue(len(State.to_dict.__doc__) > 1)

    def test_isinstance(self):
        """"Test if is an instance of the class"""
        obj = State()
        self.assertIsInstance(obj, State)

    def test_args(self):
        """Arguments to the instance"""
        b = State(8)
        self.assertEqual(type(b).__name__, "State")
        self.assertFalse(hasattr(b, "8"))
