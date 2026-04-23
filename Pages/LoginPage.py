import time

from pyexpat.errors import messages
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utills.utils import wait_for_clickable

import logging
logger = logging.getLogger(__name__)


class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    def navigate(self):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")

    def userName(self,username):
        self.driver.find_element(By.ID, "username").send_keys(username)

    def userPassword(self,password):
        self.driver.find_element(By.ID, "password").send_keys(password)

    def radioButton(self):
        self.driver.find_element(By.XPATH, "//span[@class='radiotextsty' and contains(text(),'User')]").click()

    def popUpButton(self):
        element = wait_for_clickable(self.driver, (By.XPATH, "//button[@id='okayBtn']"))
        element.click()

    def dropdownButton(self):
        dropdown = Select(self.driver.find_element(By.CSS_SELECTOR, "select[class='form-control']"))
        dropdown.select_by_value("teach")

    def submitButton(self):
        self.driver.find_element(By.ID, "signInBtn").click()

    def login(self,username,password):
        logger.info("In login page")
        self.userName(username)
        self.userPassword(password)
        self.radioButton()
        self.popUpButton()
        self.dropdownButton()
        self.submitButton()



