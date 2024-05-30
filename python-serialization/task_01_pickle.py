#!/usr/bin/python3
"""
This module defines a `CustomObject` class that can be serialized to and
deserialized from a file using the `pickle` module. This allows for
persisting instances of the class between program runs.

Classes:
- CustomObject: A class representing a custom object with attributes for
  name, age, and student status. The class includes methods for displaying
  the object attributes, and for serializing/deserializing the object to/from
  a file.
"""

import pickle
import os


class CustomObject:
    """
    A custom object class that contains attributes for name, age, and student
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize object and save it
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception as e:
            return (None)

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize object and load it
        """
        try:
            if not os.path.exists(filename):
                return (None)
            with open(filename, 'rb') as file:
                return (pickle.load(file))
        except Exception as e:
            return (None)
