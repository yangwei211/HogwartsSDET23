# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/10 3:44 下午
@file: conftest.py
@desc: 
"""
# conftest.py 文件中的函数是不需要导入的

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
