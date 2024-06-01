#!/usr/bin/python3
"""
Module for serializing and deserializing dictionaries with XML.

This module provides two functions:
1. serialize_to_xml: Converts a dictionary into an XML file.
2. deserialize_from_xml: Converts an XML file back into a dictionary.

Functions:
    - serialize_to_xml(dictionary, filename)
    - deserialize_from_xml(filename)
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the file to save the XML data.

    Example:
        data = {'name': 'John', 'age': 30}
        serialize_to_xml(data, 'output.xml')
    """
    root = ET.Element("root")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a dictionary.

    Args:
        filename (str): The name of the XML file to read.

    Returns:
        dict: The deserialized dictionary.

    Example:
        data = deserialize_from_xml('output.xml')
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for child in root:
        data[child.tag] = child.text

    return data
