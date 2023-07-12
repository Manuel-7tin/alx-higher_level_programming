#!/usr/bin/python3
"""
This module shows the conversion of a strin to its object format using json
"""
import json


def from_json_string(my_str):
    """
    This function converts a string to it's object format using json
    """

    return json.loads(my_str)
