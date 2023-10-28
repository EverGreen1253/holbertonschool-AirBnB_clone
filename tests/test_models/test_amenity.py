#!/usr/bin/python3
"""Unittests for Amenity Class
"""
import unittest
from models.amenity import Amenity

class TestBase(unittest.TestCase):
    """Test functions for Amenity Class
    """
    def test_attr_name(self):
        """Tests name attribute
        """
        a = Amenity()
        self.assertTrue(hasattr(a, "name"))
        self.assertEqual(a.name, "")

if __name__ == '__main__':
    unittest.main()
