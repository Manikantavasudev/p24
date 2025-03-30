# conftest.py
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import allure
import logging
import pytest
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("test.log"), logging.StreamHandler()],
)
logger = logging.getLogger(__name__)

import pytest
import os
import pytest

def pytest_addoption(parser):
    parser.addoption("--test-ip", action="store", help="IP address for testing")

@pytest.fixture
def test_ip(request):
    return request.config.getoption("--test-ip")


# Constants for BA connection
BASE_URL = "http://localhost:2004/"
CONNECT_BTN_XPATH = "//button[@id='connectionsetup_connect_button']"
CONNECT_STATUS_XPATH = "//td[@class='panel-connection-setup-tester-info tester-info-border device-details-border']"
MAX_RETRIES = 15
INPUT_IP_XPATH = "//input[@class='rc-select-search__field']"

def connect_status(driver):
    """
    Navigates to BASE_URL and ensures the tester is connected.
    Retries connection attempts up to MAX_RETRIES.
    """
    driver.get(BASE_URL)
    for retry in range(MAX_RETRIES):
        try:
            status = driver.find_element(By.XPATH, CONNECT_STATUS_XPATH).text
            if status == "Connected":
                print("Tester is already connected.")
                break
            ip_field = driver.find_element(By.XPATH, INPUT_IP_XPATH)
            ip_field.clear()
            ip_field.send_keys("192.168.5.13")
            time.sleep(2)
            connect_btn = driver.find_element(By.XPATH, CONNECT_BTN_XPATH)
            connect_btn.click()
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, CONNECT_STATUS_XPATH), "Connected")
            )
            print("Tester connected successfully.")
            break
        except (NoSuchElementException, TimeoutException) as e:
            print(f"Retry {retry + 1}: {e}")
            if retry == MAX_RETRIES - 1:
                pytest.fail("Failed to connect after maximum retries.")
        # Handle any pop-ups
        try:
            popup = WebDriverWait(driver, 2).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='OK']"))
            )
            popup.click()
            print("Clicked 'OK' on pop-up.")
        except (NoSuchElementException, TimeoutException):
            pass
    final_status = driver.find_element(By.XPATH, CONNECT_STATUS_XPATH).text
    assert final_status == "Connected", "Tester is not connected after retries."

@pytest.fixture(scope="module")
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()

@pytest.fixture(scope="module")
def ba_connection(driver):
    """Ensures that the Browser Application is connected before any UI tests run."""
    connect_status(driver)
    return driver

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        logger.error(f"Test failed: {item.name}. Screenshot captured.")
