#!/usr/bin/python3
"""
Contains the TestUserDocs classes
"""

from datetime import datetime
import inspect
import models
from models import users
from models.base_model import BaseModel
import pep8
import unittest
User = users.User


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/users.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['models/users.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the users.py module docstring"""
        self.assertIsNot(users.__doc__, None,
                         "users.py needs a docstring")
        self.assertTrue(len(users.__doc__) >= 1,
                        "users.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestUser(unittest.TestCase):
    """Test the User class"""
    def test_is_subclass(self):
        """Test that User is a subclass of BaseModel"""
        users = User()
        self.assertIsInstance(users, BaseModel)
        self.assertTrue(hasattr(users, "id"))
        self.assertTrue(hasattr(users, "created_at"))
        self.assertTrue(hasattr(users, "updated_at"))

    def test_email_attr(self):
        """Test that User has attr email, and it's an empty string"""
        users = User()
        self.assertTrue(hasattr(users, "email"))
        if models.storage_t == 'db':
            self.assertEqual(users.email, None)
        else:
            self.assertEqual(users.email, "")

    def test_password_attr(self):
        """Test that User has attr password, and it's an empty string"""
        users = User()
        self.assertTrue(hasattr(users, "password"))
        if models.storage_t == 'db':
            self.assertEqual(users.password, None)
        else:
            self.assertEqual(users.password, "")

    def test_first_name_attr(self):
        """Test that User has attr first_name, and it's an empty string"""
        users = User()
        self.assertTrue(hasattr(users, "first_name"))
        if models.storage_t == 'db':
            self.assertEqual(users.first_name, None)
        else:
            self.assertEqual(users.first_name, "")

    def test_last_name_attr(self):
        """Test that User has attr last_name, and it's an empty string"""
        users = User()
        self.assertTrue(hasattr(users, "last_name"))
        if models.storage_t == 'db':
            self.assertEqual(users.last_name, None)
        else:
            self.assertEqual(users.last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = User()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in u.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        times_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = User()
        new_dicz = u.to_dict()
        self.assertEqual(new_d["__class__"], "User")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        users = User()
        string = "[User] ({}) {}".format(users.id, users.__dict__)
        self.assertEqual(string, str(users))
