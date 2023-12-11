#!/usr/bin/python3
"""Module defining the Base class."""

class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instance of Base.

        Args:
            id (int): The identifier for the instance. If not provided,
                      increment the class attribute __nb_objects and assign
                      it to the public instance attribute id.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

if __name__ == "__main__":
    b1 = Base()
    print(b1.id)

    b2 = Base()
    print(b2.id)

    b3 = Base()
    print(b3.id)

    b4 = Base(12)
    print(b4.id)

    b5 = Base()
    print(b5.id)
