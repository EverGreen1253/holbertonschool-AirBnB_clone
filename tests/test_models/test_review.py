#!/usr/bin/env python3
"""Unittests for Review Class
"""
import unittest
from models.review import Review

class TestBase(unittest.TestCase):
    """Test functions for Review Class
    """
    def test_attr_place_id(self):
        """Tests place_id attribute
        """
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertEqual(r.place_id, "")

    def test_attr_user_id(self):
        """Tests user_id attribute
        """
        r = Review()
        self.assertTrue(hasattr(r, "user_id"))
        self.assertEqual(r.user_id, "")

    def test_attr_text(self):
        """Tests text attribute
        """
        r = Review()
        self.assertTrue(hasattr(r, "text"))
        self.assertEqual(r.text, "")

if __name__ == '__main__':
    unittest.main()
