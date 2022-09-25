#!/usr/bin/python3
"""Definition of a singly linked list classes."""


class Node:
    """The Node class of a Singly Linked List.

    Attribute:
        data(Int): Data to be stored in the list.
        next_node(Node): The next node in the list.
    """

    def __init__(self, data, next_node=None):
        """Initialises a new node object.

        Args:
            data: What to add the the list.
            node_next: The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve node data"""
        return self.__data

    @property
    def next_node(self):
        """Retrieve the next node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """Add(Set) data to a node"""
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @next_node.setter
    def next_node(self, value):
        """Assign(Set) the next node"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list.

    Attribute:
        head(Node): The head of the linked list.
    """

    def __init__(self, head=None):
        """Initilaises a linked-list object

        Args:
            head: The head of a Node.
        """
        self.__head = head

    def sorted_insert(self, value):
        """Inserts a new node at sorted position.

        Args:
            value: Data to be added to the new node.
        """

        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and
                    temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """String Representation of the Singly linked list"""

        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        # print("=> ", len(values))

        return "\n".join(values)
