#!/usr/bin/python3
import json

def load_files():
    file_list = []
    return file_list

def json_to_txt(json_name):
    with open(json_name, 'r') as f:
        json_data = json.load(f)
        
    