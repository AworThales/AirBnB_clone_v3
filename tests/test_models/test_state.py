#!/usr/bin/python3
"""
Contains the TestStateDocs classes
"""

from datetime import datetime
import inspect
import models
from models import stat
from models.base_model import BaseModel
import pep8
import unittest
State = stat.State


class TestStateDocs(unittest.TestCase):
    """Tests to check the documentation and style of State class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.state_f = inspect.getmembers(State, inspect.isfunction)

    def test_pep8_conformance_state(self):
        """Test that models/stat.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['models/stat.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_state(self):
        """Test that tests/test_models/test_state.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['tests/test_models/test_state.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_state_module_docstring(self):
        """Test for the stat.py module docstring"""
        self.assertIsNot(stat.__doc__, None,
                         "stat.py needs a docstring")
        self.assertTrue(len(stat.__doc__) >= 1,
                        "stat.py needs a docstring")

    def test_state_class_docstring(self):
        """Test for the State class docstring"""
        self.assertIsNot(State.__doc__, None,
                         "State class needs a docstring")
        self.assertTrue(len(State.__doc__) >= 1,
                        "State class needs a docstring")

    def test_state_func_docstrings(self):
        """Test for the presence of docstrings in State methods"""
        for func in self.state_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestState(unittest.TestCase):
    """Test the State class"""
    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        stat = State()
        self.assertIsInstance(stat, BaseModel)
        self.assertTrue(hasattr(stat, "id"))
        self.assertTrue(hasattr(stat, "created_at"))
        self.assertTrue(hasattr(stat, "updated_at"))

    def test_name_attr(self):
        """Test that State has attribute name, and it's as an empty string"""
        stat = State()
        self.assertTrue(hasattr(stat, "name"))
        if models.storage_t == 'db':
            self.assertEqual(stat.name, None)
        else:
            self.assertEqual(stat.name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        s = State()
        new_dicz = s.to_dict()
        self.assertEqual(type(new_dicz), dict)
        self.assertFalse("_sa_instance_state" in new_dicz)
        for attr in s.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_dicz)
        self.assertTrue("__class__" in new_dicz)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        times_format = "%Y-%m-%dT%H:%M:%S.%f"
        s = State()
        new_dicz = s.to_dict()
        self.assertEqual(new_dicz["__class__"], "State")
        self.assertEqual(type(new_dicz["created_at"]), str)
        self.assertEqual(type(new_dicz["updated_at"]), str)
        self.assertEqual(new_dicz["created_at"], s.created_at.strftime(t_format))
        self.assertEqual(new_dicz["updated_at"], s.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        stat = State()
        string = "[State] ({}) {}".format(stat.id, stat.__dict__)
        self.assertEqual(string, str(stat))
