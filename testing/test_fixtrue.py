# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/17 2:55 下午
@file: test_fixtrue.py
@desc: 
"""
import pytest

@pytest.fixture(scope="class")
def login():
    print("准备登录")
    yield "username, password"
    # teardown
    print("登出操作")

@pytest.fixture
def conndb():
    print("conn db")

class TestDemo1:
    def test_demo1(self, login, conndb):
        print(f"登录信息, {login}")
        print("demo1")

    def test_demo2(self, login):
        print(f"登录信息, {login}")
        print("demo2")