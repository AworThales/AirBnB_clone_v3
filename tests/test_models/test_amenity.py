#!/usr/bin/python3
"""
Contains the TestAmenityDocs classes
"""

from models import ameniti
from models.base_model import BaseModel
from datetime import datetime
import inspect
import models
import pep8
import unittest
Amenity = ameniti.Amenity


class TestAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that models/ameniti.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['models/ameniti.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Test for the ameniti.py module docstring"""
        self.assertIsNot(ameniti.__doc__, None,
                         "ameniti.py needs a docstring")
        self.assertTrue(len(ameniti.__doc__) >= 1,
                        "ameniti.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""
    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        ameniti = Amenity()
        self.assertIsInstance(ameniti, BaseModel)
        self.assertTrue(hasattr(ameniti, "id"))
        self.assertTrue(hasattr(ameniti, "created_at"))
        self.assertTrue(hasattr(ameniti, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name, and it's as an empty string"""
        ameniti = Amenity()
        self.assertTrue(hasattr(ameniti, "name"))
        if models.storage_t == 'db':
            self.assertEqual(ameniti.name, None)
        else:
            self.assertEqual(ameniti.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        am = Amenity()
        print(am.__dict__)
        new_dicz = am.to_dict()
        self.assertEqual(type(new_dicz), dict)
        self.assertFalse("_sa_instance_state" in new_dicz)
        for attr in am.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dicz)
        self.assertTrue("__class__" in new_dicz)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        times_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_dicz = am.to_dict()
        self.assertEqual(new_dicz["__class__"], "Amenity")
        self.assertEqual(type(new_dicz["created_at"]), str)
        self.assertEqual(type(new_dicz["updated_at"]), str)
        self.assertEqual(new_dicz["created_at"], am.created_at.strftime(times_format))
        self.assertEqual(new_dicz["updated_at"], am.updated_at.strftime(times_format))

    def test_str(self):
        """test that the str method has the correct output"""
        ameniti = Amenity()
        string = "[Amenity] ({}) {}".format(ameniti.id, ameniti.__dict__)
        self.assertEqual(string, str(ameniti))
