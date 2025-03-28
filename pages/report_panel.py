# # # import logging
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.support.ui import WebDriverWait
# # # from selenium.webdriver.support import expected_conditions as EC
# # # import time

# # # Report_BUTTON_XPATH = "//div[@id='left-toggle-group']/label[6]"
# # # View_report = "//button[@id='report_toolbar_refresh_button']"
# # # Download_cuurent_HTML ="//button[@id='report_toolbar_download_html_button']"
# # # Download_BSUT_report = "//button[@id='report_toolbar_dwonload_dut_button']"
# # # report_data_management = "//button[text()='Report Data Management']"
# # # Synthetic_File =  "//button[text()='Synthetic File']"


# # # class ReportPanel:
# # #     def __init__(self, driver):
# # #         """
# # #         Initialize the Report Panel class.

# # #         Args:
# # #             driver: Selenium WebDriver instance.
# # #         """
# # #         self.driver = driver
# # #         self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait

# # #     def is_report_page_available(self):
        
# # #         logging.info("Checking if the Browser application is having connection Panel")
# # #         try:
# # #             help_button = self.driver.find_element(By.XPATH, Report_BUTTON_XPATH)
# # #             if help_button.is_displayed():
# # #                 logging.info("Report button is available on the Browser Application")
# # #                 return True
# # #         except:
# # #             logging.error("Report button is not present.")
# # #             self.driver.save_screenshot("Report_buttonnot_present.png")
# # #             return False
# # import logging
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time

# # Report_BUTTON_XPATH = "//div[@id='left-toggle-group']/label[5]"
# # View_report = "//button[@id='report_toolbar_refresh_button']"
# # Download_current_HTML = "//button[@id='report_toolbar_download_html_button']"
# # Download_BSUT_report = "//button[@id='report_toolbar_dwonload_dut_button']"
# # report_data_management = "//button[text()='Report Data Management']"
# # Synthetic_File = "//button[text()='Synthetic File']"

# # class ReportPanel:
# #     def __init__(self, driver):
# #         """
# #         Initialize the Report Panel class.

# #         Args:
# #             driver: Selenium WebDriver instance.
# #         """
# #         self.driver = driver
# #         self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait

# #     def is_report_page_available(self):
# #         """
# #         Check if the Report button is available and click it.
# #         """
# #         logging.info("Checking if the Browser application is having Report Panel")
# #         try:
# #             report_button = self.driver.find_element(By.XPATH, Report_BUTTON_XPATH)
# #             if report_button.is_displayed():
# #                 logging.info("Report button is available on the Browser Application")
# #                 report_button.click()
# #                 time.sleep(2)  # Wait for the report panel to load
# #                 return True
# #         except Exception as e:
# #             logging.error(f"Report button is not present: {e}")
# #             self.driver.save_screenshot("Report_button_not_present.png")
# #             return False

# #     def verify_button_and_tooltip(self, button_name, button_xpath):
# #         """
# #         Verify if a button is available and check its tooltip.

# #         Args:
# #             button_name (str): Name of the button for logging.
# #             button_xpath (str): XPath of the button to locate it.
# #         """
# #         try:
# #             button = self.driver.find_element(By.XPATH, button_xpath)
# #             if button.is_displayed():
# #                 logging.info(f"{button_name} button is available.")
# #                 tooltip = button.get_attribute("title")
# #                 if tooltip:
# #                     logging.info(f"Tooltip for {button_name}: {tooltip}")
# #                 else:
# #                     logging.error(f"No tooltip found for {button_name}.")
# #                 return True
# #             else:
# #                 logging.error(f"{button_name} button is not displayed.")
# #                 return False
# #         except Exception as e:
# #             logging.error(f"Error finding {button_name} button: {e}")
# #             self.driver.save_screenshot(f"{button_name}_not_found.png")
# #             return False

# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# import logging
# import time

# # Button XPaths
# Report_BUTTON_XPATH = "//div[@id='left-toggle-group']/label[6]"
# View_report = "//button[@id='report_toolbar_refresh_button']"
# Download_current_HTML = "//button[@id='report_toolbar_download_html_button']"
# Download_BSUT_report = "//button[@id='report_toolbar_dwonload_dut_button']"
# report_data_management = "//button[text()='Report Data Management']"
# Synthetic_File = "//button[text()='Synthetic File']"

# # Tooltip XPaths (update these based on your application)
# View_report_tooltip = "//div[@class='tooltip' and contains(text(), 'View Report')]"
# Download_current_HTML_tooltip = "//div[@class='tooltip' and contains(text(), 'Download Current HTML')]"
# Download_BSUT_report_tooltip = "//div[@class='tooltip' and contains(text(), 'Download BSUT Report')]"
# report_data_management_tooltip = "//div[@class='tooltip' and contains(text(), 'Report Data Management')]"
# Synthetic_File_tooltip = "//div[@class='tooltip' and contains(text(), 'Synthetic File')]"

# class ReportPanel:
#     def __init__(self, driver):
#         """
#         Initialize the Report Panel class.

#         Args:
#             driver: Selenium WebDriver instance.
#         """
#         self.driver = driver

#     def is_report_page_available(self):
#         """
#         Check if the Report button is available and click it.
#         """
#         logging.info("Checking if the Browser application is having Report Panel")
#         try:
#             report_button = self.driver.find_element(By.XPATH, Report_BUTTON_XPATH)
#             if report_button.is_displayed():
#                 logging.info("Report button is available on the Browser Application")
#                 report_button.click()
#                 time.sleep(2)  # Wait for the report panel to load
#                 return True
#         except Exception as e:
#             logging.error(f"Report button is not present: {e}")
#             self.driver.save_screenshot("Report_button_not_present.png")
#             return False

#     def verify_button_and_tooltip(self, button_name, button_xpath, tooltip_xpath):
#         """
#         Verify if a button is available and check its tooltip.

#         Args:
#             button_name (str): Name of the button for logging.
#             button_xpath (str): XPath of the button to locate it.
#             tooltip_xpath (str): XPath of the tooltip element to locate it.
#         """
#         try:
#             button = self.driver.find_element(By.XPATH, button_xpath)
#             if button.is_displayed():
#                 logging.info(f"{button_name} button is available.")

#                 # Hover over the button to trigger the tooltip
#                 ActionChains(self.driver).move_to_element(button).perform()
#                 time.sleep(1)  # Wait for the tooltip to appear

#                 # Locate the tooltip element
#                 try:
#                     tooltip_element = self.driver.find_element(By.XPATH, tooltip_xpath)
#                     tooltip_text = tooltip_element.text
#                     if tooltip_text:
#                         logging.info(f"Tooltip for {button_name}: {tooltip_text}")
#                         return True
#                     else:
#                         logging.error(f"Tooltip for {button_name} is empty.")
#                         self.driver.save_screenshot(f"{button_name}_empty_tooltip.png")
#                         return False
#                 except Exception as e:
#                     logging.error(f"Tooltip element for {button_name} not found: {e}")
#                     self.driver.save_screenshot(f"{button_name}_tooltip_not_found.png")
#                     return False
#             else:
#                 logging.error(f"{button_name} button is not displayed.")
#                 return False
#         except Exception as e:
#             logging.error(f"Error finding {button_name} button: {e}")
#             self.driver.save_screenshot(f"{button_name}_not_found.png")
#             return False
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