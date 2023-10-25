#!/usr/bin/python3
"""Unittests for File Storage Class
"""
import unittest
from models.engine.file_storage import FileStorage

class TestBase(unittest.TestCase):
    """Test functions for FileStorage Class
    """
    def test_file_path(self):
        """Tests file_path exists
        """
        fs = FileStorage()
        x = fs.file_path is not None
        self.assertEqual(x, True)
