#!/usr/bin/python3
import importlib.util
from inspect import getmembers, isfunction
# Define the module name and path
module_name = "hidden"
module_path = "hidden_4.pyc"
# Load the compiled module
spec = importlib.util.spec_from_file_location(module_name, module_path)
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)
for name, obj in getmembers(h):
    if isfunction(obj) and name != "__init__":
        print(name)