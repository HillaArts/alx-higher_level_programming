#!/usr/bin/python3
"""
Read_file location

Author: Lauren Mugabo Inkingi
"""

def read_file(filename=""):
    """Function that reads the file and prints its contents to stdout
    
    Args:
        filename (str): the filename to open
    """
    with open(filename, encoding='utf-8') as f:
        for l in f:
            print(l, end="")
            
