#!/usr/bin/env python3
"""Unittests for Place Class
"""
import unittest
from models.place import Place

class TestBase(unittest.TestCase):
    """Test functions for Place Class
    """
    def test_attr_city_id(self):
        """Tests city_id attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "city_id"))
        self.assertEqual(p.city_id, "")

    def test_attr_user_id(self):
        """Tests user_id attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "user_id"))
        self.assertEqual(p.user_id, "")

    def test_attr_name(self):
        """Tests name attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "name"))
        self.assertEqual(p.name, "")

    def test_attr_description(self):
        """Tests description attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "description"))
        self.assertEqual(p.description, "")

    def test_attr_number_rooms(self):
        """Tests number_rooms attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "number_rooms"))
        self.assertEqual(p.number_rooms, 0)

    def test_attr_number_bathrooms(self):
        """Tests number_bathrooms attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "number_bathrooms"))
        self.assertEqual(p.number_bathrooms, 0)

    def test_attr_max_guest(self):
        """Tests max_guest attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "max_guest"))
        self.assertEqual(p.max_guest, 0)

    def test_attr_price_by_night(self):
        """Tests price_by_night attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "price_by_night"))
        self.assertEqual(p.price_by_night, 0)

    def test_attr_latitude(self):
        """Tests latitude attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "latitude"))
        self.assertEqual(p.latitude, 0.0)

    def test_attr_longitude(self):
        """Tests longitude attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "longitude"))
        self.assertEqual(p.longitude, 0.0)

    def test_attr_amenity_ids(self):
        """Tests amenity_ids attribute
        """
        p = Place()
        self.assertTrue(hasattr(p, "amenity_ids"))
        self.assertEqual(p.amenity_ids, [])

if __name__ == '__main__':
    unittest.main()
