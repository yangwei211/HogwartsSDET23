# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/5/2 12:05 下午
@file: test_ceshiren.py
@desc: 
"""


# 使用pytest测试框架
# 用例标题=文件名+类名+方法名
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# ==========================优化1
# 问题：1.没有前置和后置的处理的动作 2.drive启动后没有做quit()动作
# 如果没有quit()动作，会导致大量的chromedriver进程一直存在

class TestCesguren:

    def setup(self):
        """
        前提条件：进入测试人论坛的搜索页面
        :return:
        """
        # 打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
        # 打开被测地址
        self.driver.get("https://ceshiren.com/search?expanded=true")

    def teardown(self):
        # 每一次用例结束一周都会关闭chromedriver进程，也会关闭浏览器
        self.driver.quit()

    def test_search(self):
        """
        测试步骤：1.输入搜索关键词
                 2.点击搜索按钮
                 预期结果/实际结果
        :return:
        """
        # 定位到输入搜索关键字
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='搜索']").send_keys("appium")
        # 定位到搜索按钮并点击
        self.driver.find_element(By.CSS_SELECTOR, ".search-cta").click()
        # 断言=预期结果和实际结果对比的结果
        # 获取实际结果，即为获取搜索结果列表的标题内容
        # 第一种方式，获取第一个搜索结果
        # time.sleep(3)  # 加一个3秒的时间等待，等待页面渲染完成
        web_element = self.driver.find_element(By.CSS_SELECTOR, ".topic-title")
        # 获取文本类的实际结果，断言appium关键字是否在获取的实际结果的文本中
        # 获取解决方案：
        # 1、统一，比如 断言Appium in
        # 2、就是把获取到的内容和预期结果统一, 使用lower()就可以使大小写统一
        assert "appium" in web_element.text.lower()


