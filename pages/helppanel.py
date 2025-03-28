from selenium.webdriver.common.by import By
from selenium import webdriver
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import datetime
import shutil 
from datetime import datetime
import glob
import os
import shutil
import time
import glob
from datetime import datetime  # Correct import statement
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

HELP_TAB = "//span[contains(text(),'Help')]"
app_version = "//p[@class='navbar-secondaryText']"
SUPPORT_BUTTON = "//a[@id='Ref1']"
EMAIL_SUPPORT_BUTTON = "//a[@id='Ref2']"
tpt_folder_path = r"C:\GRL\GRL-C3-MP-TPT\LogFiles\DebugLogger.log"
DEBUG_LOGS_BUTTON = "//a[@id='Ref3']"


class HelpPanel:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_help_button_present(self):
        """ Check if help button is available """
        logging.info("Checking if Help button is present")
        try:
            help_button = self.wait.until(EC.presence_of_element_located((By.XPATH, HELP_TAB)))
            if help_button.is_displayed():
                logging.info("Help button is present")
                return True
        except:
            help_button.click()
            logging.error("Help button is not present. Capturing screenshot.")
            self.driver.save_screenshot("help_button_not_present.png")
            return False
    def click_help_button(self):
        """Click on the help button and verify app version"""
        logging.info("Clicking on Help button")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, HELP_TAB))).click()
        # help_button.click()

        app_version_element = self.wait.until(
            EC.presence_of_element_located((By.XPATH, app_version))
        )
        actual_app_version = app_version_element.text.strip()
        expected_app_version = "GRL-C3-TPT"

        if actual_app_version == expected_app_version:
            logging.info("APP version matches expected version.")
        else:
            logging.error(f"APP version mismatch! Expected: {expected_app_version}, Found: {actual_app_version}")
            self.driver.save_screenshot("app_version_mismatch.png")
        
    def verify_GRL_supportDesk(self):
        """Confirm the presence of the support desk and ensure it loads the ticket page."""
        logging.info("Clicking on Help button")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, HELP_TAB))).click()
        time.sleep(5)
        support_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, SUPPORT_BUTTON)))
        support_button.click()

        # Wait for the new window to appear
        main_window = self.driver.current_window_handle   

        # Wait for a new window to open
        time.sleep(3)  # Optional, but sometimes new windows take a moment to load
        all_windows = self.driver.window_handles

        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                logging.info(f"Switched to new window: {self.driver.title}")
                break

        # Capture the new window title
        title = self.driver.title
        logging.info(f"New page title: {title}")

        # Close the new window and switch back
        self.driver.close()
        self.driver.switch_to.window(main_window)

    def is_email_support_button_clickable(self) -> bool:
        """Check if the Email Support button is clickable."""
        logging.info("Checking if Email Support button is clickable")
        try:
            help_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, HELP_TAB)))
            help_tab.click()
            logging.info("Help tab clicked successfully.")

            email_support = self.wait.until(EC.element_to_be_clickable((By.XPATH, EMAIL_SUPPORT_BUTTON)))
            logging.info("Email Support button located.")
            return email_support.is_displayed()
        except Exception as e:
            logging.error(f"Email Support button not clickable: {str(e)}", exc_info=True)
            return False
    def download_and_verify_debug_logs(self):
        """Downloads debug logs, renames them with datetime format, and compares with TPT debug log."""
        logging.info("Checking Downloads debug logs button working properly in Help Panel or not")
        try:
            help_tab = self.wait.until(EC.element_to_be_clickable((By.XPATH, HELP_TAB)))
            help_tab.click()
            logging.info("Help tab clicked successfully.")
            debug_logs = self.wait.until(EC.element_to_be_clickable((By.XPATH, DEBUG_LOGS_BUTTON)))
            debug_logs.click()
            time.sleep(2)  # Wait for the download to initiate
            logging.info("Debug Logs button clicked successfully.")
        except Exception as e:
            logging.error(f"Debug Logs button not clickable: {str(e)}")
            return False

        # Assuming the file is downloaded to the default download directory
        download_dir = os.path.expanduser("~") + "/Downloads"  # Adjust this path as needed

        # Wait for the file to be downloaded
        downloaded_file = None
        start_time = time.time()
        while time.time() - start_time < 10:  # Wait up to 10 seconds
            # Get the most recently modified file in the download directory
            files = glob.glob(os.path.join(download_dir, "*"))
            if files:
                # Sort files by modification time (most recent first)
                files.sort(key=os.path.getmtime, reverse=True)
                downloaded_file = files[0]  # Most recent file
                logging.info(f"Most recent file in download directory: {downloaded_file}")
                break
            time.sleep(1)

        if not downloaded_file:
            logging.error("No files found in the download directory.")
            return False

        # Rename the file with current date and time
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        new_file_name = f"Debug_Log_{current_time}.txt"
        new_file_path = os.path.join(download_dir, new_file_name)
        os.rename(downloaded_file, new_file_path)
        logging.info(f"Debug logs file renamed to {new_file_name}.")

        # Compare the downloaded file with the reference log file
        reference_log_path = r"C:\GRL\GRL-C3-MP-TPT\LogFiles\DebugLogger.log"
        try:
            with open(new_file_path, 'r') as downloaded_file:
                downloaded_content = downloaded_file.read()
            with open(reference_log_path, 'r') as reference_file:
                reference_content = reference_file.read()

            if downloaded_content == reference_content:
                logging.info("Debug logs match the reference log file.")
                return True
            else:
                logging.error("Debug logs do not match the reference log file.")
                return False
        except Exception as e:
            logging.error(f"Error comparing log files: {str(e)}")
            return False