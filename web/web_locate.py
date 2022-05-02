# encoding: utf-8
"""
@author: yangwei
@contact: yangchen211@126.com
@time: 2022/4/27 3:16 下午
@file: web_locate.py
@desc: 
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


def web_locate():
    # 首先需要实例化driver对象
    driver = webdriver.Chrome()
    # 打开一个网页
    driver.get("https://vip.ceshiren.com/#/ui_study")
    # 1.ID定位, 第一份参数传递定位方式,第二参数传递定位元素，调用整个方法的返回值为WebElement
    # web_element = driver.find_element(By.ID, "locate_id")
    # print(web_element)
    # 2.Name定位
    # driver.find_element(By.NAME, "locate")
    # 3.CSS选择器定位
    # driver.find_element(By.CSS_SELECTOR, "#locate_id > a > span")
    # 4.XPATH选择器定位
    # driver.find_element(By.XPATH, '//*[@id="locate_id"]/a/span')
    # 5. 通过链接文本的方式 （1）元素一定是a标签 （2）输入的元素为标签内的文本
    driver.find_element(By.LINK_TEXT, "元素定位")

if __name__ == '__main__':
    web_locate()