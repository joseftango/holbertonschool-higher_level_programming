#!/usr/bin/python3
"""module of class Node"""


class Node:
    """class Node"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """SinglyLinkedList class"""
    def __init__(self):
        self.__head = None

    def __str__(self):
        """print list nodes line by line"""
        current = self.__head
        str = ''
        while current:
            str = str + f'{current.data}' + '\n'
            current = current.next_node
        str = str[:-1]
        return str

    def sorted_insert(self, value):
        """method that insert node in sorted way"""
        new = Node(value)
        if self.__head is None:
            new.next_node = self.__head
            self.__head = new

        elif self.__head.data >= new.data:
            new.next_node = self.__head
            self.__head = new

        else:
            current = self.__head
            while current.next_node is not None and \
                    current.next_node.data < new.data:
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new
