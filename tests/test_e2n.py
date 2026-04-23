import json

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Pages.LoginPage import LoginPage
from Pages.checkoutPage import CheckoutPage
from Pages.shopPage import ShopPage


def userdata():
    with open("data/data.json", 'r') as file:
        userData = json.load(file)
        return userData['users']

@pytest.mark.parametrize("users", userdata())
def test_e2e(driver, users):

    login_page = LoginPage(driver)
    login_page.navigate()

    if users['type'].lower() == 'valid':
        login_page.login(users['username'],users['password'])
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h4[@class='card-title']"))
        )
        shop_page = ShopPage(driver)
        productList = ["Blackberry", "Nokia Edge"]
        expectList = shop_page.add_to_cart(productList)
        assert set(expectList) == set(productList)


        checkout_page = CheckoutPage(driver)
        checkout_page.checkout_flow()

    else:
        login_page.login(users['username'], users['password'])
        message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert"))
        )
        assert "incorrect username/password" in message.text.lower()

