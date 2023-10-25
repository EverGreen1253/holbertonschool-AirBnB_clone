#!/usr/bin/python3
"""Unittests for File Storage Class
"""
import unittest
from models.engine.file_storage import FileStorage

class TestBase(unittest.TestCase):
    """Test functions for FileStorage Class
    """
    def test_id_selfgen(self):
        """Tests file_path exists
        """
        fs = FileStorage()
        x = fs.file_path != ""
        self.assertEqual(x, True)
