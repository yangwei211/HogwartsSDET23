# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/17 11:16 上午
@file: test_fixture_param.py
@desc: 
"""
import pytest


@pytest.fixture(params=[["selenium", 123], ["appium", 123456]])
def login(request):
    print(f"用户名: {request.param}")
    return request.param


def test_demo1(login):
    print(f"demo1 case: 数据为： {login}")
