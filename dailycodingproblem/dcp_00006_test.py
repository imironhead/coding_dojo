"""
TAGs: #dailycodingproblem, #medium
URL: https://www.dailycodingproblem.com/


Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as
'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.
"""
import typing

import pytest

import dailycodingproblem.dcp_00006 as dcp


def count_decodings(code: typing.List[int]):
    a = b = 1

    for i, x in enumerate(code):
        if x == 0 and (i == 0 or code[i - 1] not in (1, 2)):
            return 0

        if i and code[i - 1] == 0:
            a, b = b, b
            continue

        y = 0

        if x != 0:
            y += b

        if i and 1 <= code[i - 1] * 10 + code[i] <= 26:
            y += a

        a, b = b, y

    return b



@pytest.mark.parametrize(
    'case',
    [
        {
            # 1_2 / 12
            'arguments': {
                'code': [1, 2],
            },
            'answer': 2,
        }, {
            # 1_1_1 / 11_1 / 1_11
            'arguments': {
                'code': [1, 1, 1],
            },
            'answer': 3,
        }, {
            # 1_2 / 12
            'arguments': {
                'code': [1, 2],
            },
            'answer': 2,
        }, {
            # 2_2_6 / 22_6 / 2_26
            'arguments': {
                'code': [2, 2, 6],
            },
            'answer': 3,
        }, {
            # leading 0
            'arguments': {
                'code': [0, 1, 2, 3],
            },
            'answer': 0,
        }, {
            # 2_10_1
            'arguments': {
                'code': [2, 1, 0, 1],
            },
            'answer': 1,
        },
    ],
)
def test_solution(develop, case):
    if develop:
        function = count_decodings
    else:
        function = dcp.count_decodings

    assert function(**case['arguments']) == case['answer']
