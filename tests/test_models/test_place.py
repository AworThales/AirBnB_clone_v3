#!/usr/bin/python3
"""
Contains the TestPlaceDocs classes
"""

import inspect
import models
from models import plac
from datetime import datetime
from models.base_model import BaseModel
import pep8
import unittest
Place = plac.Place


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Place class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Test that models/plac.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['models/plac.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8ses = pep8.StyleGuide(quiet=True)
        results = pep8ses.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(results.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        """Test for the plac.py module docstring"""
        self.assertIsNot(plac.__doc__, None,
                         "plac.py needs a docstring")
        self.assertTrue(len(plac.__doc__) >= 1,
                        "plac.py needs a docstring")

    def test_place_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_place_func_docstrings(self):
        """Test for the presence of docstrings in Place methods"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestPlace(unittest.TestCase):
    """Test the Place class"""
    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        plac = Place()
        self.assertIsInstance(plac, BaseModel)
        self.assertTrue(hasattr(plac, "id"))
        self.assertTrue(hasattr(plac, "created_at"))
        self.assertTrue(hasattr(plac, "updated_at"))

    def test_city_id_attr(self):
        """Test Place has attr city_id, and it's an empty string"""
        plac = Place()
        self.assertTrue(hasattr(plac, "city_id"))
        if models.storage_t == 'db':
            self.assertEqual(plac.city_id, None)
        else:
            self.assertEqual(plac.city_id, "")

    def test_user_id_attr(self):
        """Test Place has attr user_id, and it's an empty string"""
        plac = Place()
        self.assertTrue(hasattr(plac, "user_id"))
        if models.storage_t == 'db':
            self.assertEqual(plac.user_id, None)
        else:
            self.assertEqual(plac.user_id, "")

    def test_name_attr(self):
        """Test Place has attr name, and it's an empty string"""
        plac = Place()
        self.assertTrue(hasattr(plac, "name"))
        if models.storage_t == 'db':
            self.assertEqual(plac.name, None)
        else:
            self.assertEqual(plac.name, "")

    def test_description_attr(self):
        """Test Place has attr description, and it's an empty string"""
        plac = Place()
        self.assertTrue(hasattr(plac, "description"))
        if models.storage_t == 'db':
            self.assertEqual(plac.description, None)
        else:
            self.assertEqual(plac.description, "")

    def test_number_rooms_attr(self):
        """Test Place has attr number_rooms, and it's an int == 0"""
        plac = Place()
        self.assertTrue(hasattr(plac, "number_rooms"))
        if models.storage_t == 'db':
            self.assertEqual(plac.number_rooms, None)
        else:
            self.assertEqual(type(plac.number_rooms), int)
            self.assertEqual(plac.number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """Test Place has attr number_bathrooms, and it's an int == 0"""
        plac = Place()
        self.assertTrue(hasattr(plac, "number_bathrooms"))
        if models.storage_t == 'db':
            self.assertEqual(plac.number_bathrooms, None)
        else:
            self.assertEqual(type(plac.number_bathrooms), int)
            self.assertEqual(plac.number_bathrooms, 0)

    def test_max_guest_attr(self):
        """Test Place has attr max_guest, and it's an int == 0"""
        plac = Place()
        self.assertTrue(hasattr(plac, "max_guest"))
        if models.storage_t == 'db':
            self.assertEqual(plac.max_guest, None)
        else:
            self.assertEqual(type(plac.max_guest), int)
            self.assertEqual(plac.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test Place has attr price_by_night, and it's an int == 0"""
        plac = Place()
        self.assertTrue(hasattr(plac, "price_by_night"))
        if models.storage_t == 'db':
            self.assertEqual(plac.price_by_night, None)
        else:
            self.assertEqual(type(plac.price_by_night), int)
            self.assertEqual(plac.price_by_night, 0)

    def test_latitude_attr(self):
        """Test Place has attr latitude, and it's a float == 0.0"""
        plac = Place()
        self.assertTrue(hasattr(plac, "latitude"))
        if models.storage_t == 'db':
            self.assertEqual(plac.latitude, None)
        else:
            self.assertEqual(type(plac.latitude), float)
            self.assertEqual(plac.latitude, 0.0)

    def test_longitude_attr(self):
        """Test Place has attr longitude, and it's a float == 0.0"""
        plac = Place()
        self.assertTrue(hasattr(plac, "longitude"))
        if models.storage_t == 'db':
            self.assertEqual(plac.longitude, None)
        else:
            self.assertEqual(type(plac.longitude), float)
            self.assertEqual(plac.longitude, 0.0)

    @unittest.skipIf(models.storage_t == 'db', "not testing File Storage")
    def test_amenity_ids_attr(self):
        """Test Place has attr amenity_ids, and it's an empty list"""
        plac = Place()
        self.assertTrue(hasattr(plac, "amenity_ids"))
        self.assertEqual(type(plac.amenity_ids), list)
        self.assertEqual(len(plac.amenity_ids), 0)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(type(new_d), dict)
        self.assertFalse("_sa_instance_state" in new_d)
        for attr in p.__dict__:
            if attr is not "_sa_instance_state":
                self.assertTrue(attr in new_d)
        self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        times_format = "%Y-%m-%dT%H:%M:%S.%f"
        p = Place()
        new_d = p.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], p.created_at.strftime(times_format))
        self.assertEqual(new_d["updated_at"], p.updated_at.strftime(times_format))

    def test_str(self):
        """test that the str method has the correct output"""
        plac = Place()
        string = "[Place] ({}) {}".format(plac.id, plac.__dict__)
        self.assertEqual(string, str(plac))
