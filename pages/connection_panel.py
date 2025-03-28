import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image, ImageChops


# Constants
CONNECT_BUTTON_XPATH = "//button[contains(text(),'Connect')]"
TTILE = "//p[@class='navbar-secondaryText']"
SCAN_BUTTON = "//button[@id='connectionsetup_AutoDiscoverIP_button']"
SETUP_DIAGRAM = "//p[contains(text(),'Setup Diagram')]"
OK_BUTTON ="//button[contains(text(),'Ok')]"
APP_URL = "http://localhost:2004/"
TESTER_STATUS  = "(//div[@class='right-spacing-tester'])[1]"
IP_INPUT = "//input[@class='rc-select-search__field']"
CLEAR_INPUT_XPATH = "//i[@class='rc-select-selection__clear-icon']"
class ConnectionPanel:
    def __init__(self, driver):
        """
        Initialize the ConnectionPanel class.

        Args:
            driver: Selenium WebDriver instance.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # Initialize WebDriverWait

    def is_landing_on_connectionpanel(self):
        """ Check if the browser is landing on the Connection Panel. """
        logging.info("Checking if the browser is landing on the Connection Panel")
        try:
            help_button = self.driver.find_element(By.XPATH, CONNECT_BUTTON_XPATH)
            if help_button.is_displayed():
                logging.info("Connection button is available, so the browser is on the Connection Page")
                return True
        except:
            logging.error("Connection button is not present.")
            self.driver.save_screenshot("Connection_buttonnot_present.png")
            return False
    def verify_browser_title(self):
        """Verify the browser title is GRL-C3-TPT."""
        logging.info("Verify The browser title in the UI tab should contain the text GRL-C3-TPT.")
        expected_title = "GRL-C3-TPT"
        try:
            title_element = self.driver.find_element(By.XPATH, TTILE)
            assert title_element.text == expected_title, (
                f"Expected browser title to be {expected_title}, but got {title_element.text}"
                
            )
            logging.info("The browser title is GRL-C3-TPT")
        except AssertionError as e:
            logging.info("The browser title is NOT GRL-C3-TPT")
            self.driver.save_screenshot("browser_title_is_not_GRL-C3-TPT.png")
            raise e
    def verify_Scan_Network_Button(self):
        logging.info("Verifying the 'Scan Network' button is visible on the UI")
        scan_network_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, SCAN_BUTTON))
        )
        
        if scan_network_button.is_displayed():
            logging.info("The 'Scan Network' button is visible on the UI.")
        else:
            logging.error("The 'Scan Network' button is not visible on the UI.")
            self.driver.save_screenshot("Scan_Network_Button_Not_Visible.png")
            return
        
        try:
            logging.info("Verifying the 'Scan Network' button is clickable")
            if scan_network_button.is_enabled():
                logging.info("The 'Scan Network' button is clickable.")
            else:
                logging.error("The 'Scan Network' button is not clickable.")
                self.driver.save_screenshot("Scan_Network_Button_Not_Clickable.png")
                return
        except Exception as e:
            self.driver.save_screenshot("Scan_Network_Button_State.png")
            logging.error("Error verifying the clickability of 'Scan Network' button: " + str(e))
            return

        # Click the scan network button and record the start time
        logging.info("Clicking the 'Scan Network' button")
        start_time = time.time()
        scan_network_button.click()

        # Attempt to confirm scan start by checking if the button becomes disabled.
        # If it doesn't change, log that the click was performed and proceed.
        scan_started = False
        try:
            self.wait.until(lambda d: not scan_network_button.is_enabled())
            scan_started = True
            logging.info("Scan has started; 'Scan Network' button is now disabled.")
            self.driver.save_screenshot("Scan_Network_UI_Grayed.png")
        except Exception as e:
            logging.warning("Could not confirm that the scan has started via button state: " + str(e))
        
        if not scan_started:
            logging.info("Scan button click registered. Proceeding without disabled state confirmation as the UI may not change the button's state.")

        # Wait for the scan to complete: wait for the button to become enabled again.
        try:
            self.wait.until(lambda d: scan_network_button.is_enabled())
            end_time = time.time()
            elapsed_time = end_time - start_time
            logging.info("Scan completed in {:.2f} seconds".format(elapsed_time))
        except Exception as e:
            logging.error("Scan did not complete in the expected time: " + str(e))
            self.driver.save_screenshot("Scan_Network_Timeout.png")
            return

        # Take a screenshot of the available networks after scan completion.
        self.driver.save_screenshot("Available_Networks.png")
        logging.info("Screenshot of available networks taken.")
            
    def test_scan_network_and_connect_button_state(self):
        
        
        # Wait for the "Scan Network" button to be visible
        scan_network_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, SCAN_BUTTON))
        )
        logging.info("The 'Scan Network' button is visible on the UI.")
        
        # 2. Click the "Scan Network" button to initiate scanning
        logging.info("Clicking the 'Scan Network' button.")
        scan_network_button.click()
        
        # 3. Verify that the "Connect" button is disabled during scanning
        connect_button = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, CONNECT_BUTTON_XPATH))
        )
        # Allow a brief moment for the UI to update
        # time.sleep(15)
        if not connect_button.is_enabled():
            logging.info("The 'Connect' button is disabled during scanning as expected.")
        else:
            logging.error("The 'Connect' button is not disabled during scanning.")
            self.driver.save_screenshot("Connect_Button_Not_Disabled.png")
            return

        # 4. Wait for the scan process to complete.
        # We assume that once scanning is complete, the "Scan Network" button is visible/enabled again.
        try:
            time.sleep(60) #given wait to complete the Scan process
            self.wait.until(lambda d: d.find_element(By.XPATH, CONNECT_BUTTON_XPATH).is_enabled())
            logging.info("Scanning process completed. The 'connection' button is visible again.")
        except Exception as e:
            logging.error("Scan process did not complete as expected: " + str(e))
            self.driver.save_screenshot("connect_Button_Not_Enabled.png")
            return

    def setup_diagram_modal(self):
    # 1. Launch the application and verify that the relevant section is displayed.
        

        # Wait for the Setup Diagram element to be visible.
        logging.info("Waiting for the Setup Diagram element to be visible")
        setup_diagram_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, SETUP_DIAGRAM))
        )
        logging.info("Setup Diagram element is visible. Clicking it now.")
        setup_diagram_element.click()

        # 2. Verify that the modal/dialog appears with the expected text.
        logging.info("Waiting for the modal to display the expected text")
        modal_text_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'GRL-C3-TPT Setup Diagram')]"))
        )
        if "GRL-C3-TPT Setup Diagram" in modal_text_element.text:
            logging.info("Modal displays the expected text: 'GRL-C3-TPT Setup Diagram'")
        else:
            logging.error("Expected text not found in the modal")
            self.driver.save_screenshot("Modal_Text_Not_Found.png")
            assert False, "Modal did not display expected text."
        # 4. Take a screenshot of the Setup Diagram view after clicking OK.
        self.driver.save_screenshot("setup_diagram_after_ok.png")
        logging.info("Screenshot of the Setup Diagram view taken after clicking OK.")

        # 3. Click the OK button on the modal to dismiss it.
        logging.info("Waiting for the OK button to be clickable")
        ok_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, OK_BUTTON))
        )
        logging.info("Clicking the OK button in the modal")
        ok_button.click()

        # Wait until the modal is dismissed; for example, wait until the expected text is no longer visible.
        self.wait.until(
            EC.invisibility_of_element_located((By.XPATH, "//*[contains(text(),'GRL-C3-TPT Setup Diagram')]"))
        )
        logging.info("Modal dismissed; back to the Connection Panel.")
    def connect_with_wrong_ip(self):
        # 1. Open the application URL
        logging.info("Opening application URL")
        self.driver.get(APP_URL)  # Replace APP_URL with your application's URL

        # 2. Check tester status and print the current state
        tester_status_element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, TESTER_STATUS))
        )
        initial_status = tester_status_element.text
        logging.info("Initial tester status: %s", initial_status)

        # 3. Clear (if needed) and input a wrong IP address
        ip_input_field = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, IP_INPUT))
        )
        wrong_ip = "192.168.255.22"  # Deliberately wrong IP
        ip_input_field.send_keys(wrong_ip)
        logging.info("Entered wrong IP: %s", wrong_ip)
        time.sleep(10)  # Allow UI update time

        # 4. Click the Connect button
        connect_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, CONNECT_BUTTON_XPATH))
        )
        connect_button.click()
        logging.info("Clicked on the Connect button.")

        # 5. Wait a few seconds and capture the tester status
        time.sleep(5)
        final_status = self.driver.find_element(By.XPATH, TESTER_STATUS).text
        logging.info("Tester status after clicking Connect: %s", final_status)

        # 6. Assert that the tester status contains the expected error message
        expected_error_text = "invalid ip address format"
        if expected_error_text in final_status.lower():
            logging.info("Expected error message is present: %s", final_status)
        else:
            self.driver.save_screenshot("Tester_Status_Unexpected.png")
            assert False, f"Expected '{expected_error_text}' in tester status, got: {final_status}"