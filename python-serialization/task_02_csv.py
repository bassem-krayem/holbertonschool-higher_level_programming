#!/usr/bin/python3
"""
Module for converting CSV files to JSON format.

This module provides a function to convert a CSV file to a JSON file.

Functions:
    - convert_csv_to_json(csv_file)
"""

import csv
import json


def convert_csv_to_json(csv_file):
    """
    Convert a CSV file to a JSON file.

    Args:
        csv_file (str): The path to the CSV file to be converted.

    Returns:
        bool: True if the conversion is successful, False
        if the file is not found.

    Example:
        success = convert_csv_to_json('input.csv')
    """
    try:
        data = []
        with open(csv_file, 'r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

        return True

    except FileNotFoundError:
        return False
