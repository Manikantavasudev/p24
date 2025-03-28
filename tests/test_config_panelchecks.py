# from utilities.browser_setup import BrowserSetup
# from pages.configpage_panel import TestConfigPage
# import logging
# import pytest
# import time

# URL = "http://localhost:2004"

# @pytest.fixture(scope="module")
# def setup_teardown():
#     logging.info("Setting up the browser")
#     browser = BrowserSetup()
#     driver = browser.way1(URL)
#     Config = TestConfigPage(driver)
#     Config.open_test_config()
#     time.sleep(5)
#     Config.click_edit_sdf()
#     yield driver, Config
#     logging.info("Tearing down the browser")
#     driver.quit()

# def test_TC20(setup_teardown):
#     logging.info("Verifying the product name input button functility")
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.ProductName, "Product Name")

# def test_TC21(setup_teardown):
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.Applicatname, "Applicant Name")

# def test_TC22(setup_teardown):
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.PartNumber, "Part Number")

# def test_TC23(setup_teardown):
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.QIID, "QIID")

# def test_TC24(setup_teardown):
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.MFcode, "Manufacturer Code")

# def test_TC25(setup_teardown):
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.clock, "Cloak Retry Count")

# def test_TC(setup_teardown):
#     driver, Config = setup_teardown
#     Config.input_field_test(Config.maimumpower, "Maximum Power")


# #CHECK BOXES

# def test_TC26(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.OBsupport, "OB Support")

# def test_TC27(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.Negotiationsupport, "Negotiation Support")

# def test_TC28(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.XIDDataPacketSupport, "XID Data Packet Support")

# def test_TC29(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.RestrictedModeSupport, "Restricted Mode Support")

# def test_TC30(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.CloakSupport, "Cloak Support")

# def test_TC31(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.GainLinearizationSupport, "Gain Linearization Support")

# def test_TC32(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.DupSupport, "Dup Support")

# def test_TC33(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.WPIDSupport, "WPID Support")

# def test_TC34(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.PCHDataPacketSupport, "PCH Data Packet Support")

# def test_TC35(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.RestrictedToFullMode, "Restricted To Full Mode")

# def test_TC36(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.DetectPingSupport, "Detect Ping Support")

# def test_TC37(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.HPMPingSupport, "HPM Ping Support")

# def test_TC38(setup_teardown):
#     driver, Config = setup_teardown
#     Config.checkbox_test(Config.Authsupport, "Authentication Support")

# # Dropdown test cases
# def test_TC39(setup_teardown):
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_specification, "Supported Specification")

# def test_TC40_Power_Profile_Dropdown(setup_teardown):
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.power_profile, "Power Profile")

# def test_TC41_Supported_PROP_DP_inputbox_checking(setup_teardown):
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_prop_data_packets, "Supported PROP Data Packets")

# def test_TC42_Supported_Protocols__inputbox_checking(setup_teardown):
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_protocols, "Supported Protocols")

# def test_TC43_SupportedCloak_Reasons_inputbox_checking(setup_teardown):
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_cloak_reasons, "Supported Cloak Reasons")

# def test_TC44_Supported_GetRequests_inputbox_checking(setup_teardown):
#     driver, Config = setup_teardown
#     Config.dropdown_test(Config.supported_get_requests, "Supported GetRequests")


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

# Inputbox test cases
def test_TC20_Product_Name_inputbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.input_field_test(Config.ProductName, "Product Name")

def test_TC21_Applicant_Name_inputbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.input_field_test(Config.Applicatname, "Applicant Name")

def test_TC22_Part_Number_inputbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.input_field_test(Config.PartNumber, "Part Number")

def test_TC23_QIID_inputbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.input_field_test(Config.QIID, "QIID")

def test_TC24_Manufacturer_Code_inputbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.input_field_test(Config.MFcode, "Manufacturer Code")

def test_TC25_Cloak_Retry_Count_inputbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.input_field_test(Config.clock, "Cloak Retry Count")

def test_TC26_Maximum_Power_inputbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.input_field_test(Config.maimumpower, "Maximum Power")

# Checkbox test cases
def test_TC27_OB_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.OBsupport, "OB Support")

def test_TC28_Negotiation_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.Negotiationsupport, "Negotiation Support")

def test_TC29_XID_Data_Packet_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.XIDDataPacketSupport, "XID Data Packet Support")

def test_TC30_Restricted_Mode_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.RestrictedModeSupport, "Restricted Mode Support")

def test_TC31_Cloak_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.CloakSupport, "Cloak Support")

def test_TC32_Gain_Linearization_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.GainLinearizationSupport, "Gain Linearization Support")

def test_TC33_Dup_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.DupSupport, "Dup Support")

def test_TC34_WPID_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.WPIDSupport, "WPID Support")

def test_TC35_PCH_Data_Packet_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.PCHDataPacketSupport, "PCH Data Packet Support")

def test_TC36_Restricted_To_Full_Mode_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.RestrictedToFullMode, "Restricted To Full Mode")

def test_TC37_Detect_Ping_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.DetectPingSupport, "Detect Ping Support")

def test_TC38_HPM_Ping_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.HPMPingSupport, "HPM Ping Support")

def test_TC39_Authentication_Support_checkbox_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.checkbox_test(Config.Authsupport, "Authentication Support")

# Dropdown test cases
def test_TC40_Supported_Specification_dropdown_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.dropdown_test(Config.supported_specification, "Supported Specification")

def test_TC41_Power_Profile_dropdown_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.dropdown_test(Config.power_profile, "Power Profile")

def test_TC42_Supported_PROP_DP_dropdown_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.dropdown_test(Config.supported_prop_data_packets, "Supported PROP Data Packets")

def test_TC43_Supported_Protocols_dropdown_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.dropdown_test(Config.supported_protocols, "Supported Protocols")

def test_TC44_Supported_Cloak_Reasons_dropdown_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.dropdown_test(Config.supported_cloak_reasons, "Supported Cloak Reasons")

def test_TC45_Supported_GetRequests_dropdown_checking(setup_teardown):
    driver, Config = setup_teardown
    Config.dropdown_test(Config.supported_get_requests, "Supported GetRequests")
