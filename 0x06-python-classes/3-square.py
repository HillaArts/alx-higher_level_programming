#!/usr/bin/python3
""""Define an empty class"""


class Square:
    ''' a class named square'''
    __size = None

    def __init__(self, size=0):
        '''Initializes class'''
        if size != int(size):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        '''Returns the current area square'''
        return(self.__size ** 2)
