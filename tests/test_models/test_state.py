#!/usr/bin/python3
"""Unittests for State Class
"""
import unittest
from models.state import State

class TestBase(unittest.TestCase):
    """Test functions for State Class
    """
    def test_attr_name(self):
        """Tests name attribute
        """
        s = State()
        self.assertTrue(hasattr(s, "name"))
        self.assertEqual(s.name, "")

if __name__ == '__main__':
    unittest.main()
