# from utilities.browser_setup import BrowserSetup
# from pages.report_panel import ReportPanel
# import logging
# import pytest
# import time
# URL = "http://localhost:2004"
# # IP_ADDRESS = "192.168.5.77"
# # tpt_folder_path = r"C:\GRL\GRL-C3-MP-TPT\LogFiles\DebugLogger.log"
# def test_TC100():
#     browser = BrowserSetup()
#     driver = browser.way1(URL)
#     report = ReportPanel(driver)
#     report.is_report_page_available()
#     driver.quit()


from utilities.browser_setup import BrowserSetup
from pages.report_panel import ReportPanel
import pytest

URL = "http://localhost:2004"
Report_BUTTON_XPATH = "//label[@class='leftbarButtonGroup btn btn-primary' and @for='navbar-toggle-5']"
View_report = "//button[@id='report_toolbar_refresh_button']"
Download_current_HTML = "//button[@id='report_toolbar_download_html_button']"
Download_BSUT_report = "//button[@id='report_toolbar_dwonload_dut_button']"
report_data_management = "//button[text()='Report Data Management']"
Synthetic_File = "//button[text()='Synthetic File']"

@pytest.fixture(scope="module")
def setup():
    browser = BrowserSetup()
    driver = browser.way1(URL)
    yield driver
    driver.quit()

def test_report_button_available(setup):
    """
    Test Case 1: Verify if the Report button is available and clickable.
    """
    report = ReportPanel(setup)
    assert report.is_report_page_available(), "Report button is not available."

def test_view_report_button_available(setup):
    """
    Test Case 2: Verify if the View Report button is available.
    """
    report = ReportPanel(setup)
    assert report.verify_button_available("View Report", View_report), "View Report button is not available."

def test_download_current_html_button_available(setup):
    """
    Test Case 3: Verify if the Download Current HTML button is available.
    """
    report = ReportPanel(setup)
    assert report.verify_button_available("Download Current HTML", Download_current_HTML), "Download Current HTML button is not available."

def test_download_bsut_report_button_available(setup):
    """
    Test Case 4: Verify if the Download BSUT Report button is available.
    """
    report = ReportPanel(setup)
    assert report.verify_button_available("Download BSUT Report", Download_BSUT_report), "Download BSUT Report button is not available."

def test_report_data_management_button_available(setup):
    """
    Test Case 5: Verify if the Report Data Management button is available.
    """
    report = ReportPanel(setup)
    assert report.verify_button_available("Report Data Management", report_data_management), "Report Data Management button is not available."

def test_synthetic_file_button_available(setup):
    """
    Test Case 6: Verify if the Synthetic File button is available.
    """
    report = ReportPanel(setup)
    assert report.verify_button_available("Synthetic File", Synthetic_File), "Synthetic File button is not available."