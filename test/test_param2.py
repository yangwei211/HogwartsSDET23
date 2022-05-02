# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/10 3:07 下午
@file: test_param2.py
@desc: 
"""
import pytest


# 1、参数化的名字，要与方法中的参数名一一对应
# 2、如果传递多个参数的话，要放在列表中，列表中嵌套列表或者元组
# 3、ids个数==传递的数据个数
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8), ("2+5", 7), ("7+5", 12)
], ids=["num1", "num2", "num3"])
def test_mark_more(test_input, expected):
    assert eval(test_input) == expected
