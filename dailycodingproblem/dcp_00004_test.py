"""
TAGs: #dailycodingproblem
URL: https://www.dailycodingproblem.com/

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
last element of that pair. For example, car(cons(3, 4)) returns 3, and
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr
"""
import typing

import dailycodingproblem.dcp_00004 as dcp


def cons(a: typing.Any, b: typing.Any):
    def pair(f):
        return f(a, b)
    return pair


def car(cons_ab: typing.Any):
    return cons_ab(lambda x, _: x)


def cdr(cons_ab: typing.Any):
    return cons_ab(lambda _, y: y)


def test_solution(develop):
    if develop:
        fn_car, fn_cdr = car, cdr
    else:
        fn_car, fn_cdr = dcp.car, dcp.cdr

    assert fn_car(cons(0, 1)) == 0
    assert fn_cdr(cons(0, 1)) == 1

    assert fn_car(cons(0, '1')) == 0
    assert fn_cdr(cons(0, '1')) == '1'

    assert fn_car(cons('0', '1')) == '0'
    assert fn_cdr(cons('0', '1')) == '1'
