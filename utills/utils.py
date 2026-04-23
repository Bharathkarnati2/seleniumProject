from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_clickable(driver, locator, timeout=25):
    wait = WebDriverWait(driver, timeout)

    element = wait.until(EC.presence_of_element_located(locator))
    wait.until(EC.visibility_of(element))

    return element


def wait_for_element(driver, locator, timeout=25):
    wait = WebDriverWait(driver, timeout)

    # Step 1: Wait for presence
    element = wait.until(EC.presence_of_element_located(locator))

    # Step 2: FORCE SCROLL (critical fix)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    # Step 3: small delay for rendering
    import time
    time.sleep(1)

    return element