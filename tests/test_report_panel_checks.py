from utilities.browser_setup import BrowserSetup
from pages.report_panel import ReportPanel
import pytest
import logging

URL = "http://localhost:2004"

@pytest.fixture(scope="module")
def setup():
    browser = BrowserSetup()
    driver = browser.way1(URL)
    yield driver
    driver.quit()

def test_report_button_available(setup):
    report = ReportPanel(setup)
    assert report.is_report_page_available(), "Report button is not available."

def test_view_report_button_available(setup):
    report = ReportPanel(setup)
    assert report.verify_button_available("View Report", "//button[@id='report_toolbar_refresh_button']"), "View Report button is not available."

def test_download_current_html_flow(setup):
    report = ReportPanel(setup)
    assert report.handle_download_current_html_flow(), "Download Current HTML flow failed."

def test_download_current_bsut_flow(setup):
    report = ReportPanel(setup)
    assert report.handle_download_bsut_flow(), "Download Current BSUT Report Data flow failed."

# def test_report_data_management_flow(setup):
#     report = ReportPanel(setup)
#     assert report.handle_report_data_management_flow(), "Report Data Management flow failed."

def test_report_data_management_flow(setup):
    """
    Test Case: Validate the Report Data Management Panel Behavior
    Steps:
        1. Click on Report Data Management
        2. Check Delete Test Report button availability
        3. Check Test Results Folder Size text
        4. Check Delete Report buttons
        5. Perform Cancel flow on Delete Report popup
        6. Perform Download Report action
        7. Click Delete Test Report button
        8. Verify Confirmation popup
        9. Click Cancel on confirmation
    """
    report = ReportPanel(setup)
    assert report.handle_report_data_management_flow(), "Report Data Management flow failed."
def test_Synthetic_File(setup):
    
    report = ReportPanel(setup)
    assert report.handle_synthetic_file_popup(), " Synthetic File btn function failed."


def test_write_close_btn_verification(setup):
        
        """
        Test Case: Validate Write Button, Error Popup, and Navigation Back to Report Page.
        Steps:
            1. Check Write button availability.
            2. Check if it is clickable.
            3. Click Write button.
            4. Verify error popup appears.
            5. Click Close/Cancel button on popup.
            6. Verify navigation back to Report page.
        """
        logging.info("====== Test: Write Button + Error Popup + Return to Report Page ======")

        report_panel = ReportPanel(setup)
        result = report_panel.write_close_btn_verification()

        assert result, "Write button flow validation failed."

