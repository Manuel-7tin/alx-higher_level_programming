#!/usr/bin/python3
"""
This module demonstartes the act of creating json representations of object
"""
import json


def to_json_string(my_obj):
    """
    This function converts objects to their respective json representations
    """

    return json.dumps(my_obj)
