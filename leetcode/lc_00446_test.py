"""
TAGs: #leetcode, #hard, #leetcode_446
URL: https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

446. Arithmetic Slices II - Subsequence
"""
import collections
import typing

import pytest

import leetcode.lc_00446 as lc


def count_arithmetic_slices(nums: typing.List[int]) -> int:
    # seqs[index][diff]: number of subsequences end at index with difference
    # "diff"
    ans, seqs = 0, [collections.defaultdict(int) for _ in nums]

    for idx, num in enumerate(nums):
        for jdx in range(idx):
            diff = num - nums[jdx]
            count = seqs[jdx][diff]
            seqs[idx][diff] += count
            ans += count

        for jdx in range(idx):
            seqs[idx][num - nums[jdx]] += 1

    return ans


@pytest.mark.parametrize(
    'case',
    [
        {
            'arguments': {
                'nums': [2, 4, 6, 8, 10],
            },
            'answer': 7,
        }, {
            'arguments': {
                'nums': [7, 7, 7, 7, 7],
            },
            'answer': 16,
        },
    ],
)
def test_solution(develop, case):
    if develop:
        function = count_arithmetic_slices
    else:
        function = lc.count_arithmetic_slices

    assert function(**case['arguments']) == case['answer']
