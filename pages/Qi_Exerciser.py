# import logging
# import json
# import os
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# # from pages.base_page import BasePage
# import time

# logger = logging.getLogger(__name__)


# driver =webdriver.Chrome()

# driver.get('http://localhost:2004/')
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH, "//i[@class='rc-select-selection__clear-icon']").click()
# print("clear")
# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@class='rc-select-search__field']").send_keys("192.168.5.81")
# print("input")
# time.sleep(5)
# driver.find_element(By.ID, 'connectionsetup_connect_button').click()
# time.sleep(5)
# driver.find_element(By.XPATH, "//div[@id='left-toggle-group']/label[2]").click()

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

class QiExerciserPanel:
    def __init__(self, driver):
        self.driver = driver
        self.elements = xpaths.get("Qi_Exerciser", {})
        
        # Coil Configuration
        self.coil_type = self.elements.get("coil_type")
        self.demodulator = self.elements.get("Demodulator")
        
        # Inverter Configuration
        self.phase_shift = self.elements.get("Phase_shift")
        self.duty_cycle = self.elements.get("Duty_cycle")
        self.dead_delay = self.elements.get("Dead_Delay")
        
        # Dropdowns
        self.capacitance_coupling = self.elements.get("Capacitance_Coupling")
        self.frequency_dropdown = self.elements.get("Frequency_dropdown")
        self.pwm_mode_dropdown = self.elements.get("PWM_Mode_dropdown")
        self.selection_mode_dropdown = self.elements.get("Selection_Mode_dropdown")
        
        # Checkboxes
        self.pps_volts_checkbox = self.elements.get("PPS_volts_checkbox")
        self.q_factor_measurement_checkbox = self.elements.get("Q_factor_Measurement_checkbox")
        self.enable_disable_clock = self.elements.get("enable_disble_clock")
        self.cpm_checkbox = self.elements.get("CPM_checkbox")
        self.npm_checkbox = self.elements.get("NPM_checkbox")
        self.lpm_checkbox = self.elements.get("LPM_checkbox")
        self.hpm_checkbox = self.elements.get("HPM_checkbox")
        self.aux_checkbox = self.elements.get("Aux_checkbox")
        
        # Input fields
        self.a0_inputbox = self.elements.get("A0_inputbox")
        self.a1_inputbox = self.elements.get("A1_inputbox")
        self.d_tx_inputbox = self.elements.get("d_Tx_inputbox")
        self.ffactory_inputbox = self.elements.get("Ffactory_inputbox")
        self.qfactory_inputbox = self.elements.get("Qfactory_inputbox")
        self.offset_10w_less = self.elements.get("ofset_10W_less")
        self.offset_10w_plus = self.elements.get("ofset_10W_plus")
        
        # Buttons
        self.set_inverter = self.elements.get("Set_Inverter")
        self.qi_exerciser_tab = self.elements.get("QI_EXERCISER_TAB")
        self.pfo_offset_btn = self.elements.get("PFO_offset_btn")
        
        # HiRes Measurement Data
        self.vctx = self.elements.get("vctx")
        self.phase = self.elements.get("phase")
        self.magnitude = self.elements.get("magnitude")
        self.realI = self.elements.get("realI")
        self.realQ = self.elements.get("realQ")
        
        # FW Write
        self.fw_write = self.elements.get("FW_Write")
        self.reset_button = self.elements.get("Reest_button")
        self.send_all = self.elements.get("Send_all")
    
    def open_qi_exerciser(self):
        logging.info("Opening Qi Exerciser Panel")
        self.driver.find_element(By.XPATH, self.qi_exerciser_tab).click()
        time.sleep(2)
    
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