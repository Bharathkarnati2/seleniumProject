import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def driver(request):
    browser = request.config.getoption("browser")

    if browser == "chrome":
        chrome_options = ChromeOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }

        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("--disable-infobars")

        driver = webdriver.Chrome(options=chrome_options)

    elif browser == "edge":
        edge_options = EdgeOptions()

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False
        }

        edge_options.add_experimental_option("prefs", prefs)
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-infobars")

        driver = webdriver.Edge(options=edge_options)

    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.maximize_window()
    yield driver
    driver.quit()