from utilities.browser_setup import BrowserSetup
from pages.helppanel import HelpPanel
import logging
import pytest
import time
URL = "http://localhost:2004"
IP_ADDRESS = "192.168.5.77"
tpt_folder_path = r"C:\GRL\GRL-C3-MP-TPT\LogFiles\DebugLogger.log"
# def test_TC1():
#     browser = BrowserSetup()
#     driver = browser.way1(URL)
#     help_panel = HelpPanel(driver)
#     assert help_panel.is_help_button_present()
#     driver.quit()

# def test_TC2():
#     logging.info("Starting test_TC2")
#     browser = BrowserSetup()
#     driver = browser.way1("http://localhost:2004")
#     if driver is None:
#         logging.error("Browser initialization failed in way2(). Skipping test.")
#         # pytest.fail("Browser initialization failed in way2()")

#     help_panel = HelpPanel(driver)
#     help_panel.click_help_button()
#     driver.quit()

# def test_TC3():
#     logging.info("Starting test_TC3")
#     browser = BrowserSetup()
#     driver = browser.way1("http://localhost:2004")
#     time.sleep(5)  # Allow time for the page to load

#     help_panel = HelpPanel(driver)

#     # Call the method to verify the support desk page
#     help_panel.verify_GRL_supportDesk()

#     driver.quit()

# def test_TC4():
#     logging.info("Starting test_TC4")
#     browser = BrowserSetup()
#     driver = browser.way1("http://localhost:2004")
#     time.sleep(5)  # Allow time for the page to load
#     help_panel = HelpPanel(driver)
#     # Call the method to verify the support desk page
#     help_panel.is_email_support_button_clickable()
#     driver.quit()

# def test_TC5():
#     logging.info("Starting test_TC5")
#     browser = BrowserSetup()
#     driver = browser.way1("http://localhost:2004")
#     time.sleep(5)  # Allow time for the page to load
#     help_panel = HelpPanel(driver)
#     # Call the method to verify the support desk page
#     help_panel.download_and_verify_debug_logs()
#     driver.quit()

def test_TC1():
    """
    Test Case: TC1 - Verify Help Button Presence
    Steps:
        1. Launch the application using the browser setup.
        2. Verify if the 'Help' button is present on the UI.
        3. Assert that the 'Help' button is visible and available for interaction.
        4. Capture screenshot if not found.
        5. Close the browser.
    """
    browser = BrowserSetup()
    driver = browser.way1(URL)
    help_panel = HelpPanel(driver)
    assert help_panel.is_help_button_present()
    driver.quit()


def test_TC2():
    """
    Test Case: TC2 - Click Help Button and Verify App Version
    Steps:
        1. Launch the application using the browser setup.
        2. Click on the 'Help' button.
        3. Verify if the app version displayed matches the expected version ('GRL-C3-TPT').
        4. Log the result and capture screenshot if version mismatches.
        5. Close the browser.
    """
    logging.info("Starting test_TC2")
    browser = BrowserSetup()
    driver = browser.way1("http://localhost:2004")
    if driver is None:
        logging.error("Browser initialization failed in way2(). Skipping test.")

    help_panel = HelpPanel(driver)
    help_panel.click_help_button()
    driver.quit()


def test_TC3():
    """
    Test Case: TC3 - Verify Support Desk Button Functionality
    Steps:
        1. Launch the application using the browser setup.
        2. Click on the 'Help' button.
        3. Click on the 'Support Desk' button.
        4. Verify that a new tab/window opens.
        5. Validate the title of the support desk page.
        6. Close the support window and return to the main window.
        7. Close the browser.
    """
    logging.info("Starting test_TC3")
    browser = BrowserSetup()
    driver = browser.way1("http://localhost:2004")
    time.sleep(5)  # Allow time for the page to load

    help_panel = HelpPanel(driver)
    help_panel.verify_GRL_supportDesk()
    driver.quit()


def test_TC4():
    """
    Test Case: TC4 - Verify Email Support Button Clickability
    Steps:
        1. Launch the application using the browser setup.
        2. Click on the 'Help' button.
        3. Verify if the 'Email Support' button is clickable.
        4. Log the result and capture screenshot if not clickable.
        5. Close the browser.
    """
    logging.info("Starting test_TC4")
    browser = BrowserSetup()
    driver = browser.way1("http://localhost:2004")
    time.sleep(5)  # Allow time for the page to load
    help_panel = HelpPanel(driver)
    help_panel.is_email_support_button_clickable()
    driver.quit()


def test_TC5():
    """
    Test Case: TC5 - Verify Debug Logs Download and Content Validation
    Steps:
        1. Launch the application using the browser setup.
        2. Click on the 'Help' button.
        3. Click on the 'Download Debug Logs' button.
        4. Wait for the download to complete.
        5. Rename the downloaded debug log file with a timestamp.
        6. Compare the downloaded debug log with the reference log file.
        7. Log success if logs match.
        8. Log error if logs do not match.
        9. Close the browser.
    """
    logging.info("Starting test_TC5")
    browser = BrowserSetup()
    driver = browser.way1("http://localhost:2004")
    time.sleep(5)  # Allow time for the page to load
    help_panel = HelpPanel(driver)
    help_panel.download_and_verify_debug_logs()
    driver.quit()
