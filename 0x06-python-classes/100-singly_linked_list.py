#!/usr/bin/python3
"""module on advanced class creation tasks"""


class Node:

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:

    def __init__(self):
        self.__head = None

    def __str__(self):
        current = self.__head
        output = ""
        while current:
            strng = str(current.data) + "\n"
            output += strng
            current = current.next_node
        return output

    def sorted_insert(self, value):
        temp = Node(data=value)
        if self.__head is None:
            self.__head = temp
        else:
            current = self.__head
            temp_current = self.__head
            unchecked = True
            if current.data > temp.data:
                temp2 = current
                self.__head = temp
                self.__head.next_node = temp2
                unchecked = False

            while unchecked:
                if temp_current.data > temp.data:
                    temp2 = temp_current
                    temp.next_node = temp2
                    current.next_node = temp
                    break
                if temp_current.next_node is None:
                    temp_current.next_node = temp
                    break
                current = temp_current
                temp_current = current.next_node
