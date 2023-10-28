#!/usr/bin/python3
"""Unittests for City Class
"""
import unittest
from models.city import City

class TestBase(unittest.TestCase):
    """Test functions for City Class
    """
    def test_attr_state_id(self):
        """Tests state_id attribute
        """
        c = City()
        self.assertTrue(hasattr(c, "state_id"))
        self.assertEqual(c.state_id, "")

    def test_attr_name(self):
        """Tests name attribute
        """
        c = City()
        self.assertTrue(hasattr(c, "name"))
        self.assertEqual(c.name, "")

if __name__ == '__main__':
    unittest.main()
