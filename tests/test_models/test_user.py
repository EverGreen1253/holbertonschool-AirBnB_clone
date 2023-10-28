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
        u = User()
        test_string = "test@email.com"
        u.email = test_string
        self.assertEqual(u.email, "test@email.com")

    def test_attr_password(self):
        """Tests password attribute
        """
        u = User()
        test_string = "yo_momma_is_phat_123"
        u.password = test_string
        self.assertEqual(u.password, "yo_momma_is_phat_123")

    def test_attr_first_name(self):
        """Tests first_name attribute
        """
        u = User()
        u.first_name = "Clark"
        self.assertEqual(u.first_name, "Clark")

    def test_attr_last_name(self):
        """Tests last_name attribute
        """
        u = User()
        u.last_name = "Kent"
        self.assertEqual(u.last_name, "Kent")

    def test_to_str_method(self):
        """Tests that the instance can be stringified
        """
        u = User()
        self.assertEqual(u.__str__(), "[User] ({0}) {1}".format(u.id, u.__dict__))


if __name__ == '__main__':
    unittest.main()
