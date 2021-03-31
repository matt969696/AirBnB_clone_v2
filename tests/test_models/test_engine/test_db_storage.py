#!/usr/bin/python3
""" Test for DataBase Storage """
import MySQLdb
import unittest
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.state import State
from os import getenv
import inspect
import pep8
from models.engine import db_storage
DBStorage = db_storage.DBStorage


class TestDBStorageDocs(unittest.TestCase):
    """Tests to check the documentation and style of DBStorage class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.dbs_f = inspect.getmembers(DBStorage, inspect.isfunction)

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_db_storage(self):
        """Test tests/test_models/test_db_storage.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_engine/\
test_db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_db_storage_module_docstring(self):
        """Test for the db_storage.py module docstring"""
        self.assertIsNot(db_storage.__doc__, None,
                         "db_storage.py needs a docstring")
        self.assertTrue(len(db_storage.__doc__) >= 1,
                        "db_storage.py needs a docstring")

    def test_db_storage_class_docstring(self):
        """Test for the DBStorage class docstring"""
        self.assertIsNot(DBStorage.__doc__, None,
                         "DBStorage class needs a docstring")
        self.assertTrue(len(DBStorage.__doc__) >= 1,
                        "DBStorage class needs a docstring")

    def test_dbs_func_docstrings(self):
        """Test for the presence of docstrings in DBStorage methods"""
        for func in self.dbs_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


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

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_all_no_class(self):
        """Test that all returns all rows when no class is passed"""

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_new(self):
        """test that new adds an object to the database"""

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') != 'db',
                     "not testing db storage")
    def test_save(self):
        """Test that save properly saves objects to file.json"""
