#!/usr/bin/python3
"""module for  Python - Input/Output
    """
import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


save_to_json_file(sys.argv[1:], "add_item.json")
my_list = load_from_json_file("add_item.json")
