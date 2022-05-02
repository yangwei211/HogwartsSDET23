# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/28 10:15 上午
@file: web_wait.py
@desc: 
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def wait_sleep():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # time.sleep(2)
    driver.implicitly_wait(4)
    driver.find_element(By.XPATH, "//*[text()='个人中心']")
    driver.find_element(By.XPATH, "//*[text()='题库']")

def wait_show():
    driver = webdriver.Chrome()
    driver.get("https://vip.ceshiren.com/#/ui_study")
    driver.implicitly_wait(5)
    # 问题：元素可以找到，但是点击效果没有触发
    # 原因：
    WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
        (By.ID, "success_btn")))
    driver.find_element(By.ID, "success_btn").click()
    time.sleep(3)


if __name__ == '__main__':
    # wait_sleep()
    wait_show()
