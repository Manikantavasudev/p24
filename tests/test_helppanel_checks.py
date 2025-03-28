from utilities.browser_setup import BrowserSetup
from pages.helppanel import HelpPanel
import logging
import pytest
import time
URL = "http://localhost:2004"
IP_ADDRESS = "192.168.5.77"
tpt_folder_path = r"C:\GRL\GRL-C3-MP-TPT\LogFiles\DebugLogger.log"
def test_TC1():
    browser = BrowserSetup()
    driver = browser.way1(URL)
    help_panel = HelpPanel(driver)
    assert help_panel.is_help_button_present()
    driver.quit()

def test_TC2():
    logging.info("Starting test_TC2")
    browser = BrowserSetup()
    driver = browser.way1("http://localhost:2004")
    if driver is None:
        logging.error("Browser initialization failed in way2(). Skipping test.")
        # pytest.fail("Browser initialization failed in way2()")

    help_panel = HelpPanel(driver)
    help_panel.click_help_button()
    driver.quit()

def test_TC3():
    logging.info("Starting test_TC3")
    browser = BrowserSetup()
    driver = browser.way1("http://localhost:2004")
    time.sleep(5)  # Allow time for the page to load

    help_panel = HelpPanel(driver)

    # Call the method to verify the support desk page
    help_panel.verify_GRL_supportDesk()

    driver.quit()

def test_TC4():
    logging.info("Starting test_TC4")
    browser = BrowserSetup()
    driver = browser.way1("http://localhost:2004")
    time.sleep(5)  # Allow time for the page to load
    help_panel = HelpPanel(driver)
    # Call the method to verify the support desk page
    help_panel.is_email_support_button_clickable()
    driver.quit()

def test_TC5():
    logging.info("Starting test_TC5")
    browser = BrowserSetup()
    driver = browser.way1("http://localhost:2004")
    time.sleep(5)  # Allow time for the page to load
    help_panel = HelpPanel(driver)
    # Call the method to verify the support desk page
    help_panel.download_and_verify_debug_logs()
    driver.quit()