#!/usr/bin/python3
"""
Contains the TestReviewDocs classes
"""

from datetime import datetime
import inspect
import models
from models import revie
from models.base_model import BaseModel
import pep8
import unittest
Review = revie.Review


class TestReviewDocs(unittest.TestCase):
    """Tests to check the documentation and style of Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test that models/revie.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['models/revie.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Test for the revie.py module docstring"""
        self.assertIsNot(revie.__doc__, None,
                         "revie.py needs a docstring")
        self.assertTrue(len(revie.__doc__) >= 1,
                        "revie.py needs a docstring")

    def test_review_class_docstring(self):
        """Test for the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """Test for the presence of docstrings in Review methods"""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestReview(unittest.TestCase):
    """Test the Review class"""
    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        revie = Review()
        self.assertIsInstance(revie, BaseModel)
        self.assertTrue(hasattr(revie, "id"))
        self.assertTrue(hasattr(revie, "created_at"))
        self.assertTrue(hasattr(revie, "updated_at"))

    def test_place_id_attr(self):
        """Test Review has attr place_id, and it's an empty string"""
        revie = Review()
        self.assertTrue(hasattr(revie, "place_id"))
        if models.storage_t == 'db':
            self.assertEqual(revie.place_id, None)
        else:
            self.assertEqual(revie.place_id, "")

    def test_user_id_attr(self):
        """Test Review has attr user_id, and it's an empty string"""
        revie = Review()
        self.assertTrue(hasattr(revie, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(revie.user_id, None)
        else:
            self.assertEqual(revie.user_id, "")

    def test_text_attr(self):
        """Test Review has attr text, and it's an empty string"""
        revie = Review()
        self.assertTrue(hasattr(revie, "text"))
        if models.storage_t == 'db':
            self.assertEqual(revie.text, None)
        else:
            self.assertEqual(revie.text, "")

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in r.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        times_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = Review()
        new_d = r.to_dict()
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], r.created_at.strftime(times_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(times_format))

    def test_str(self):
        """test that the str method has the correct output"""
        revie = Review()
        string = "[Review] ({}) {}".format(revie.id, revie.__dict__)
        self.assertEqual(string, str(revie))
