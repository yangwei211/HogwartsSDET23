# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/10 3:04 下午
@file: test_prams1.py
@desc: 
"""
import pytest

search_list = ['appium', 'selenium', 'pytest']


@pytest.mark.parametrize('name', search_list)
def test_search(name):
    assert name in search_list
