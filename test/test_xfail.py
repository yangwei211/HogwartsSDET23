# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/10 11:26 下午
@file: test_xfail.py
@desc: 
"""
import sys
import pytest

def test_xfail():
    print("******开始测试*****")
    pytest.xfail(reason='该功能尚未完成')
    print("测试过程")
    assert 1 == 1

@pytest.mark.xfail
def test_aaa():
    print("test xfail 方法执行")
    assert 1 == 2

xfail = pytest.mark.xfail

@xfail(reason="bug 110")
def test_hello4():
    assert 0