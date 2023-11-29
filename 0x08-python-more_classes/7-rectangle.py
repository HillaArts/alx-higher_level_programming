#!/usr/bin/python3
"""Rectangle empty class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Area of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Perimeter of a rectangle"""
        if 0 in (self.__height, self.__width):
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        '''Returns string representation.'''
        if not self.width or not self.height:
            return ""
        return ((str(self.print_symbol) *
                 self.width + "\n") * self.height)[:-1]

    def __repr__(self):
        '''Returns formal string representation...'''
        return "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"

    def __del__(self):
        '''Called at instance deletion.'''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
