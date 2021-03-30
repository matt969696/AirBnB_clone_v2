#!/usr/bin/python3
""" Test for DataBase Storage """
import MySQLdb
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State
from os import getenv

class TestDBStorage(unittest.TestCase):
    """ Unittest for database storage """

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not supported in file storage mode")
    def setUp(self):
        """ Set Up """
        self.conn = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                    getenv("HBNB_MYSQL_USER"),
                                    getenv("HBNB_MYSQL_PWD"),
                                    getenv("HBNB_MYSQL_DB"))
        self.cur = self.conn.cursor()

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not supported in file storage mode")
    def tearDown(self):
        """ Tear Down """
        self.cur.close()
        self.conn.close()

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not supported in file storage mode")
    def test_new_record(self):
        """ Test add new record in table """
        newState = State(name="Lyon")
        newState.save()
        nb = self.cur.execute("SELECT * FROM states")
        newState2 = State(name="Paris")
        newState2.save()
        nbAfter = self.cur.execute("SELECT * FROM states")
        self.assertEqual(nbAfter - nb, 0)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not supported in file storage mode")
    def test_find_state(self):
        """ Test find state """
        newState = State(name="Nana")
        newState.save()
        name = self.cur.execute("SELECT states.name FROM states\
        WHERE name LIKE BINARY 'N%'")
        query_rows = self.cur.fetchall()
        for row in query_rows:
            self.assertEqual(row, ('Nana',))



