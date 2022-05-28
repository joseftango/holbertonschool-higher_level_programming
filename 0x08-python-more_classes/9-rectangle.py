#!/usr/bin/python3
""""this is a Rectangle"""


class Rectangle:
    """"Rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """inisialising"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        a = self.width * self.height
        return a

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            p = 0
            return 0
        p = (self.width + self.height) * 2
        return p

    def __str__(self):
        st = ""
        if self.width == 0 or self.height == 0:
            return st
        for i in range(self.height):
            for j in range(self.width):
                st += str(self.print_symbol)
            if i != self.height-1:
                st += "\n"
        return st

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """square a class method that returns new argument of the class"""
        return cls(height=size, width=size)
