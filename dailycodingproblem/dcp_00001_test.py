"""
TAGs: #dailycodingproblem, #hard
URL: https://www.dailycodingproblem.com/

Given an array of integers, return a new array such that each element at index
i of the new array is the product of all the numbers in the original array
except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be
[2, 3, 6].

Follow-up: what if you can't use division?
"""
import itertools
import operator
import typing

import pytest

import dailycodingproblem.dcp_00001 as dcp



def solve(nums: typing.List[int]) -> typing.List[int]:
    ans, prod = list(itertools.accumulate(nums, operator.mul)), 1

    for i in range(len(nums)):
        ans[~i] = prod * (ans[~i - 1] if i + 1 < len(nums) else 1)
        prod *= nums[~i]

    return ans


@pytest.mark.parametrize(
    'case',
    [
        {
            'arguments': {'nums': [1, 2, 3, 4, 5]},
            'answer': [120, 60, 40, 30, 24],
        }, {
            'arguments': {'nums': [1, 2, 3, 4, 5, 0]},
            'answer': [0, 0, 0, 0, 0, 120],
        }, {
            'arguments': {'nums': [3, 2, 1]},
            'answer': [2, 3, 6],
        }, {
            'arguments': {'nums': []},
            'answer': [],
        }, {
            'arguments': {'nums': [2]},
            'answer': [1],
        },
    ],
)
def test_solution(develop, case):
    if develop:
        function = solve
    else:
        function = dcp.solve

    assert function(**case['arguments']) == case['answer']
