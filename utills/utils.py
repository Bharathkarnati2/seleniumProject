from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_clickable(driver, locator):
    wait = WebDriverWait(driver, 10)
    return wait.until(EC.element_to_be_clickable(locator))

# def wait_for_visible(driver, locator):
#     wait = WebDriverWait(driver, 10)
#     return wait.until(EC.element_to_be_visble(locator))