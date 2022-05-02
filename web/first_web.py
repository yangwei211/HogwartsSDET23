# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/27 10:35 上午
@file: first_web.py
@desc: 
"""
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://ceshiren.com/")
driver.quit()
