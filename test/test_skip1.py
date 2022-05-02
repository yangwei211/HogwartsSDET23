# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/10 11:18 下午
@file: test_ski[1.py
@desc: 
"""
import sys
import pytest


@pytest.mark.skipif(sys.platform == 'darwin', reason="does not run on mac")
def test_case1():
    assert True

@pytest.mark.skipif(sys.platform == 'win', reason="does not run on windows")
def test_case2():
    assert True

@pytest.mark.skipif(sys.version_info< (3, 6), reason="requires Python3.6 or higher")
def test_case3():
    print(sys.version_info)
    assert True


