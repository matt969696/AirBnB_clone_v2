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

    def setUp(self):
        """ Set Up """
        self.conn = MySQLdb.connect(getenv("HBNB_MYSQL_HOST"),
                                    getenv("HBNB_MYSQL_USER"),
                                    getenv("HBNB_MYSQL_PWD"),
                                    getenv("HBNB_MYSQL_DB"))
        self.cur = self.conn.cursor()

    def tearDown(self):
        """ Tear Down """
        self.cur.close()
        self.conn.close()


    def test_new_record(self):
        """ Test add new record in table """
        nb = self.cur.execute("SELECT COUNT(*) FROM states")
        newState = State(name="California")
        newState.save()
        nbAfter = self.cur.execute("SELECT COUNT(*) FROM states")
        self.assertEqual(nbAfter - nb, 1)


    def test_find_state(self):
        """ Test find state """
        newState = State(name="New York")
        newState.save()
        name = self.cur.execute("SELECT states.name FROM states\
        WHERE name LIKE BINARY 'N%'")
        query_rows = self.cur.fetchall()
        for row in query_rows:
            self.assertEqual(row, "New York")



