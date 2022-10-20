#!/usr/bin/python3
"""a Node model"""


class Node:
    """class named Node"""
    def __init__(self, data, next_node=None):
        """initializing function"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """data getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """data setter"""
        if type(value) == int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """next_node getter"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter"""
        if type(value) == Node or type(value) is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:

    def __str__(self):
        """print a linked list"""
        my_str = ""
        trav = self.__head

        while trav:
            my_str += str(trav.data)
            if trav.__next_node is not None:
                my_str += "\n"
            trav = trav.__next_node

        return my_str

    def __init__(self):
        """initializing function"""
        self.__head = None

    def sorted_insert(self, value):
        """insertion sort"""
        new_node = Node(value)

        if self.__head is None:
            new_node.__next_node = self.__head
            self.__head = new_node

        elif self.__head.data >= new_node.data:
            new_node.__next_node = self.__head
            self.__head = new_node

        else:
            current = self.__head
            while current.__next_node is not None and\
                    current.__next_node.data < new_node.data:

                current = current.__next_node

            new_node.__next_node = current.__next_node
            current.__next_node = new_node
