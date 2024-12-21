#!/usr/bin/python3
"""LockedClass
This class only allows first_name field
"""


class LockedClass(object):
    """LockedClass Class
    This class only allows first_name field
    """
    __slots__ = 'first_name'

    def __init__(self, first_name="") -> None:
        self.first_name = first_name
