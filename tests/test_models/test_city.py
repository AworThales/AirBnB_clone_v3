#!/usr/bin/python3
"""
Contains the TestCityDocs classes
"""

from datetime import datetime
import inspect
import models
from models import cit
from models.base_model import BaseModel
import pep8
import unittest
City = cit.City


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/cit.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['models/cit.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the cit.py module docstring"""
        self.assertIsNot(cit.__doc__, None,
                         "cit.py needs a docstring")
        self.assertTrue(len(cit.__doc__) >= 1,
                        "cit.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for the presence of docstrings in City methods"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestCity(unittest.TestCase):
    """Test the City class"""
    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        cit = City()
        self.assertIsInstance(cit, BaseModel)
        self.assertTrue(hasattr(cit, "id"))
        self.assertTrue(hasattr(cit, "created_at"))
        self.assertTrue(hasattr(cit, "updated_at"))

    def test_name_attr(self):
        """Test that City has attribute name, and it's an empty string"""
        cit = City()
        self.assertTrue(hasattr(cit, "name"))
        if models.storage_t == 'db':
            self.assertEqual(cit.name, None)
        else:
            self.assertEqual(cit.name, "")

    def test_state_id_attr(self):
        """Test that City has attribute state_id, and it's an empty string"""
        cit = City()
        self.assertTrue(hasattr(cit, "state_id"))
        if models.storage_t == 'db':
            self.assertEqual(cit.state_id, None)
        else:
            self.assertEqual(cit.state_id, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        c = City()
        new_diz = c.to_dict()
        self.assertEqual(type(new_diz), dict)
        self.assertFalse("_sa_instance_state" in new_diz)
        for attr in c.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_diz)
        self.assertTrue("__class__" in new_diz)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        c = City()
        new_diz = c.to_dict()
        self.assertEqual(new_diz["__class__"], "City")
        self.assertEqual(type(new_diz["created_at"]), str)
        self.assertEqual(type(new_diz["updated_at"]), str)
        self.assertEqual(new_diz["created_at"], c.created_at.strftime(t_format))
        self.assertEqual(new_diz["updated_at"], c.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        cit = City()
        string = "[City] ({}) {}".format(cit.id, cit.__dict__)
        self.assertEqual(string, str(cit))
