from selenium.webdriver.common.by import By
from trio import sleep_forever

from utills.utils import wait_for_clickable


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    # def go_to_checkout(self):
    #     element = wait_for_clickable(
    #         self.driver,
    #         (By.XPATH, "//a[contains(@class,'nav-link') and contains(text(),'Checkout')]")
    #     )
    #     element.click()
    def go_to_checkout(self):
        locator = (By.CSS_SELECTOR, "a.nav-link.btn.btn-primary")

        element = wait_for_clickable(self.driver, locator)

        # Scroll (CRITICAL for headless)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

        # Small stabilization delay
        import time
        time.sleep(1)

        # JS click (bypass interactable issue)
        self.driver.execute_script("arguments[0].click();", element)

    def confirm_checkout(self):
        element = wait_for_clickable(
            self.driver,
            (By.XPATH, "//button[contains(@class,'btn') and contains(text(),'Checkout')]")
        )
        element.click()

    def select_country(self, location):
        self.driver.find_element(By.ID, "country").send_keys(location)

        locator = (By.XPATH, f"//li[contains(normalize-space(),'{location}')]")
        element = wait_for_clickable(self.driver, locator)
        element.click()

    def accept_terms(self):
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()

    def purchase(self):
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()

    def get_success_message(self):
        return self.driver.find_element(
            By.XPATH, "//div[@class='alert alert-success alert-dismissible']"
        ).text

    def checkout_flow(self):

        self.go_to_checkout()
        self.confirm_checkout()
        self.select_country("India")
        self.accept_terms()
        self.purchase()

        message = self.get_success_message()

        assert "Your order will be delivered" in message