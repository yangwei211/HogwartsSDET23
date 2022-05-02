# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/10 9:39 下午
@file: test_dke.py
@desc: 
"""
import pytest

@pytest.mark.parametrize("wd",["appium","selenium","pytest"])
@pytest.mark.parametrize("code",["utf-8","gbk","gb2323"])
def test_dke(wd,code):
    print(f"wd: {wd}, code: {code}")