import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import logging
import os

# Set logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Get IP from environment variable (set by Jenkins parameter)
TEST_IP = os.getenv("TESTER_IP", "192.168.5.74")  # fallback if not passed
logging.info(f"Using TESTER_IP: {TEST_IP}")

# Constants
URL = "http://localhost:2004"
TESTER_STATUS_XPATH = "(//div[@class='right-spacing-tester'])[1]"
CONNECT_BUTTON_ID = "connectionsetup_connect_button"
IP_INPUT_XPATH = "//input[@class='rc-select-search__field']"
CLEAR_INPUT_XPATH = "//i[@class='rc-select-selection__clear-icon']"
POPUP_XPATH = "//button[@class='popupButtons popupButton_Ok btn btn-success']"


# class BrowserSetup:
#     def __init__(self):
#         self.driver = webdriver.Chrome()

    # def way1(self, url):
    #     """Initialize browser and verify tester connection status"""
    #     logging.info("Opening browser using way1")
    #     self.driver.maximize_window()
    #     self.driver.get(url)
    #     wait = WebDriverWait(self.driver, 10)

    #     self.handle_popup(wait)

    #     retries = 0
    #     max_retries = 10
    #     connected = False

    #     while retries < max_retries and not connected:
    #         try:
    #             status_text = wait.until(
    #                 EC.presence_of_element_located((By.XPATH, TESTER_STATUS_XPATH))
    #             ).text
    #             logging.info(f"Tester status: {status_text}")

    #             if "Connected" in status_text:
    #                 connected = True
    #             else:
    #                 # Attempt to connect
    #                 clear_input = wait.until(EC.element_to_be_clickable((By.XPATH, CLEAR_INPUT_XPATH)))
    #                 clear_input.click()

    #                 ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, IP_INPUT_XPATH)))
    #                 ip_input.send_keys(TEST_IP)

    #                 connect_button = wait.until(EC.element_to_be_clickable((By.ID, CONNECT_BUTTON_ID)))
    #                 connect_button.click()

    #                 self.handle_popup(wait)
    #                 time.sleep(2)  # Wait for connection attempt

    #         except Exception as e:
    #             logging.error(f"Connection attempt {retries + 1} failed: {str(e)}")
    #             self.driver.save_screenshot(f"connection_error_{retries}.png")

    #         retries += 1

    #     if not connected:
    #         logging.error("Failed to establish connection after maximum retries")
    #         raise Exception("Could not connect to tester after multiple attempts")

    #     return self.driver  # Return driver only after connection is verified

    # def handle_popup(self, wait):
    #     """Handles popup if it appears"""
    #     try:
    #         popup = wait.until(EC.element_to_be_clickable((By.XPATH, POPUP_XPATH)))
    #         popup.click()
    #         logging.info("Popup handled")
    #     except TimeoutException:
    #         logging.info("No popup appeared")
# class BrowserSetup:
#     def __init__(self):
#         self.driver = webdriver.Chrome()

#     def way1(self, url):
#         """ Initialize browser using Way1 """
#         logging.info("Opening browser using way1")
#         self.driver.maximize_window()
#         self.driver.get(url)
#         wait = WebDriverWait(self.driver, 10) 
#         self.handle_popup(wait)
#         return self.driver
class BrowserSetup:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def way1(self, url):
        """Initialize browser and verify tester connection status"""
        logging.info("Opening browser using way1")
        self.driver.maximize_window()
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)

        self.handle_popup(wait)

        retries = 0
        max_retries = 10
        connected = False

        while retries < max_retries and not connected:
            try:
                status_text = wait.until(
                    EC.presence_of_element_located((By.XPATH, TESTER_STATUS_XPATH))
                ).text
                logging.info(f"Tester status: {status_text}")

                if "Connected" in status_text:
                    connected = True
                else:
                    # Attempt to connect
                    clear_input = wait.until(EC.element_to_be_clickable((By.XPATH, CLEAR_INPUT_XPATH)))
                    clear_input.click()

                    ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, IP_INPUT_XPATH)))
                    ip_input.send_keys(TEST_IP)

                    connect_button = wait.until(EC.element_to_be_clickable((By.ID, CONNECT_BUTTON_ID)))
                    connect_button.click()

                    self.handle_popup(wait)
                    time.sleep(2)  # Wait for connection attempt

            except Exception as e:
                logging.error(f"Connection attempt {retries + 1} failed: {str(e)}")
                self.driver.save_screenshot(f"connection_error_{retries}.png")

            retries += 1

        if not connected:
            logging.error("Failed to establish connection after maximum retries")
            raise Exception("Could not connect to tester after multiple attempts")

        return self.driver  # Return driver only after connection is verified

    def handle_popup(self, wait):
        """Handles popup if it appears"""
        try:
            popup = wait.until(EC.element_to_be_clickable((By.XPATH, POPUP_XPATH)))
            popup.click()
            logging.info("Popup handled")
        except TimeoutException:
            logging.info("No popup appeared")

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
