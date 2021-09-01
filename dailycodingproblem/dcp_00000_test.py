"""
TAGs: #dailycodingproblem
URL: https://www.dailycodingproblem.com/

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
import itertools
import typing

import pytest

import dcp_00000 as dcp


TEST_CASES = [
    {
        'arguments': {
            'nums': [10, 15, 3, 7],
            'k': 17,
        },
        'answer': True,
    }, {
        'arguments': {
            'nums': [],
            'k': 17,
        },
        'answer': False,
    }, {
        'arguments': {
            'nums': [17],
            'k': 17,
        },
        'answer': False,
    },
]


def solve(nums: typing.List[int], k: int) -> bool:
    seens = set()

    for num in nums:
        if k - num in seens:
            return True
        seens.add(num)

    return False


@pytest.mark.parametrize(
    'function, case',
    list(itertools.product([solve, dcp.solve], TEST_CASES)),
)
def test_solution(function, case):
    assert function(**case['arguments']) == case['answer']
