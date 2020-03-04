# -*-coding:utf-8-*-
# @Time       :2019/12/29 15:44
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :seleium_learn-_001.py
# @Software   :PyCharm
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_testerhome():

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://testerhome.com/")

    def test_testerhome1(self):
        self.driver.find_element(By.LINK_TEXT, 'MTSC2020 中国互联网测试开发大会议题征集').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'caret')))
        self.driver.find_element(By.CLASS_NAME, 'caret').click()
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, '征集议题范围')))
        self.driver.find_element(By.LINK_TEXT, '征集议题范围').click()

    def teardown_method(self):
        time.sleep(2)
        self.driver.quit()