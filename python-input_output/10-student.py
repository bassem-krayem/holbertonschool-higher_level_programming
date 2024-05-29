#!/usr/bin/python3
""" This module defines a `Student` class."""


class Student:
    """
    Represents a student with attributes for their first name, last name,
    and age.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of the Student instance.
        If attrs is a list of strings, only the attributes named in the list
        are included in the returned dictionary.

        Args:
            attrs (list, optional): A list of attribute names (strings)
            to include in the returned dictionary.
                                     If None, all attributes are included.

        Returns:
            dict: A dictionary containing the specified attributes of
            the Student instance.
                  If attrs is None or not a list of strings, all attributes
                  are included.
        """
        new_dict = {}

        # If no specific attributes are requested, return the full dictionary
        if attrs is None:
            return self.__dict__

        # Check if attrs is a list
        if isinstance(attrs, list):
            # Iterate over each element in the list
            for element in attrs:
                # Ensure each element is a string
                if isinstance(element, str):
                    # Check if the attribute exists in the object's dictionary
                    if element in self.__dict__:
                        # Add the attribute to the new dictionary
                        new_dict[element] = self.__dict__[element]
                else:
                    return self.__dict__

            return new_dict

        return self.__dict__
