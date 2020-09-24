#!/usr/bin/python3

""" Singly Linked List Module """


class Node:
    """ Represents a node. """

    def __init__(self, data, next_node=None):
        """ Initializes a new node.

        Args:
            data (int): Data to store in the node.
            next_node (Node): The following node. Defaults to None.

        Attributes:
            __data (int): Private. Stored data in the node.
            __next_node (Node): Private. Next node.

        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ Sets and returns 'data' value. """
        return self.__data

    @data.setter
    def data(self, value):
        """ Verifies that value is integer, otherwise rises
            TypeError exception. """
        if type(value) is int:
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """ Sets and returns 'next_node' value. """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ Verifies that value is an Node object or None, otherwise rises
            TypeError exception. """
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """ Represents a singly linked list. """
    def __init__(self):
        """ Initializes the list.

            Attribute:
                __head (Node): Private. First node in the list.

        """
        __head = None

    def sorted_insert(self, value):
        """ Adds a new node to the list in a sorted manner.

        Args:
            value (Node): Node to add to the list.

        """
        if __head is None:
            __head = value
        else:
            temp = __head
            while temp.next_node is not None and
            temp.next_node.data < value.data:
                temp = temp.next_node
