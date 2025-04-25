from selenium import webdriver
from utilities.browser_setup import BrowserSetup
from pages.configpage_panel import TestConfigPage
import logging
import pytest
import time

URL = "http://localhost:2004"

@pytest.fixture(scope="module")
def setup_teardown():
    logging.info("Setting up the browser")
    browser = BrowserSetup()
    driver = browser.way1(URL)
    Config = TestConfigPage(driver)
    Config.open_test_config()
    time.sleep(5)
    Config.click_edit_sdf()
    yield driver, Config
    logging.info("Tearing down the browser")
    driver.quit()

# def test_TC20_Product_Name_inputbox_checking(setup_teardown):
#     """
#     Test Case: Validate Product Name Input Box with Multiple Inputs
#     Steps:
#         1. Locate the Product Name input box.
#         2. Check if the input box is available on the page.
#         3. Input 100 random characters (letters, numbers, special characters) and verify if accepted.
#         4. Input 100 digits and verify if accepted.
#         5. Input 100 letters and verify if accepted.
#         6. Input a combination of 100 random letters, numbers, and special characters and verify if accepted.
#         7. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.ProductName, "Product Name")

# def test_TC21_Applicant_Name_inputbox_checking(setup_teardown):
#     """
#     Test Case: Validate Applicant Name Input Box with Multiple Inputs
#     Steps:
#         1. Locate the Applicant Name input box.
#         2. Check if the input box is available on the page.
#         3. Input 100 random characters (letters, numbers, special characters) and verify if accepted.
#         4. Input 100 digits and verify if accepted.
#         5. Input 100 letters and verify if accepted.
#         6. Input a combination of 100 random letters, numbers, and special characters and verify if accepted.
#         7. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.Applicatname, "Applicant Name")

# def test_TC22_Part_Number_inputbox_checking(setup_teardown):
#     """
#     Test Case: Validate Part Number Input Box with Multiple Inputs
#     Steps:
#         1. Locate the Part Number input box.
#         2. Check if the input box is available on the page.
#         3. Input 100 random characters (letters, numbers, special characters) and verify if accepted.
#         4. Input 100 digits and verify if accepted.
#         5. Input 100 letters and verify if accepted.
#         6. Input a combination of 100 random letters, numbers, and special characters and verify if accepted.
#         7. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.PartNumber, "Part Number")

# def test_TC23_QIID_inputbox_checking(setup_teardown):
#     """
#     Test Case: Validate QIID Input Box with Multiple Inputs
#     Steps:
#         1. Locate the QIID input box.
#         2. Check if the input box is available on the page.
#         3. Input 100 random characters (letters, numbers, special characters) and verify if accepted.
#         4. Input 100 digits and verify if accepted.
#         5. Input 100 letters and verify if accepted.
#         6. Input a combination of 100 random letters, numbers, and special characters and verify if accepted.
#         7. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.QIID, "QIID")

# def test_TC24_Manufacturer_Code_inputbox_checking(setup_teardown):
#     """
#     Test Case: Validate Manufacturer Code Input Box with Multiple Inputs
#     Steps:
#         1. Locate the Manufacturer Code input box.
#         2. Check if the input box is available on the page.
#         3. Input 100 random characters (letters, numbers, special characters) and verify if accepted.
#         4. Input 100 digits and verify if accepted.
#         5. Input 100 letters and verify if accepted.
#         6. Input a combination of 100 random letters, numbers, and special characters and verify if accepted.
#         7. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.MFcode, "Manufacturer Code")

# def test_TC25_Cloak_Retry_Count_inputbox_checking(setup_teardown):
#     """
#     Test Case: Validate Cloak Retry Count Input Box with Multiple Inputs
#     Steps:
#         1. Locate the Cloak Retry Count input box.
#         2. Check if the input box is available on the page.
#         3. Input 100 random characters (letters, numbers, special characters) and verify if accepted.
#         4. Input 100 digits and verify if accepted.
#         5. Input 100 letters and verify if accepted.
#         6. Input a combination of 100 random letters, numbers, and special characters and verify if accepted.
#         7. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.clock, "Cloak Retry Count")

# def test_TC26_Maximum_Power_inputbox_checking(setup_teardown):
#     """
#     Test Case: Validate Maximum Power Input Box with Multiple Inputs
#     Steps:
#         1. Locate the Maximum Power input box.
#         2. Check if the input box is available on the page.
#         3. Input 100 random characters (letters, numbers, special characters) and verify if accepted.
#         4. Input 100 digits and verify if accepted.
#         5. Input 100 letters and verify if accepted.
#         6. Input a combination of 100 random letters, numbers, and special characters and verify if accepted.
#         7. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.maimumpower, "Maximum Power")

# def test_TC27_OB_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate OB Support Checkbox Functionality
#     Steps:
#         1. Locate the OB Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.OBsupport, "OB Support")

# def test_TC28_Negotiation_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate Negotiation Support Checkbox Functionality
#     Steps:
#         1. Locate the Negotiation Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.Negotiationsupport, "Negotiation Support")

# def test_TC29_XID_Data_Packet_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate XID Data Packet Support Checkbox Functionality
#     Steps:
#         1. Locate the XID Data Packet Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.XIDDataPacketSupport, "XID Data Packet Support")

# def test_TC30_Restricted_Mode_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate Restricted Mode Support Checkbox Functionality
#     Steps:
#         1. Locate the Restricted Mode Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.RestrictedModeSupport, "Restricted Mode Support")

# def test_TC31_Cloak_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate Cloak Support Checkbox Functionality
#     Steps:
#         1. Locate the Cloak Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.CloakSupport, "Cloak Support")

# def test_TC32_Gain_Linearization_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate Gain Linearization Support Checkbox Functionality
#     Steps:
#         1. Locate the Gain Linearization Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.GainLinearizationSupport, "Gain Linearization Support")

# def test_TC33_Dup_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate Dup Support Checkbox Functionality
#     Steps:
#         1. Locate the Dup Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.DupSupport, "Dup Support")

# def test_TC34_WPID_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate WPID Support Checkbox Functionality
#     Steps:
#         1. Locate the WPID Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.WPIDSupport, "WPID Support")

# def test_TC35_PCH_Data_Packet_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate PCH Data Packet Support Checkbox Functionality
#     Steps:
#         1. Locate the PCH Data Packet Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.PCHDataPacketSupport, "PCH Data Packet Support")

# def test_TC36_Restricted_To_Full_Mode_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate Restricted To Full Mode Checkbox Functionality
#     Steps:
#         1. Locate the Restricted To Full Mode checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.RestrictedToFullMode, "Restricted To Full Mode")

# def test_TC37_Detect_Ping_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate Detect Ping Support Checkbox Functionality
#     Steps:
#         1. Locate the Detect Ping Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.DetectPingSupport, "Detect Ping Support")

# def test_TC38_HPM_Ping_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate HPM Ping Support Checkbox Functionality
#     Steps:
#         1. Locate the HPM Ping Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.HPMPingSupport, "HPM Ping Support")

# def test_TC39_Authentication_Support_checkbox_checking(setup_teardown):
#     """
#     Test Case: Validate Authentication Support Checkbox Functionality
#     Steps:
#         1. Locate the Authentication Support checkbox on the page.
#         2. Verify if the checkbox is present and available for interaction.
#         3. Check if the checkbox is unchecked by default.
#         4. Click to check the checkbox and verify it is selected.
#         5. Click again to uncheck the checkbox and verify it is unselected.
#         6. Log the result for each action.
#     """
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.Authsupport, "Authentication Support")

# def test_TC40_Supported_Specification_dropdown_checking(setup_teardown):
#     """
#     Test Case: Validate Supported Specification Dropdown Functionality
#     Steps:
#         1. Locate the Supported Specification dropdown.
#         2. Verify if the dropdown is present on the page.
#         3. Verify if the dropdown is enabled.
#         4. Click to open the dropdown.
#         5. Locate and log all available options.
#         6. Select each option one by one and verify if it gets selected properly.
#         7. Verify that the dropdown closes when clicking outside.
#         8. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_specification, "Supported Specification")

# def test_TC40_Supported_Specification_dropdown_checking(setup_teardown):
#     """
#     Test Case: Validate Supported Specification Dropdown Functionality
#     Steps:
#         1. Locate the Supported Specification dropdown.
#         2. Verify if the dropdown is present on the page.
#         3. Verify if the dropdown is enabled.
#         4. Click to open the dropdown.
#         5. Locate and log all available options.
#         6. Select each option one by one and verify if it gets selected properly.
#         7. Verify that the dropdown closes when clicking outside.
#         8. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_specification, "Supported Specification")

# def test_TC41_Power_Profile_dropdown_checking(setup_teardown):
#     """
#     Test Case: Validate Power Profile Dropdown Functionality
#     Steps:
#         1. Locate the Power Profile dropdown.
#         2. Verify if the dropdown is present on the page.
#         3. Verify if the dropdown is enabled.
#         4. Click to open the dropdown.
#         5. Locate and log all available options.
#         6. Select each option one by one and verify if it gets selected properly.
#         7. Verify that the dropdown closes when clicking outside.
#         8. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.power_profile, "Power Profile")

# def test_TC42_Supported_PROP_DP_dropdown_checking(setup_teardown):
#     """
#     Test Case: Validate Supported PROP Data Packets Dropdown Functionality
#     Steps:
#         1. Locate the Supported PROP Data Packets dropdown.
#         2. Verify if the dropdown is present on the page.
#         3. Verify if the dropdown is enabled.
#         4. Click to open the dropdown.
#         5. Locate and log all available options.
#         6. Select each option one by one and verify if it gets selected properly.
#         7. Verify that the dropdown closes when clicking outside.
#         8. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_prop_data_packets, "Supported PROP Data Packets")

# def test_TC43_Supported_Protocols_dropdown_checking(setup_teardown):
#     """
#     Test Case: Validate Supported Protocols Dropdown Functionality
#     Steps:
#         1. Locate the Supported Protocols dropdown.
#         2. Verify if the dropdown is present on the page.
#         3. Verify if the dropdown is enabled.
#         4. Click to open the dropdown.
#         5. Locate and log all available options.
#         6. Select each option one by one and verify if it gets selected properly.
#         7. Verify that the dropdown closes when clicking outside.
#         8. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_protocols, "Supported Protocols")

# def test_TC44_Supported_Cloak_Reasons_dropdown_checking(setup_teardown):
#     """
#     Test Case: Validate Supported Cloak Reasons Dropdown Functionality
#     Steps:
#         1. Locate the Supported Cloak Reasons dropdown.
#         2. Verify if the dropdown is present on the page.
#         3. Verify if the dropdown is enabled.
#         4. Click to open the dropdown.
#         5. Locate and log all available options.
#         6. Select each option one by one and verify if it gets selected properly.
#         7. Verify that the dropdown closes when clicking outside.
#         8. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_cloak_reasons, "Supported Cloak Reasons")

# def test_TC45_Supported_GetRequests_dropdown_checking(setup_teardown):
#     """
#     Test Case: Validate Supported GetRequests Dropdown Functionality
#     Steps:
#         1. Locate the Supported GetRequests dropdown.
#         2. Verify if the dropdown is present on the page.
#         3. Verify if the dropdown is enabled.
#         4. Click to open the dropdown.
#         5. Locate and log all available options.
#         6. Select each option one by one and verify if it gets selected properly.
#         7. Verify that the dropdown closes when clicking outside.
#         8. Log each validation result.
#     """
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_get_requests, "Supported GetRequests")

def test_Product_Name_Input_Box_Verification(setup_teardown):
    """
    Test Case: TC20 - Validate Product Name Input Box with Multiple Inputs
    """
    driver, Config = setup_teardown
    Config.input_field_test(Config.ProductName, "Product Name")

def test_Applicant_Name_Input_Box_Verification(setup_teardown):
    """
    Test Case: TC21 - Validate Applicant Name Input Box with Multiple Inputs
    """
    driver, Config = setup_teardown
    Config.input_field_test(Config.Applicatname, "Applicant Name")

def test_Part_Number_Input_Box_Verification(setup_teardown):
    """
    Test Case: TC22 - Validate Part Number Input Box with Multiple Inputs
    """
    driver, Config = setup_teardown
    Config.input_field_test(Config.PartNumber, "Part Number")

def test_QIID_Input_Box_Verification(setup_teardown):
    """
    Test Case: TC23 - Validate QIID Input Box with Multiple Inputs
    """
    driver, Config = setup_teardown
    Config.input_field_test(Config.QIID, "QIID")

def test_Manufacturer_Code_Input_Box_Verification(setup_teardown):
    """
    Test Case: TC24 - Validate Manufacturer Code Input Box with Multiple Inputs
    """
    driver, Config = setup_teardown
    Config.input_field_test(Config.MFcode, "Manufacturer Code")

def test_Cloak_Retry_Count_Input_Box_Verification(setup_teardown):
    """
    Test Case: TC25 - Validate Cloak Retry Count Input Box with Multiple Inputs
    """
    driver, Config = setup_teardown
    Config.input_field_test(Config.clock, "Cloak Retry Count")

def test_Maximum_Power_Input_Box_Verification(setup_teardown):
    """
    Test Case: TC26 - Validate Maximum Power Input Box with Multiple Inputs
    """
    driver, Config = setup_teardown
    Config.input_field_test(Config.maimumpower, "Maximum Power")

def test_OB_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC27 - Validate OB Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.OBsupport, "OB Support")

def test_Negotiation_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC28 - Validate Negotiation Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.Negotiationsupport, "Negotiation Support")

def test_XID_Data_Packet_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC29 - Validate XID Data Packet Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.XIDDataPacketSupport, "XID Data Packet Support")

def test_Restricted_Mode_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC30 - Validate Restricted Mode Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.RestrictedModeSupport, "Restricted Mode Support")

def test_Cloak_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC31 - Validate Cloak Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.CloakSupport, "Cloak Support")

def test_Gain_Linearization_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC32 - Validate Gain Linearization Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.GainLinearizationSupport, "Gain Linearization Support")

def test_Dup_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC33 - Validate Dup Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.DupSupport, "Dup Support")

def test_WPID_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC34 - Validate WPID Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.WPIDSupport, "WPID Support")

def test_PCH_Data_Packet_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC35 - Validate PCH Data Packet Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.PCHDataPacketSupport, "PCH Data Packet Support")

def test_Restricted_To_Full_Mode_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC36 - Validate Restricted To Full Mode Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.RestrictedToFullMode, "Restricted To Full Mode")

def test_Detect_Ping_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC37 - Validate Detect Ping Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.DetectPingSupport, "Detect Ping Support")

def test_HPM_Ping_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC38 - Validate HPM Ping Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.HPMPingSupport, "HPM Ping Support")

def test_Authentication_Support_Checkbox_Functionality(setup_teardown):
    """
    Test Case: TC39 - Validate Authentication Support Checkbox Functionality
    """
    driver, Config = setup_teardown
    Config.checkbox_test(Config.Authsupport, "Authentication Support")

def test_Supported_Specification_Dropdown_Functionality(setup_teardown):
    """
    Test Case: TC40 - Validate Supported Specification Dropdown Functionality
    """
    driver, Config = setup_teardown
    Config.dropdown_test(Config.supported_specification, "Supported Specification")

def test_Power_Profile_Dropdown_Functionality(setup_teardown):
    """
    Test Case: TC41 - Validate Power Profile Dropdown Functionality
    """
    driver, Config = setup_teardown
    Config.dropdown_test(Config.power_profile, "Power Profile")

def test_Supported_PROP_DP_Dropdown_Functionality(setup_teardown):
    """
    Test Case: TC42 - Validate Supported PROP Data Packets Dropdown Functionality
    """
    driver, Config = setup_teardown
    Config.dropdown_test(Config.supported_prop_data_packets, "Supported PROP Data Packets")

def test_Supported_Protocols_Dropdown_Functionality(setup_teardown):
    """
    Test Case: TC43 - Validate Supported Protocols Dropdown Functionality
    """
    driver, Config = setup_teardown
    Config.dropdown_test(Config.supported_protocols, "Supported Protocols")

# def test_Supported_Cloak_Reasons_Dropdown_Functionality(setup_teardown):
#     """
#     Test Case: TC44 - Validate Supported Cloak Reasons Dropdown Functionality
#     """
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_cloak_reasons, "Supported Cloak Reasons")

def test_Supported_GetRequests_Dropdown_Functionality(setup_teardown):
    """
    Test Case: TC45 - Validate Supported GetRequests Dropdown Functionality
    """
    driver, Config = setup_teardown
    Config.dropdown_test(Config.supported_get_requests, "Supported GetRequests")
