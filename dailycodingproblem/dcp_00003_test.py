"""
TAGs: #dailycodingproblem
URL: https://www.dailycodingproblem.com/

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.
"""
import typing

import pytest

import dailycodingproblem.dcp_00003 as dcp


def solve(nums: typing.List[int]):
    n = len(nums)

    for i in range(n):
        while 0 < nums[i] <= n and nums[i] != i + 1 and nums[i] != nums[nums[i] - 1]:
            j = nums[i]

            nums[i], nums[j - 1] = nums[j - 1], nums[i]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


@pytest.mark.parametrize(
    'case',
    [
        {
            'arguments': {
                'nums': [3, 4, -1, 1],
            },
            'answer': 2,
        }, {
            'arguments': {
                'nums': [1, 2, 0],
            },
            'answer': 3,
        }, {
            'arguments': {
                'nums': [0, 0],
            },
            'answer': 1,
        }, {
            'arguments': {
                'nums': [],
            },
            'answer': 1,
        }, {
            'arguments': {
                'nums': [-1],
            },
            'answer': 1,
        }, {
            'arguments': {
                'nums': [1, 2, 3, 4],
            },
            'answer': 5,
        }, {
            'arguments': {
                'nums': [1, 1, 1],
            },
            'answer': 2,
        }, {
            'arguments': {
                'nums': [4, 4, 4, 4, 4],
            },
            'answer': 1,
        },
    ],
)
def test_solution(develop, case):
    if develop:
        function = solve
    else:
        function = dcp.solve

    assert function(**case['arguments']) == case['answer']
