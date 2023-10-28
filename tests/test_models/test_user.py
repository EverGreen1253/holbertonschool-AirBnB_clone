#!/usr/bin/python3
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
        user = User()
        self.assertTrue(hasattr(user, "email"))
        self.assertEqual(user.email, "")

    def test_attr_password(self):
        """Tests password attribute
        """
        u = User()
        test_string = "yo_momma_is_phat_123"
        u.password = test_string
        self.assertEqual(type(u.password).__name__, "str")

    def test_attr_first_name(self):
        """Tests first_name attribute
        """
        u = User()
        u.first_name = "Clark"
        self.assertEqual(type(u.first_name).__name__, "str")

    def test_attr_last_name(self):
        """Tests last_name attribute
        """
        u = User()
        u.last_name = "Kent"
        self.assertEqual(type(u.last_name).__name__, "str")

    def test_to_str_method(self):
        """Tests that the instance can be stringified
        """
        u = User()
        self.assertEqual(u.__str__(), "[User] ({0}) {1}".format(u.id, u.__dict__))


if __name__ == '__main__':
    unittest.main()
