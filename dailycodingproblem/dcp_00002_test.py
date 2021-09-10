"""
TAGs: #dailycodingproblem, #medium
URL: https://www.dailycodingproblem.com/

Given the root to a binary tree, implement serialize(root), which serializes
the tree into a string, and deserialize(s), which deserializes the string back
into the tree.
"""
import pytest

import dailycodingproblem.dcp_00002 as dcp


class Node:
    def __init__(self, val: int, left: 'Node' = None, right: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right


def same_tree(tree_1, tree_2):
    if tree_1 and tree_2:
        return tree_1.val == tree_2.val \
            and same_tree(tree_1.left, tree_2.left) \
            and same_tree(tree_1.right, tree_2.right)
    else:
        return tree_1 is None and tree_2 is None


def serialize(root: Node) -> str:
    if root:
        return f'({root.val}{serialize(root.left)}{serialize(root.right)})'
    else:
        return '(*)'


def deserialize(s: str) -> Node:
    def _deserialize(i):
        if s[i + 1] == '*':
            return None, i + 3

        j, val = i + 1, 0

        while s[j] != '(':
            val = 10 * val + int(s[j])
            j += 1

        left, j = _deserialize(j)
        right, j = _deserialize(j)

        return Node(val, left=left, right=right), j + 1

    return _deserialize(0)[0]


@pytest.mark.parametrize(
    'case',
    [
        {
            'arguments': {
                'root': None,
            },
        }, {
            'arguments': {
                'root': Node(0),
            },
        }, {
            'arguments': {
                'root': Node(
                    0,
                    left=Node(1, left=Node(2)),
                    right=Node(3, right=Node(4))),
            },
        }, {
            'arguments': {
                'root': Node(
                    0,
                    left=Node(1, left=Node(2, left=Node(3, left=Node(4))))),
            },
        }, {
            'arguments': {
                'root': Node(
                    0,
                    left=Node(1, left=Node(2, left=Node(3), right=Node(4))),
                    right=Node(5, right=Node(4, left=Node(5), right=Node(6)))),
            },
        },
    ]
)
def test_solution(develop, case):
    if develop:
        encode, decode = serialize, deserialize
    else:
        encode, decode = dcp.serialize, dcp.deserialize

    root = decode(encode(**case['arguments']))

    assert same_tree(root, case['arguments']['root'])
