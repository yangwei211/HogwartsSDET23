# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/17 10:02 上午
@file: conftest.py
@desc: 
"""
# conftest.py 名字是固定的，不能改变
import pytest


@pytest.fixture(scope="function",autouse=True)
def login():
    # setup操作
    print("完成登录操作")
    token = "abcdadsasda"
    username = "hogwarts"
    yield token,username  # 相当于return
    # teardown操作
    print("完成登出操作")

@pytest.fixture()
def connectDB():
    print("连接数据库")
    yield
    print("断开数据库")