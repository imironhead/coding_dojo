"""
An XOR linked list is a more memory efficient doubly linked list. Instead of
each node holding next and prev fields, it holds a field named both, which is
an XOR of the next node and the previous node. Implement an XOR linked list; it
has an add(element) which adds the element to the end, and a get(index) which
returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to get_pointer and dereference_pointer functions that converts
between nodes and memory addresses.
"""
import typing


class Node:

    def __init__(self, val: typing.Any) -> None:
        self._val = val
        self._link = 0


class LinkedList:

    def __init__(self) -> None:
        pass

    def add(self, val: typing.Any) -> None:
        pass

    def get(self, index: int) -> typing.Any:
        pass


NODE_TO_POINTER = {None: 0}
POINTER_TO_NODE = {0: None}


def get_pointer(node: Node) -> int:
    if node not in NODE_TO_POINTER:
        pointer = len(NODE_TO_POINTER)

        NODE_TO_POINTER[node] = pointer
        POINTER_TO_NODE[pointer] = node

    return NODE_TO_POINTER[node]


def dereference_pointer(pointer: int) -> Node:
    return POINTER_TO_NODE.get(pointer)
