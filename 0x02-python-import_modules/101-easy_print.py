#!/usr/bin/python3
import os

str = "#pythoniscool\n"
os.write(1, str.encode())
