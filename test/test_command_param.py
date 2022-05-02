# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/10 9:52 下午
@file: test_command_param.py
@desc: 
"""
import pytest


def double(a):
    return a * 2


@pytest.mark.int
def test_double_int():
    print("test double int")
    assert 2 == double(1)


@pytest.mark.minus
def test_double_minus():
    print("test double minus")
    assert -2 == double(-1)


@pytest.mark.float
def test_double_float():
    assert 0.2 == double(-0.1)


@pytest.mark.float
def test_double2_minus():
    assert -0.2 == double(-0.1)


@pytest.mark.zero
def test_double_zero():
    assert 10 == double(0)


@pytest.mark.bignum
def test_double_bignum():
    assert 200 == double(100)


@pytest.mark.str
def test_double_str():
    assert 'aa' == double('a')


@pytest.mark.str
def test_double_str1():
    assert 'a$a$' == double('a$')
