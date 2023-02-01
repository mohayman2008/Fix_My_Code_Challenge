#!/usr/bin/python3
"""
This Python module contains declaration of a weird Square Class
"""


class square():
    """ Weird Square Class """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Instance initialization """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """ Returns the perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Returns string representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
