#!/usr/bin/python3
"""
a class that prevents the user from dynamically creating new instance
attributes, except if the new instance attribute is called first_name.
"""


class LockedClass:
    """
    A class that restricts the creation of instance attributes
    to only `first_name`.

    This class uses the `__slots__` mechanism to define a fixed
    set of attributes
    that can be assigned to instances of the class.
    By using `__slots__`, the class
    avoids creating a `__dict__` for each instance, which
    reduces memory usage.

    Attributes:
        first_name (str): The only allowed attribute for instances of
        this class.
"""
    __slots__ = ['first_name']
