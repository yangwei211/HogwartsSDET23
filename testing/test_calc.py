# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/10 3:27 下午
@file: test_calc.py
@desc: 
"""

import pytest
from pythoncode.calculator import Calculator


class TestCalculator:
    def setup_class(self):
        print("实例化calculator对象")
        self.calc = Calculator()

    def setup(self):
        print("开始计算")

    def teardown(self):
        print("结束计算")

    def teardown_class(self):
        print("结束测试")

    # 冒烟测试用例
    @pytest.mark.P0
    # 需要至少两个参数，第一个是字符串，里面存放要传递的参数，以逗号隔开
    # 第二个参数，就是我们要传递的数据序列（可以列表，可以元组），每个序列里存刚一组数据
    @pytest.mark.parametrize('a,b,expected', [[1, 1, 2],
                                              [-0.01, 0.02, 0.01],
                                              [10, 0.02, 10.02]],
                             ids=['整型', '浮点型', '整型+浮点型'])
    def test_add0(self, a, b, expected):
        # 测试相加方法
        result = self.calc.add(a, b)
        # 实际结果 对比预期结果
        assert result == expected

    # 有效边界值
    @pytest.mark.P1
    @pytest.mark.parametrize('a,b,expected', [[98.99, 99, 197.99],
                                              [99, 98.99, 197.99],
                                              [-98.99, -99, -197.99],
                                              [-99, -98.99, -197.99]],
                             ids=['边界值-正1', '边界值-正2', '边界值-负1', '边界值-负2'])
    def test_add1(self, a, b, expected):
        result = self.calc.add(a, b)
        assert result == expected

    # 无效边界值
    @pytest.mark.P1
    @pytest.mark.parametrize('a,b,expected', [[99.01, 0, "参数大小超出范围"],
                                              [-99.01, -1, "参数大小超出范围"],
                                              [2, 99.01, "参数大小超出范围"],
                                              [1, -99.01, "参数大小超出范围"],
                                              ],
                             ids=['边界值-参数超出范围1',
                                  '边界值-参数超出范围2',
                                  '边界值-参数超出范围3',
                                  '边界值-参数超出范围4'])
    def test_add2(self, a, b, expected):
        result = self.calc.add(a, b)
        assert result == expected

    # @pytest.mark.P1
    # @pytest.mark.parametrize('a,b,expected', [[99.01, 0, "参数大小超出范围"],
    #                                       [-99.01, -1, "参数大小超出范围"],
    #                                       [2, 99.01, "参数大小超出范围"],
    #                                       [1, -99.01, "参数大小超出范围"],
    #                                       ],
    #                      ids=['边界值-参数超出范围1',
    #                           '边界值-参数超出范围2',
    #                           '边界值-参数超出范围3',
    #                           '边界值-参数超出范围4'])
    # 异常情况处理
    @pytest.mark.P1
    @pytest.mark.parametrize('a,b,errortype', [
        ["文", 9.3, TypeError],
        [4, "字", TypeError]
    ])
    def test_add3(self, a, b, errortype):
        # pytest封装的一种处理异常的方式
        with pytest.raises(errortype) as e:
            result = self.calc.add(a, b)
        print(e.typename)
        # try:
        #     result = self.calc.add("中", 9.3)
        #     # 1/0
        # except TypeError as e:
        #     print("异常信息:")
        #     print(e)
