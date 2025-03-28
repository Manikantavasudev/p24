import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import logging
import configparser

# import allure

URL = "http://localhost:2004"
IP_ADDRESS = "192.168.5.77"

TESTER_STATUS_XPATH = "(//div[@class='right-spacing-tester'])[1]"
CONNECT_BUTTON_ID = "connectionsetup_connect_button"
IP_INPUT_XPATH = "//input[@class='rc-select-search__field']"
CLEAR_INPUT_XPATH = "//i[@class='rc-select-selection__clear-icon']"
POPUP_XPATH = "//button[@class='popupButtons popupButton_Ok btn btn-success']"
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# def attach_log_to_allure(message):
#     try:
        
#         allure.attach(message, name="Log Message", attachment_type=allure.attachment_type.TEXT)
#     except ImportError:
#         pass

class BrowserSetup:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def way1(self, url):
        """ Initialize browser using Way1 """
        logging.info("Opening browser using way1")
        self.driver.maximize_window()
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10) 
        self.handle_popup(wait)
        return self.driver

    def way2(self, url, ip_address):
        """ Initialize browser using Way2 """
        logging.info("Opening browser using way2")
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(2)
        wait = WebDriverWait(self.driver, 10)
        self.handle_popup(wait)
        # Check tester connection status
        retries = 0
        while retries < 10:
            status_text = wait.until(EC.presence_of_element_located((By.XPATH, TESTER_STATUS_XPATH))).text
            logging.info(f"Tester status: {status_text}")
            self.handle_popup(wait)
            if "Connected" in status_text:
                break
            else:
                clear_input = wait.until(EC.element_to_be_clickable((By.XPATH, CLEAR_INPUT_XPATH)))
                clear_input.click()
                ip_input_element = wait.until(EC.element_to_be_clickable((By.XPATH, IP_INPUT_XPATH)))
                ip_input_element.send_keys(ip_address)

                connect_button_element = wait.until(EC.element_to_be_clickable((By.ID, CONNECT_BUTTON_ID)))
                connect_button_element.click()
                self.handle_popup(wait)
                time.sleep(2)


                retries += 1

        # Handle any popups
    def handle_popup(self, wait):
        """ Handle popups if present """
        try:
            popup = wait.until(EC.presence_of_element_located((By.XPATH, POPUP_XPATH)))
            if popup.is_displayed():
                logging.info("Popup detected. Clicking OK.")
                popup.click()
        except:
            pass
