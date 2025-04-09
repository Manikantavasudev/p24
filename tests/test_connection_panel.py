from utilities.browser_setup import BrowserSetup
from pages.connection_panel import ConnectionPanel
import logging
import pytest
import time
URL = "http://localhost:2004"


# def test_TC6():
#     """
#     Test Case: TC6 - Verify Landing on Connection Panel
#     Steps:
#         1. Launch the application using the browser setup.
#         2. Check if the Connection Panel page is loaded successfully.
#         3. Verify the presence of the 'Connect' button.
#         4. Confirm the Connection Panel is correctly displayed.
#         5. Close the browser.
#     """
#     browser = BrowserSetup()
#     driver = browser.way1(URL)
#     connection = ConnectionPanel(driver)
#     connection.is_landing_on_connectionpanel()
#     driver.quit()

# def test_TC7():
#     """
#     Test Case: TC7 - Verify Browser Title
#     Steps:
#         1. Launch the application using the browser setup.
#         2. Retrieve and verify the browser title on the Connection Panel page.
#         3. Confirm that the title matches the expected title 'GRL-C3-TPT'.
#         4. Log the result.
#         5. Close the browser.
#     """
#     browser = BrowserSetup()
#     driver = browser.way1(URL)
#     connection = ConnectionPanel(driver)
#     connection.verify_browser_title()
#     driver.quit()

# def test_TC8():
#     """
#     Test Case: TC8 - Verify Scan Network Button Behavior
#     Steps:
#         1. Launch the application using the browser setup.
#         2. Verify the presence and visibility of the 'Scan Network' button.
#         3. Verify the button is clickable.
#         4. Click the 'Scan Network' button and check if the scan starts.
#         5. Wait for scan completion and validate that the button gets re-enabled.
#         6. Capture screenshots as required.
#         7. Close the browser.
#     """
#     browser = BrowserSetup()
#     driver = browser.way1(URL)
#     connection = ConnectionPanel(driver)
#     connection.verify_Scan_Network_Button()
#     driver.quit()

# def test_TC9():
#     """
#     Test Case: TC9 - Validate Scan Network and Connect Button Interaction
#     Steps:
#         1. Launch the application using the browser setup.
#         2. Click the 'Scan Network' button to start scanning.
#         3. Verify that the 'Connect' button gets disabled during scanning.
#         4. Wait for the scan to complete.
#         5. Confirm that the 'Connect' button is re-enabled after the scan.
#         6. Capture screenshots if the expected behavior fails.
#         7. Close the browser.
#     """
#     browser = BrowserSetup()
#     driver = browser.way1(URL)
#     connection = ConnectionPanel(driver)
#     connection.test_scan_network_and_connect_button_state()
#     driver.quit()

# def test_TC10():
#     """
#     Test Case: TC10 - Verify Setup Diagram Modal
#     Steps:
#         1. Launch the application using the browser setup.
#         2. Click on the 'Setup Diagram' option.
#         3. Verify if the modal appears with the text 'GRL-C3-TPT Setup Diagram'.
#         4. Take a screenshot of the modal.
#         5. Click on the 'OK' button to close the modal.
#         6. Confirm the modal is successfully dismissed.
#         7. Close the browser.
#     """
#     browser = BrowserSetup()
#     driver = browser.way1(URL)
#     connection = ConnectionPanel(driver)
#     connection.setup_diagram_modal()
#     driver.quit()

# def test_TC11():
#     """
#     Test Case: TC11 - Connect with Wrong IP and Validate Error Handling
#     Steps:
#         1. Launch the application using the browser setup.
#         2. Verify the initial tester status.
#         3. Enter an invalid IP address (e.g., 192.168.255.22).
#         4. Click on the 'Connect' button.
#         5. Validate that the tester status displays the error message: 'invalid ip address format'.
#         6. Capture a screenshot if the error message is not displayed.
#         7. Close the browser.
#     """
#     browser = BrowserSetup()
#     driver = browser.way1(URL)
#     connection = ConnectionPanel(driver)
#     connection.connect_with_wrong_ip()
#     driver.quit()


def test_Connection_Panel_verification():
    """
    Test Case: TC6 - Verify Landing on Connection Panel
    """
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.is_landing_on_connectionpanel()
    driver.quit()

def test_Browser_Title_verification():
    """
    Test Case: TC7 - Verify Browser Title
    """
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.verify_browser_title()
    driver.quit()

def test_Scan_Network_Button_Behavior():
    """
    Test Case: TC8 - Verify Scan Network Button Behavior
    """
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.verify_Scan_Network_Button()
    driver.quit()

def test_Scan_Network_and_Connect_Button_Interaction():
    """
    Test Case: TC9 - Validate Scan Network and Connect Button Interaction
    """
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.test_scan_network_and_connect_button_state()
    driver.quit()

def test_Setup_Diagram_Modal_Verification():
    """
    Test Case: TC10 - Verify Setup Diagram Modal
    """
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.setup_diagram_modal()
    driver.quit()

def test_Connect_with_Wrong_IP_Validation():
    """
    Test Case: TC11 - Connect with Wrong IP and Validate Error Handling
    """
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.connect_with_wrong_ip()
    driver.quit()
