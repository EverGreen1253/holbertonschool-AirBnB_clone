#!/usr/bin/env python3
"""Unittests for User Class
"""
import unittest
from models.user import User

class TestBase(unittest.TestCase):
    """Test functions for User Class
    """
    def test_attr_email(self):
        """Tests email attribute
        """
        u = User()
        self.assertTrue(hasattr(u, "email"))
        self.assertEqual(u.email, "")

    def test_attr_password(self):
        """Tests password attribute
        """
        u = User()
        self.assertTrue(hasattr(u, "password"))
        self.assertEqual(u.password, "")

    def test_attr_first_name(self):
        """Tests first_name attribute
        """
        u = User()
        self.assertTrue(hasattr(u, "first_name"))
        self.assertEqual(u.first_name, "")

    def test_attr_last_name(self):
        """Tests last_name attribute
        """
        u = User()
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.last_name, "")

    def test_to_str_method(self):
        """Tests that the instance can be stringified
        """
        u = User()
        self.assertEqual(u.__str__(), "[User] ({0}) {1}".format(u.id, u.__dict__))


if __name__ == '__main__':
    unittest.main()
