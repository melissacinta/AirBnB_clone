#!/usr/bin/python3
"""
Test suits for the base model
"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """
    Tests attributes of the base model
    """
    def setUp(self):
        pass

    def test_initialization(self):
        """
        Tests basic inputs for the BaseModel class
        """
        my_model = BaseModel()
        my_model2_uuid = str(uuid.uuid4())
        my_model2 = BaseModel(id=my_model2_uuid,
                              name="The weeknd", album="Trilogy")
        my_model.name = "ALX"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number],
                         ["ALX", 89])
        self.assertIsInstance(my_model.id, str)
        self.assertIsInstance(my_model2.id, str)
        self.assertEqual(my_model2_uuid, my_model2.id)
        self.assertEqual(my_model2.album, "Trilogy")
        self.assertEqual(my_model2.name, "The weeknd")
        self.assertIsInstance(my_model.created_at, datetime)
        self.assertIsInstance(my_model.updated_at, datetime)
        self.assertEqual(str(type(my_model)),
                         "<class 'models.base_model.BaseModel'>")

    def test_dict(self):
        """Test method for dict"""
        b1 = BaseModel()
        b2_uuid = str(uuid.uuid4())
        b2 = BaseModel(id=b2_uuid, name="The weeknd", album="Trilogy")
        b1_dict = b1.to_dict()
        self.assertIsInstance(b1_dict, dict)
        self.assertIn('id', b1_dict.keys())
        self.assertIn('created_at', b1_dict.keys())
        self.assertIn('updated_at', b1_dict.keys())
        self.assertEqual(b1_dict['__class__'], type(b1).__name__)


if __name__ == '__main__':
    unittest.main()
