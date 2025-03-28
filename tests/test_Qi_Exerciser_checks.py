# import pytest
# import logging
# from pages.Qi_Exerciser import Qi_Exerciser

# logger = logging.getLogger(__name__)

# # Optional JSON for expected coil types
# EXPECTED_COIL_TYPES = ["TPT_MPP1", "TPT_SPP1", "TPT_SPP2"]

# @pytest.fixture
# def qi_exerciser_page(ba_connection):
#     """
#     Fixture to navigate to Qi Exerciser page after the BA connection is established.
#     Uses Xpaths.json for locators.
#     """
#     # If Xpaths.json is not in the project root, specify the path:
#     page = Qi_Exerciser(ba_connection, xpaths_json_path="Xpaths.json")
#     page.navigate_to_qi_exerciser()
#     return page

# def test_tc1_qi_exerciser_tab(qi_exerciser_page):
#     """TC1: Check Qi-Exerciser is available (tab presence)."""
#     assert qi_exerciser_page.is_qi_exerciser_tab_present(), "Qi Exerciser tab not present"

# def test_tc2_qi_spec_dropdown_values(qi_exerciser_page):
#     """TC2: Check QI Specification text & coil type dropdown values."""
#     assert qi_exerciser_page.is_qi_specification_text_present(), "QI Specification text not found"

#     coil_types = qi_exerciser_page.get_coil_type_options()
#     logger.info(f"Available coil types: {coil_types}")
#     for ect in EXPECTED_COIL_TYPES:
#         assert ect in coil_types, f"Expected coil type '{ect}' not found in dropdown"

# def test_tc3_coil_configuration(qi_exerciser_page):
#     """Verify coil configuration can be set."""
#     qi_exerciser_page.select_coil_type("TPT_MPP1")
#     qi_exerciser_page.click_set_coil()
#     logger.info("Coil configuration set to TPT_MPP1.")

# def test_tc4_inverter_configuration(qi_exerciser_page):
#     """Check that user can set Inverter Configuration (PPS Volt, Phase Shift)."""
#     qi_exerciser_page.set_inverter_configuration(pps_volt=5, phase_shift=90)
#     logger.info("Inverter configuration set: PPS Volt=5, Phase Shift=90.")

# def test_tc5_cloak_checkbox(qi_exerciser_page):
#     """Verify cloak checkbox can be toggled."""
#     assert qi_exerciser_page.is_cloak_checkbox_enabled(), "Cloak checkbox not enabled"
#     qi_exerciser_page.toggle_cloak_checkbox(enable=True)
#     qi_exerciser_page.toggle_cloak_checkbox(enable=False)

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
import pytest
from utilities.browser_setup import BrowserSetup
from pages.Qi_Exerciser import QiExerciserPanel


URL = "http://localhost:2004"

@pytest.fixture(scope="module")
def setup_teardown_qi_exerciser():
    logging.info("Setting up the browser for Qi Exerciser Panel")
    browser = BrowserSetup()
    driver = browser.way1(URL)
    QiExerciser = QiExerciserPanel(driver)
    QiExerciser.open_qi_exerciser()
    time.sleep(5)
    yield driver, QiExerciser
    logging.info("Tearing down the browser")
    driver.quit()

# Inputbox test cases for Qi Exerciser Panel
def test_TC30_A0_inputbox_checking(setup_teardown_qi_exerciser):
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.input_field_test(QiExerciser.a0_inputbox, "A0")

def test_TC31_A1_inputbox_checking(setup_teardown_qi_exerciser):
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.input_field_test(QiExerciser.a1_inputbox, "A1")

def test_TC32_d_Tx_inputbox_checking(setup_teardown_qi_exerciser):
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.input_field_test(QiExerciser.d_tx_inputbox, "Δd_Tx")

# Checkbox test cases for Qi Exerciser Panel
def test_TC33_PPS_volts_checkbox_checking(setup_teardown_qi_exerciser):
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.checkbox_test(QiExerciser.pps_volts_checkbox, "PPS Volts Checkbox")

def test_TC34_Q_factor_Measurement_checkbox_checking(setup_teardown_qi_exerciser):
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.checkbox_test(QiExerciser.q_factor_measurement_checkbox, "Q Factor Measurement Checkbox")

# Dropdown test cases for Qi Exerciser Panel
def test_TC35_Coil_Type_dropdown_checking(setup_teardown_qi_exerciser):
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.dropdown_test(QiExerciser.coil_type, "Coil Type")

def test_TC36_Demodulator_dropdown_checking(setup_teardown_qi_exerciser):
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.dropdown_test(QiExerciser.demodulator, "Demodulator")