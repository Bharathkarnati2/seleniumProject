import time

from selenium.webdriver.common.by import By


class ShopPage:
    def __init__(self,driver):
        self.driver = driver

    def add_to_cart(self,productList):
        added_products = []
        products = self.driver.find_elements(By.XPATH,"//div[@class ='card h-100']")
        for product in products:
            product_name = product.find_element(By.XPATH,"div/h4/a").text
            if product_name in productList:
                product.find_element(By.XPATH,"div/button").click()
                added_products.append(product_name)
        return added_products




