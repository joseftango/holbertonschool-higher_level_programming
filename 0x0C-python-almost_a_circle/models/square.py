#!/usr/bin/python3
"""Square module
This module defines a Square class
"""
from models.rectangle import Rectangle
"""import rectangle model"""


class Square(Rectangle):
    """a Square class that inherited from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
