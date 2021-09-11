"""
TAGs: #leetcode, #hard, #leetcode_224
URL: https://leetcode.com/problems/basic-calculator/

224. Basic Calculator
"""


def calculate(s: str) -> int:
    """
    1.  treats substraction like minus sign. e.g. 1 - 2 -> 1 + (-2)
    2.  flips signs when there is a '(' or ')', use stack. e.g.
        1 - (2 - (3 + 4)) -> 1 - 2 + 3 + 4
    """
    ans, num, signs, prev_sign = 0, 0, [1], 1

    for c in filter(lambda x: x != ' ', s):
        if c == '+':
            ans += signs[-1] * prev_sign * num

            num = 0
            prev_sign = 1
        elif c == '-':
            ans += signs[-1] * prev_sign * num

            num = 0
            prev_sign = -1
        elif c == '(':
            signs.append(signs[-1] * prev_sign)

            num = 0
            prev_sign = 1
        elif c == ')':
            ans += signs[-1] * prev_sign * num

            num = 0
            signs.pop()
        else:
            num = 10 * num + int(c)

    ans += signs[-1] * prev_sign * num

    return ans


def test():
    assert calculate('123') == 123
    assert calculate('12+13') == 25
    assert calculate('12-13') == -1
    assert calculate('- 11 - 12') == -23
    assert calculate(' ( 11 + 22) ') == 33
    assert calculate('- ( 11 + 22) ') == -33
    assert calculate('1+( 2-(3 +4)- 5)') == -9
    assert calculate('1+( 2-(3 +4)- 5) + 99 ') == 90

    # extra cases
    assert calculate('+1+( +2-(+3 +4)- 5) + 99 ') == 90