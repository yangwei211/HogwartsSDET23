# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/17 8:45 上午
@file: test_fieturedemo1.py
@desc: 
"""
# fixture的作用域
import pytest

"""
@pytest.fixture
def fixture_name():
    setup 操作
    yield 返回值
    teardown 操作
"""

# 定义了登录的fixture，尽量避免以test_开头
# @pytest.fixture(scope="class")
# def login():
#     # setup操作
#     print("完成登录操作")
#     token = "abcdadsasda"
#     username = "hogwarts"
#     yield token,username  # 相当于return
#     # teardown操作
#     print("完成登出操作")


def test_search(login):
    token,username = login
    print(f"token: {token} ,name : {username}")
    # login返回None
    print("搜索")


def test_cart(login):
    print("购物车")


def test_order(login):
    print("下单")


class TestDemo:
    def test_case1(self, login):
        print("case 1")

    def test_case2(self, login):
        print("case 2")
