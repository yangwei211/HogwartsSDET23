# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/10 11:11 下午
@file: test_skip.py
@desc: 
"""
import pytest


@pytest.mark.skip
def test_aaa():
    print("代码未开发完")
    assert True


@pytest.mark.skip(reason="代码没用实现")
def test_bbb():
    assert False


def check_login():
    return False


def test_function():
    print("start")
    if not check_login():
        pytest.skip("unsupported configuration")
    print("end")
