#!/usr/bin/python3
"""
An append_write function

Author:Lauren Mugabo Inkingi
"""

def append_write(filename="", text=""):
    """Appends text to a specified file
    
    Args: 
        filename (str): the file to open 
        text (str): the text to append to the file
    """

    with open(filename, mode='a', encoding='utf-8') as f:
        written = f.write(text)
    return written
