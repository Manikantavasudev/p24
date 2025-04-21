# import os
# import time
# import logging
# import pytest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# # Logging Configuration
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# # Environment Configurations
# TEST_IP = os.getenv("TESTER_IP", "192.168.5.74")  # Default IP if not passed
# BROWSER_NAME = os.getenv("BROWSER", "chrome").lower()  # Default browser if not passed

# # UI Constants
# URL = "http://localhost:2004"
# TESTER_STATUS_XPATH = "(//div[@class='right-spacing-tester'])[1]"
# CONNECT_BUTTON_ID = "connectionsetup_connect_button"
# IP_INPUT_XPATH = "//input[@class='rc-select-search__field']"
# CLEAR_INPUT_XPATH = "//i[@class='rc-select-selection__clear-icon']"
# POPUP_XPATH = "//button[@class='popupButtons popupButton_Ok btn btn-success']"


# class BrowserSetup:
#     def __init__(self):
#         self.driver = self._init_browser()

#     def _init_browser(self):
#         """Initialize browser based on env/browser name"""
#         logging.info(f"Initializing browser: {BROWSER_NAME}")
#         if BROWSER_NAME == "chrome":
#             return webdriver.Chrome()
#         elif BROWSER_NAME == "firefox":
#             return webdriver.Firefox()
#         elif BROWSER_NAME == "edge":
#             return webdriver.Edge()
#         else:
#             raise ValueError(f"Unsupported browser: {BROWSER_NAME}")

#     def way1(self, url):
#         """Open tester page and establish connection"""
#         logging.info("Opening browser using way1")
#         self.driver.maximize_window()
#         self.driver.get(url)
#         wait = WebDriverWait(self.driver, 10)
#         self.handle_popup(wait)

#         retries = 0
#         connected = False

#         while retries < 10 and not connected:
#             try:
#                 status_text = wait.until(
#                     EC.presence_of_element_located((By.XPATH, TESTER_STATUS_XPATH))
#                 ).text
#                 logging.info(f"Tester status: {status_text}")

#                 if "Connected" in status_text:
#                     connected = True
#                 else:
#                     self._connect_tester(wait)

#             except Exception as e:
#                 logging.error(f"Connection attempt {retries + 1} failed: {str(e)}")
#                 self.driver.save_screenshot(f"connection_error_{retries}.png")

#             retries += 1

#         if not connected:
#             logging.error("Failed to connect to tester after max retries")
#             raise Exception("Connection Failure")

#         return self.driver

#     def _connect_tester(self, wait):
#         clear_input = wait.until(EC.element_to_be_clickable((By.XPATH, CLEAR_INPUT_XPATH)))
#         clear_input.click()

#         ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, IP_INPUT_XPATH)))
#         ip_input.send_keys(TEST_IP)

#         connect_button = wait.until(EC.element_to_be_clickable((By.ID, CONNECT_BUTTON_ID)))
#         connect_button.click()

#         self.handle_popup(wait)
#         time.sleep(2)

#     def way2(self, url, ip_address):
#         """Alternative method with IP passed explicitly"""
#         logging.info("Opening browser using way2")
#         self.driver.maximize_window()
#         self.driver.get(url)
#         wait = WebDriverWait(self.driver, 10)
#         self.handle_popup(wait)

#         retries = 0
#         while retries < 10:
#             status_text = wait.until(EC.presence_of_element_located((By.XPATH, TESTER_STATUS_XPATH))).text
#             logging.info(f"Tester status: {status_text}")
#             self.handle_popup(wait)
#             if "Connected" in status_text:
#                 break
#             else:
#                 self._connect_tester_with_custom_ip(wait, ip_address)
#                 retries += 1

#     def _connect_tester_with_custom_ip(self, wait, ip_address):
#         clear_input = wait.until(EC.element_to_be_clickable((By.XPATH, CLEAR_INPUT_XPATH)))
#         clear_input.click()

#         ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, IP_INPUT_XPATH)))
#         ip_input.send_keys(ip_address)

#         connect_button = wait.until(EC.element_to_be_clickable((By.ID, CONNECT_BUTTON_ID)))
#         connect_button.click()

#         self.handle_popup(wait)
#         time.sleep(2)

#     def handle_popup(self, wait):
#         """Handle popups if present"""
#         try:
#             popup = wait.until(EC.presence_of_element_located((By.XPATH, POPUP_XPATH)))
#             if popup.is_displayed():
#                 logging.info("Popup detected. Clicking OK.")
#                 popup.click()
#         except TimeoutException:
#             logging.info("No popup appeared")
#         except Exception as ex:
#             logging.error(f"Unexpected popup error: {ex}")

import os
import time
import logging
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Logging Configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Environment Configurations
TEST_IP = os.getenv("TESTER_IP", "192.168.5.74")  # Default IP if not passed
BROWSER_NAME = os.getenv("BROWSER", "chrome").lower()  # Default browser if not passed
TEST_TYPE = os.getenv("TEST_TYPE", "TPT").upper()  # TPT or TPR

# URL Selection
TPT_URL = "http://localhost:2004"
TPR_URL = "http://localhost:3004"
URL = TPT_URL if TEST_TYPE == "TPT" else TPR_URL

# UI Constants
TESTER_STATUS_XPATH = "(//div[@class='right-spacing-tester'])[1]"
CONNECT_BUTTON_ID = "connectionsetup_connect_button"
IP_INPUT_XPATH = "//input[@class='rc-select-search__field']"
CLEAR_INPUT_XPATH = "//i[@class='rc-select-selection__clear-icon']"
POPUP_XPATH = "//button[@class='popupButtons popupButton_Ok btn btn-success']"


class BrowserSetup:
    def __init__(self):
        self.driver = self._init_browser()

    def _init_browser(self):
        """Initialize browser based on env/browser name"""
        logging.info(f"Initializing browser: {BROWSER_NAME}")
        if BROWSER_NAME == "chrome":
            return webdriver.Chrome()
        elif BROWSER_NAME == "firefox":
            return webdriver.Firefox()
        elif BROWSER_NAME == "edge":
            return webdriver.Edge()
        else:
            raise ValueError(f"Unsupported browser: {BROWSER_NAME}")

    def way1(self, url):
        """Open tester page and establish connection"""
        logging.info(f"Opening browser using way1 with URL: {url}")
        self.driver.maximize_window()
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        self.handle_popup(wait)

        retries = 0
        connected = False

        while retries < 10 and not connected:
            try:
                status_text = wait.until(
                    EC.presence_of_element_located((By.XPATH, TESTER_STATUS_XPATH))
                ).text
                logging.info(f"Tester status: {status_text}")

                if "Connected" in status_text:
                    connected = True
                else:
                    self._connect_tester(wait)

            except Exception as e:
                logging.error(f"Connection attempt {retries + 1} failed: {str(e)}")
                self.driver.save_screenshot(f"connection_error_{retries}.png")

            retries += 1

        if not connected:
            logging.error("Failed to connect to tester after max retries")
            raise Exception("Connection Failure")

        return self.driver

    def _connect_tester(self, wait):
        clear_input = wait.until(EC.element_to_be_clickable((By.XPATH, CLEAR_INPUT_XPATH)))
        clear_input.click()

        ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, IP_INPUT_XPATH)))
        ip_input.send_keys(TEST_IP)

        connect_button = wait.until(EC.element_to_be_clickable((By.ID, CONNECT_BUTTON_ID)))
        connect_button.click()

        self.handle_popup(wait)
        time.sleep(2)

    def way2(self, url, ip_address):
        """Alternative method with IP passed explicitly"""
        logging.info(f"Opening browser using way2 with URL: {url} and IP: {ip_address}")
        self.driver.maximize_window()
        self.driver.get(url)
        wait = WebDriverWait(self.driver, 10)
        self.handle_popup(wait)

        retries = 0
        while retries < 10:
            status_text = wait.until(EC.presence_of_element_located((By.XPATH, TESTER_STATUS_XPATH))).text
            logging.info(f"Tester status: {status_text}")
            self.handle_popup(wait)
            if "Connected" in status_text:
                break
            else:
                self._connect_tester_with_custom_ip(wait, ip_address)
                retries += 1

    def _connect_tester_with_custom_ip(self, wait, ip_address):
        clear_input = wait.until(EC.element_to_be_clickable((By.XPATH, CLEAR_INPUT_XPATH)))
        clear_input.click()

        ip_input = wait.until(EC.element_to_be_clickable((By.XPATH, IP_INPUT_XPATH)))
        ip_input.send_keys(ip_address)

        connect_button = wait.until(EC.element_to_be_clickable((By.ID, CONNECT_BUTTON_ID)))
        connect_button.click()

        self.handle_popup(wait)
        time.sleep(2)

    def handle_popup(self, wait):
        """Handle popups if present"""
        try:
            popup = wait.until(EC.presence_of_element_located((By.XPATH, POPUP_XPATH)))
            if popup.is_displayed():
                logging.info("Popup detected. Clicking OK.")
                popup.click()
        except TimeoutException:
            logging.info("No popup appeared")
        except Exception as ex:
            logging.error(f"Unexpected popup error: {ex}")


# Example usage for local or Jenkins
if __name__ == "__main__":
    setup = BrowserSetup()
    driver = setup.way1(URL)
    # Optionally, use setup.way2(URL, TEST_IP)
