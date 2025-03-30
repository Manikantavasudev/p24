
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Button XPaths
Report_BUTTON_XPATH = "//label[@class='leftbarButtonGroup btn btn-primary' and @for='navbar-toggle-5']"
View_report = "//button[@id='report_toolbar_refresh_button']"
Download_current_HTML = "//button[@id='report_toolbar_download_html_button']"
Download_BSUT_report = "//button[@id='report_toolbar_dwonload_dut_button']"
report_data_management = "//button[text()='Report Data Management']"
Synthetic_File = "//button[text()='Synthetic File']"

class ReportPanel:
    def __init__(self, driver):
        """
        Initialize the Report Panel class.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait

    def is_report_page_available(self):
        """
        Check if the Report button is available and click it.
        """
        logging.info("Checking if the Browser application is having Report Panel")
        try:
            report_button = self.driver.find_element(By.XPATH, Report_BUTTON_XPATH)
            if report_button.is_displayed():
                logging.info("Report button is available on the Browser Application")
                report_button.click()
                time.sleep(2)  # Wait for the report panel to load
                return True
        except Exception as e:
            logging.error(f"Report button is not present: {e}")
            self.driver.save_screenshot("Report_button_not_present.png")
            return False

    def verify_button_available(self, button_name, button_xpath):
        """
        Verify if a button is available.

        Args:
            button_name (str): Name of the button for logging.
            button_xpath (str): XPath of the button to locate it.
        """
        try:
            button = self.driver.find_element(By.XPATH, button_xpath)
            if button.is_displayed():
                logging.info(f"{button_name} button is available.")
                return True
            else:
                logging.error(f"{button_name} button is not displayed.")
                return False
        except Exception as e:
            logging.error(f"Error finding {button_name} button: {e}")
            self.driver.save_screenshot(f"{button_name}_not_found.png")
            return False