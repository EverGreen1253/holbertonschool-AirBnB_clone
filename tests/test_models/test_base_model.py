#!/usr/bin/env python3
"""Unittests for Base Model Class
"""
import unittest
from models.base_model import BaseModel

class TestBase(unittest.TestCase):
    """Test functions for BaseModel Class
    """
    def test_id_selfgen(self):
        """Tests self-generated uuid
        """
        b = BaseModel()
        x = b.id != None
        self.assertEqual(x, True)

    def test_save_method(self):
        """Tests save method
        """
        b = BaseModel()
        dt_old = str(b.updated_at)
        b.save()
        dt_new = str(b.updated_at)

        self.assertNotEqual(dt_old, dt_new)

    def test_to_dict_method(self):
        """Tests to_dict method
        """
        b = BaseModel()
        d = b.to_dict()

        self.assertEqual(b.id, d["id"])

    def test_to_str_method(self):
        """Tests that the instance can be stringified
        """
        b = BaseModel()
        self.assertEqual(b.__str__(), "[BaseModel] ({0}) {1}".format(b.id, b.__dict__))

if __name__ == '__main__':
    unittest.main()
