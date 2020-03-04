# -*-coding:utf-8-*-
# @Time       :2020/2/29 18:31
# @Autor      :DAN HUI
# @Email      :icewong401@163.com
# @File       :test_企业微信.py
# @Software   :PyCharm
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#>chrome --remote-debugging-port=9222

class TestHome():
    def setup(self):
        chromeOptions = Options()
        chromeOptions.add_experimental_option("debuggerAddress","127.0.0.1:9222")
        # address = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
        self.driver = webdriver.Chrome(options=chromeOptions)
        self.driver.implicitly_wait(10)
        print(self.driver.title)


    def test_home(self):
        self.driver.find_element(By.ID,"menu_contacts").click()
        self.driver.find_element(By.CSS_SELECTOR,'.js_has_member div:nth-child(1) .js_add_member').click()
        time.sleep(3)
        self.driver.find_element(By.ID,'username').send_keys('icewang')
        time.sleep(1)
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys('i122325')
        time.sleep(1)
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys('13653485475')
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "qui_btn ww_btn js_btn_save'][1]").click()