# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/17 8:45 上午
@file: test_fieturedemo1.py
@desc: 
"""
# fixture的作用域
"""
@pytest.fixture
def fixture_name():
    setup 操作
    yield 返回值
    teardown 操作
"""

def test_search(login):
    token,username = login
    print(f"token: {token} ,name : {username}")
    # login返回None
    print("搜索")


def test_get_product(login, connectDB):
    print("验证 获取单品信息")

def test_cart(login):
    print("购物车")


def test_order(login):
    print("下单")


class TestDemo:
    def test_case1(self, login):
        print("case 1")

    def test_case2(self, login):
        print("case 2")
