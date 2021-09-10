"""
TAGs: #dailycodingproblem
URL: https://www.dailycodingproblem.com/

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

import dailycodingproblem.dcp_00005 as dcp


class Node:

    def __init__(self, val: typing.Any) -> None:
        self._val = val
        self._link = 0


class LinkedList:

    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def add(self, val: typing.Any) -> None:
        node = Node(val)

        if self._tail:
            pointer_temp = get_pointer(node)
            pointer_tail = get_pointer(self._tail)

            node._link = pointer_tail

            self._tail._link = self._tail._link ^ pointer_temp
            self._tail = node
        else:
            self._head = self._tail = node

        self._size += 1

    def get(self, index: int) -> typing.Any:
        if 0 > index or index >= self._size:
            return None

        a, b, node = get_pointer(None), get_pointer(self._head), self._head

        while index:
            a, b = b, node._link ^ a

            node = dereference_pointer(b)

            index -= 1

        return node._val


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


def test_solution(develop):
    if develop:
        clazz = LinkedList
    else:
        clazz = dcp.LinkedList

    nums = [0, 1, 2, 3, 4]

    data = clazz()

    for idx, num in enumerate(nums):
        assert data.get(-1) is None
        assert data.get(idx) is None

        data.add(num)

        for jdx in range(idx + 1):
            assert data.get(jdx) == nums[jdx]

        assert data.get(idx + 1) is None
