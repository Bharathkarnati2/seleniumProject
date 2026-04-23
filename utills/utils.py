from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_clickable(driver, locator, timeout=25):
    wait = WebDriverWait(driver, timeout)

    element = wait.until(EC.presence_of_element_located(locator))
    wait.until(EC.visibility_of(element))

    return element