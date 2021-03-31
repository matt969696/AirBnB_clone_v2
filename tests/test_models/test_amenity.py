#!/usr/bin/python3
""" """
import unittest
from models.amenity import Amenity
from datetime import datetime


class test_Amenity(unittest.TestCase):
    """ Test Amenity Class """

    def setUp(self):
        """ Initialization """
        self.am_1 = Amenity()
        self.am_1.name = "Kitchen"

    def test_attr_base(self):
        """ Test attribut BaseModel """
        self.assertIsNotNone(self.am_1.id)
        self.assertIsNotNone(self.am_1.created_at)
        self.assertIsNotNone(self.am_1.updated_at)
        self.assertIsNotNone(self.am_1.name)

    def test_type_attr_base(self):
        """ Test type attribut BaseModel """
        self.assertEqual(type(self.am_1.id), str)
        self.assertEqual(type(self.am_1.created_at), datetime)
        self.assertEqual(type(self.am_1.updated_at), datetime)

    def test_attr(self):
        """ Test attribut Amenity class """
        self.assertEqual(self.am_1.name, "Kitchen")

    def test_type_args(self):
        """ Test type attribut Amenity """
        self.assertEqual(type(self.am_1.name), str)
