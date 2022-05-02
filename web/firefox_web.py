# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/27 11:11 上午
@file: firefox_web.py
@desc: 
"""
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://ceshiren.com/")
