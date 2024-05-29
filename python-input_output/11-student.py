#!/usr/bin/python3
"""Create student class"""


class Student:
    """Class representing a student"""

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
            dict: A dictionary containing the specified attributes of the
            Student instance.
                  If attrs is None or not a list of strings, all attributes
                  are included.
        """
        new_dict = {}
        if attrs is None:
            return self.__dict__
        if type(attrs) is list:
            for elements in attrs:
                if type(elements) is str:
                    dict = self.__dict__
                    if elements in dict:
                        new_dict[elements] = dict[elements]
                else:
                    return self.__dict__
            return new_dict

    def reload_from_json(self, json):
        """
        Replaces all attributes of the
        Student instance with the values from the json dictionary.

        Args:
            json (dict): A dictionary containing new attribute
            values for the Student instance.
        """
        for key, value in json.items():
            self.__dict__[key] = value
