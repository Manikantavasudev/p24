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

# # Inputbox test cases for Qi Exerciser Panel
# def test_TC30_A0_inputbox_checking(setup_teardown_qi_exerciser):
#     driver, QiExerciser = setup_teardown_qi_exerciser
#     QiExerciser.input_field_test(QiExerciser.a0_inputbox, "A0")

# def test_TC31_A1_inputbox_checking(setup_teardown_qi_exerciser):
#     driver, QiExerciser = setup_teardown_qi_exerciser
#     QiExerciser.input_field_test(QiExerciser.a1_inputbox, "A1")

# def test_TC32_d_Tx_inputbox_checking(setup_teardown_qi_exerciser):
#     driver, QiExerciser = setup_teardown_qi_exerciser
#     QiExerciser.input_field_test(QiExerciser.d_tx_inputbox, "Δd_Tx")

# # Checkbox test cases for Qi Exerciser Panel
# def test_TC33_PPS_volts_checkbox_checking(setup_teardown_qi_exerciser):
#     driver, QiExerciser = setup_teardown_qi_exerciser
#     QiExerciser.checkbox_test(QiExerciser.pps_volts_checkbox, "PPS Volts Checkbox")

# def test_TC34_Q_factor_Measurement_checkbox_checking(setup_teardown_qi_exerciser):
#     driver, QiExerciser = setup_teardown_qi_exerciser
#     QiExerciser.checkbox_test(QiExerciser.q_factor_measurement_checkbox, "Q Factor Measurement Checkbox")

# # Dropdown test cases for Qi Exerciser Panel
# def test_TC35_Coil_Type_dropdown_checking(setup_teardown_qi_exerciser):
#     driver, QiExerciser = setup_teardown_qi_exerciser
#     QiExerciser.dropdown_test(QiExerciser.coil_type, "Coil Type")

# def test_TC36_Demodulator_dropdown_checking(setup_teardown_qi_exerciser):
#     driver, QiExerciser = setup_teardown_qi_exerciser
#     QiExerciser.dropdown_test(QiExerciser.demodulator, "Demodulator")



# Inputbox test cases for Qi Exerciser Panel
def test_TC30_A0_inputbox_checking(setup_teardown_qi_exerciser):
    """
    Test Case: TC30_A0 - Verify A0 Input Box functionality in Qi Exerciser
    """
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.input_field_test(QiExerciser.a0_inputbox, "A0")

def test_TC31_A1_inputbox_checking(setup_teardown_qi_exerciser):
    """
    Test Case: TC31_A1 - Verify A1 Input Box functionality in Qi Exerciser
    """
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.input_field_test(QiExerciser.a1_inputbox, "A1")

def test_TC32_d_Tx_inputbox_checking(setup_teardown_qi_exerciser):
    """
    Test Case: TC32_d_Tx - Verify Δd_Tx Input Box functionality in Qi Exerciser
    """
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.input_field_test(QiExerciser.d_tx_inputbox, "Δd_Tx")

# Checkbox test cases for Qi Exerciser Panel
def test_TC33_PPS_volts_checkbox_checking(setup_teardown_qi_exerciser):
    """
    Test Case: TC33_PPS_volts - Verify PPS Volts Checkbox functionality in Qi Exerciser
    """
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.checkbox_test(QiExerciser.pps_volts_checkbox, "PPS Volts Checkbox")

def test_TC34_Q_factor_Measurement_checkbox_checking(setup_teardown_qi_exerciser):
    """
    Test Case: TC34_Q_factor_Measurement - Verify Q Factor Measurement Checkbox functionality in Qi Exerciser
    """
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.checkbox_test(QiExerciser.q_factor_measurement_checkbox, "Q Factor Measurement Checkbox")

# Dropdown test cases for Qi Exerciser Panel
def test_TC35_Coil_Type_dropdown_checking(setup_teardown_qi_exerciser):
    """
    Test Case: TC35_Coil_Type - Verify Coil Type Dropdown functionality in Qi Exerciser
    """
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.dropdown_test(QiExerciser.coil_type, "Coil Type")

def test_TC36_Demodulator_dropdown_checking(setup_teardown_qi_exerciser):
    """
    Test Case: TC36_Demodulator - Verify Demodulator Dropdown functionality in Qi Exerciser
    """
    driver, QiExerciser = setup_teardown_qi_exerciser
    QiExerciser.dropdown_test(QiExerciser.demodulator, "Demodulator")
