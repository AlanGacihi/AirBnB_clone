#!/usr/bin/python3
"""Unittest cases for console"""

import unittest
import console
import pep8
import sys
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class Test_BaseModel(unittest.TestCase):
    """Class for testing the console."""

    def test_pep8_console(self):
        """ Test for PEP8 ok. """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0, "Please fix pep8")

    def test_help(self):
        """ Test for help command. """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            cont_EOF = f.getvalue()
            HBNBCommand().onecmd("help quit")
            cont_quit = f.getvalue()
            HBNBCommand().onecmd("help all")
            cont_all = f.getvalue()
            HBNBCommand().onecmd("help create")
            cont_create = f.getvalue()
            HBNBCommand().onecmd("help destroy")
            cont_destroy = f.getvalue()
            HBNBCommand().onecmd("help help")
            cont_help = f.getvalue()
            HBNBCommand().onecmd("help show")
            cont_show = f.getvalue()
            HBNBCommand().onecmd("help update")
            cont_update = f.getvalue()
        self.assertNotEqual(cont_EOF, "*** No help on EOF\n")
        self.assertNotEqual(cont_quit, "*** No help on quit\n")
        self.assertNotEqual(cont_all, "*** No help on all\n")
        self.assertNotEqual(cont_create, "*** No help on create\n")
        self.assertNotEqual(cont_destroy, "*** No help on destroy\n")
        self.assertNotEqual(cont_help, "*** No help on help\n")
        self.assertNotEqual(cont_show, "*** No help on show\n")
        self.assertNotEqual(cont_update, "*** No help on update\n")

    def test_docstring_console(self):
        """Checks docstring in the console"""
        self.assertIsNot(console.__doc__, None,
                         "Please write a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "Please write a docstring"
                        )

    def test_docstrings_in_console(self):
        """Checks docstring in the console's methods"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand().do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand().do_create.__doc__)
        self.assertIsNotNone(HBNBCommand().do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand().emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand().do_show.__doc__)
        self.assertIsNotNone(HBNBCommand().do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand().do_all.__doc__)
        self.assertIsNotNone(HBNBCommand().do_update.__doc__)
        self.assertIsNotNone(HBNBCommand().default.__doc__)
