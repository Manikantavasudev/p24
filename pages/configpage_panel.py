
import logging
import random
import string
import json
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def load_xpaths(json_file="Xpaths.json"):
    try:
        with open(json_file, "r") as file:
            data = json.load(file)
        if "Testconfig_page" not in data:
            logging.error("Missing 'Testconfig_page' key in XPaths JSON file")
            raise KeyError("Testconfig_page key not found in JSON file")
        return data
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading XPaths JSON: {e}")
        raise

xpaths = load_xpaths()

class TestConfigPage:
    def __init__(self, driver):
        self.driver = driver
        self.elements = xpaths.get("Testconfig_page", {})
        
        self.test_config_btn = self.elements.get("Testconfig_page")
        self.edit_sdf_btn = self.elements.get("EDIT_SDF_BTN")

         # Input fields
        self.ProductName = self.elements.get("ProductName")
        self.Applicatname = self.elements.get("ApplicantName")
        self.PartNumber = self.elements.get("PartNumber")
        self.QIID = self.elements.get("QIID")
        self.MFcode = self.elements.get("Manufacturer_Code")
        self.clock = self.elements.get("CloakRetryCount")
        self.maimumpower = self.elements.get("Maximum_Power")


        # Checkboxes
        self.OBsupport = self.elements.get("OB_Support")
        self.Negotiationsupport = self.elements.get("Negotiation_Support")
        self.XIDDataPacketSupport = self.elements.get("XIDDataPacket_Support")
        self.RestrictedModeSupport = self.elements.get("RestrictedMode_Support")
        self.CloakSupport = self.elements.get("Cloak_Support")
        self.GainLinearizationSupport = self.elements.get("Gain Linearization Support")
        self.DupSupport = self.elements.get("Dup_Support")
        self.WPIDSupport = self.elements.get("WPID_Support")
        self.PCHDataPacketSupport = self.elements.get("PCHDataPacket_Support")
        self.RestrictedToFullMode = self.elements.get("RestrictedToFullMode")
        self.DetectPingSupport = self.elements.get("Detect_Ping_Support")
        self.HPMPingSupport = self.elements.get("HPM_PingSupport")
        self.Authsupport = self.elements.get("Auth_support_chkbox")

        #DROPDOWN ELEMENTS
        self.supported_specification = self.elements.get("Supported_Specification")
        self.power_profile = self.elements.get("powerprofile")
        self.supported_prop_data_packets = self.elements.get("SupportedPROPData_Packets")
        self.supported_protocols = self.elements.get("Supported_Protocols")
        self.supported_cloak_reasons = self.elements.get("Supported_Cloak_Reasons")
        self.supported_get_requests = self.elements.get("Supported GetRequests")
        

        
    
    def open_test_config(self):
        logging.info("Opening Test Configuration Panel")
        self.driver.find_element(By.XPATH, self.test_config_btn).click()
        time.sleep(2)
        logging.info("clicking on body of the UI to enble the UI")
        self.driver.find_element(By.TAG_NAME, "body").click()
    
    def click_edit_sdf(self):
        logging.info("Clicking on Edit SDF Button")
        self.driver.find_element(By.XPATH, self.edit_sdf_btn).click()

    def input_field_test(self, element_xpath, field_name):
        logging.info(f"Verifying the input box functionality for {field_name}")
        
        # Check if the input box is present
        try:
            input_field = self.driver.find_element(By.XPATH, element_xpath)
        except NoSuchElementException:
            logging.error(f"{field_name} input box is not available on the page")
            return  # Stop further execution for this test case
        
        # Test with 100 random characters (numbers, letters, and special characters)
        test_value = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=100))
        input_field.clear()
        input_field.send_keys(test_value)
        
        # Verify if the input box accepts the value
        if input_field.get_attribute("value") == test_value:
            logging.info(f"{field_name} input box accepted 100 random characters: {test_value}")
        else:
            logging.error(f"{field_name} input box failed to accept 100 random characters")
        
        # Test with 100 numbers
        test_value = ''.join(random.choices(string.digits, k=100))
        input_field.clear()
        input_field.send_keys(test_value)
        
        if input_field.get_attribute("value") == test_value:
            logging.info(f"{field_name} input box accepted 100 numbers: {test_value}")
        else:
            logging.error(f"{field_name} input box failed to accept 100 numbers")
        
        # Test with 100 letters
        test_value = ''.join(random.choices(string.ascii_letters, k=100))
        input_field.clear()
        input_field.send_keys(test_value)
        
        if input_field.get_attribute("value") == test_value:
            logging.info(f"{field_name} input box accepted 100 letters: {test_value}")
        else:
            logging.error(f"{field_name} input box failed to accept 100 letters")
        
        # Test with a combination of letters, numbers, and special characters
        test_value = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=100))
        input_field.clear()
        input_field.send_keys(test_value)
        
        if input_field.get_attribute("value") == test_value:
            logging.info(f"{field_name} input box accepted a combination of letters, numbers, and special characters: {test_value}")
        else:
            logging.error(f"{field_name} input box failed to accept a combination of letters, numbers, and special characters")

    def checkbox_test(self, checkbox_xpath, checkbox_name):
        logging.info(f"Verifying the checkbox functionality for {checkbox_name}")
        
        # Check if the checkbox is present
        try:
            checkbox = self.driver.find_element(By.XPATH, checkbox_xpath)
        except NoSuchElementException:
            logging.error(f"{checkbox_name} checkbox is not available on the page")
            return  # Stop further execution for this test case
        
        # Ensure the checkbox is unchecked by default
        if not checkbox.is_selected():
            logging.info(f"{checkbox_name} checkbox is unchecked by default")
        else:
            logging.error(f"{checkbox_name} checkbox is checked by default")
            checkbox.click()  # Uncheck it if it's checked by default
        
        # Check the checkbox
        checkbox.click()
        if checkbox.is_selected():
            logging.info(f"{checkbox_name} checkbox is now checked")
        else:
            logging.error(f"{checkbox_name} checkbox could not be checked")
        
        # Uncheck the checkbox
        checkbox.click()
        if not checkbox.is_selected():
            logging.info(f"{checkbox_name} checkbox is now unchecked")
        else:
            logging.error(f"{checkbox_name} checkbox could not be unchecked")
    
    # def dropdown_test(self, dropdown_xpath, dropdown_name):
    #     """Verify the dropdown functionality."""
    #     logging.info(f"Verifying the dropdown functionality for {dropdown_name}")        
    #     # Check if the dropdown is present
    #     try:
    #         dropdown_element = self.driver.find_element(By.XPATH, dropdown_xpath)
    #     except NoSuchElementException:
    #         logging.error(f"{dropdown_name} dropdown is not available on the page")
    #         return False
        
    #     # Verify if the dropdown can be selected
    #     try:
    #         dropdown = Select(dropdown_element)
    #     except Exception as e:
    #         logging.error(f"{dropdown_name} dropdown cannot be selected: {e}")
    #         return False
        
    #     # Check if the dropdown is enabled
    #     if not dropdown_element.is_enabled():
    #         logging.error(f"{dropdown_name} dropdown is not enabled")
    #         return False
        
    #     # Get all options in the dropdown
    #     options = dropdown.options
    #     if not options:
    #         logging.error(f"{dropdown_name} dropdown has no options")
    #         return False
        
    #     # Print all available options
    #     logging.info(f"Available options in {dropdown_name}:")
    #     for option in options:
    #         logging.info(f"- {option.text}")
        
    #     # Select each option and verify selection
    #     for option in options:
    #         option_text = option.text
    #         dropdown.select_by_visible_text(option_text)
    #         selected_option = dropdown.first_selected_option.text
            
    #         assert selected_option == option_text, \
    #             f"Failed to select '{option_text}' in {dropdown_name}"
        
    #     # Verify dropdown disappears when clicking outside
    #     dropdown_element.click()  # Open the dropdown
    #     self.driver.find_element(By.XPATH, "//body").click()  # Click outside the dropdown
    #     assert not dropdown_element.is_displayed(), \
    #         f"{dropdown_name} dropdown did not disappear after clicking outside"
        
    #     return True

    def dropdown_test(self, dropdown_xpath, dropdown_name):
        """Verify the dropdown functionality for non-<select> dropdowns."""
        logging.info(f"Verifying the dropdown functionality for {dropdown_name}")

        # Check if the dropdown is present
        try:
            dropdown_element = self.driver.find_element(By.XPATH, dropdown_xpath)
        except NoSuchElementException:
            logging.error(f"{dropdown_name} dropdown is not available on the page")
            return False

        # Verify if the dropdown is enabled
        if not dropdown_element.is_enabled():
            logging.error(f"{dropdown_name} dropdown is not enabled")
            return False

        # Open the dropdown
        dropdown_element.click()

        # Locate all options (adjust the XPath as needed)
        options_xpath = f"{dropdown_xpath}//div[@role='option']"
        try:
            options = self.driver.find_elements(By.XPATH, options_xpath)
        except NoSuchElementException:
            logging.error(f"{dropdown_name} dropdown has no options")
            return False

        # Print all available options
        logging.info(f"Available options in {dropdown_name}:")
        for option in options:
            logging.info(f"- {option.text}")

        # Select each option and verify selection
        for option in options:
            option_text = option.text
            option.click()
            selected_option = dropdown_element.text  # Adjust this based on how the selected option is displayed

            assert selected_option == option_text, \
                f"Failed to select '{option_text}' in {dropdown_name}"

        # Verify dropdown disappears when clicking outside
        dropdown_element.click()  # Open the dropdown
        self.driver.find_element(By.XPATH, "//body").click()  # Click outside the dropdown
