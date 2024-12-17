#!/usr/bin/python3
"""1-rectangle module"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        eval(self.__class__.__name__).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """method that calculates area"""
        return self.height * self.width

    def perimeter(self):
        """method that calculates the perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        """returns a string rectangle with the character #"""
        res = ''
        if self.height == 0 or self.width == 0:
            return res

        for i in range(self.height):
            for j in range(self.width):
                res += str(self.print_symbol)
            if i != self.height - 1:
                res += '\n'

        return res

    def __repr__(self):
        """return a string representation of the
        rectangle to be able to recreate a new instance"""
        return f'{type(self).__name__}({self.width}, {self.height})'

    def __del__(self):
        """print message when an object
        of rectangle is deleted"""
        eval(self.__class__.__name__).number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() == rect_2.area():
            return rect_1
        elif rect_1.area() > rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance
        with same value as height as width"""
        return eval(cls.__name__)(size, size)
