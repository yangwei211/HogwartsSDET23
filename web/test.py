import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestDefaultSuite():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_ceshiren(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1021, 977)
        self.driver.find_element(By.LINK_TEXT, "热门").click()
        time.sleep(5)

    def test_ceshiren2(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.set_window_size(1021, 977)
        self.driver.find_element(By.LINK_TEXT, "精华帖").click()
        time.sleep(5)
