from utilities.browser_setup import BrowserSetup
from pages.connection_panel import ConnectionPanel
import logging
import pytest
import time
URL = "http://localhost:2004"
# IP_ADDRESS = "192.168.5.77"
# tpt_folder_path = r"C:\GRL\GRL-C3-MP-TPT\LogFiles\DebugLogger.log"
def test_TC6():
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.is_landing_on_connectionpanel()
    driver.quit()
def test_TC7():
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.verify_browser_title()
    driver.quit()
def test_TC8():
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.verify_Scan_Network_Button()
    driver.quit()

def test_TC9():
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.test_scan_network_and_connect_button_state()
    driver.quit()

def test_TC10():
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.setup_diagram_modal()
    driver.quit()
def test_TC11():
    browser = BrowserSetup()
    driver = browser.way1(URL)
    connection = ConnectionPanel(driver)
    connection.connect_with_wrong_ip()
    driver.quit()