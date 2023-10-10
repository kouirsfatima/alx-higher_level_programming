#!/usr/bin/python3
""" function that returns the dictionary description with simple data structure 
(list, dictionary, string, integer and boolean)for JSON serialization of an object:."""


import json

class obj:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

def class_to_json(obj_instance):
    obj_dict = {
        "name": obj_instance.name,
        "age": obj_instance.age,
        "is_student": obj_instance.is_student
    }
    
    return json.dumps(obj_dict)
