# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/27 2:47 下午
@file: web_browser.py
@desc: 
"""
# 打开浏览器
import time

from selenium import webdriver


def open_browser():
    driver = webdriver.Chrome()
    # 调用get 方法时需要传递浏览器的URL
    driver.get("https://ceshiren.com/")
    time.sleep(2)
    # 刷新浏览器
    driver.refresh()

    # 通过get调到百度
    driver.get("https://www.baidu.com/")
    # 退回上一步
    driver.back()

    # 浏览器最大化
    driver.maximize_window()
    time.sleep(2)
    driver.minimize_window()
    time.sleep(2)




# 最大化


# 最小化


if __name__ == '__main__':
    # 1.打开浏览器
    # 2.刷新浏览器
    open_browser()
