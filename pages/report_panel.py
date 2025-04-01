import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Button XPaths
Report_BUTTON_XPATH = "//label[@class='leftbarButtonGroup btn btn-primary' and @for='navbar-toggle-5']"
View_report = "//button[@id='report_toolbar_refresh_button']"
Download_current_HTML = "//button[@id='report_toolbar_download_html_button']"
Download_BSUT_report = "//button[@id='report_toolbar_dwonload_dut_button']"
report_data_management = "//button[text()='Report Data Management']"
Synthetic_File = "//button[text()='Synthetic File']"
Popup_OK = "//button[@class='popupButtons popupButton_Ok btn btn-primary']"
Popup_Cancel = "//button[@class='popupButtons popupButton_Cancel btn btn-secondary']"
Popup_Error_Message = "//div[@class='Toastify__toast Toastify__toast--error']"
Delete_test_report = "//button[@id='report_toolbar_delete_report_button']"
total_size_txt = "//small[@class='artifacts-fonts']"
delete_report = "//button[text()='Delete Report' and @id='0']"
dowwload_report = "//button[text()='Download Report' and @id='0']"
txt_del_test_report_btn = "//strong[contains(@class,'displayMessage') and contains(text(),'permanently delete')]"
file_path = "//input[@class='ms-1 synthetic_channel_field']"
VC_chckbox = "//label[span[contains(text(),'Enable VCTx')]]//input[@type='checkbox']"
close_btn  = "//button[@class='btn-close']"
write_btn = "//button[@class='ms-1 grl-button']"

class ReportPanel:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def is_report_page_available(self):
        try:
            logging.info("Step: Checking Report Button availability")
            report_button = self.driver.find_element(By.XPATH, Report_BUTTON_XPATH)
            if report_button.is_displayed():
                logging.info("Report button is available.")
                report_button.click()
                logging.info("Clicked Report button.")
                time.sleep(2)
                return True
        except Exception as e:
            logging.error(f"Report button is not present: {e}")
            return False

    def verify_button_available(self, button_name, button_xpath):
        try:
            logging.info(f"Step: Checking '{button_name}' button availability")
            button = self.driver.find_element(By.XPATH, button_xpath)
            if button.is_displayed():
                logging.info(f"{button_name} button is available.")
                return True
            else:
                logging.error(f"{button_name} button is not displayed.")
                return False
        except Exception as e:
            logging.error(f"Error finding {button_name} button: {e}")
            return False

    def handle_download_current_html_flow(self):
        try:
            logging.info("====== Starting Download Current HTML Button Flow ======")

            logging.info("Step 1: Clicking Download Current HTML button")
            download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Download_current_HTML)))
            download_button.click()

            logging.info("Step 2: Waiting for popup OK and Cancel buttons")
            popup_ok = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_OK)))
            popup_cancel = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_Cancel)))
            logging.info("Step 2 Result: Popup OK and Cancel buttons are available")

            logging.info("Step 3: Clicking Cancel")
            popup_cancel.click()

            logging.info("Step 4: Verifying Download Current HTML button availability after Cancel")
            download_button = self.wait.until(EC.presence_of_element_located((By.XPATH, Download_current_HTML)))
            assert download_button.is_displayed(), "Download Current HTML button disappeared after Cancel."
            logging.info("Step 4 Result: Download Current HTML button is available after Cancel")

            logging.info("Step 5: Clicking Download Current HTML button again")
            download_button.click()

            logging.info("Step 6: Clicking OK in popup")
            popup_ok = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_OK)))
            popup_ok.click()

            logging.info("Step 7: Waiting for error popup to appear")
            error_popup = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_Error_Message)))
            assert error_popup.is_displayed(), "Error popup did not appear after clicking OK."
            logging.info(f"Step 7 Result: Error popup text - {error_popup.text}")

            logging.info("Step 8: Waiting for error popup to disappear (max 15 seconds)")
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(error_popup))

            logging.info("Step 9: Verifying Download Current HTML button availability after error popup")
            download_button = self.wait.until(EC.presence_of_element_located((By.XPATH, Download_current_HTML)))
            assert download_button.is_displayed(), "Download Current HTML button not available after error popup disappears."
            logging.info("====== Completed Download Current HTML Button Flow Successfully ======")

            return True

        except Exception as e:
            logging.error(f"Download Current HTML flow failed: {e}")
            # self.driver.save_screenshot(f"failure_html_{int(time.time())}.png")
            # logging.info("Screenshot saved for debugging.")
            raise

    def handle_download_bsut_flow(self):
        try:
            logging.info("====== Starting Download Current BSUT Report Data Button Flow ======")

            logging.info("Step 1: Clicking Download Current BSUT Report Data button")
            download_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Download_BSUT_report)))
            download_button.click()

            logging.info("Step 2: Waiting for popup OK and Cancel buttons")
            popup_ok = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_OK)))
            popup_cancel = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_Cancel)))
            logging.info("Step 2 Result: Popup OK and Cancel buttons are available")

            logging.info("Step 3: Clicking Cancel")
            popup_cancel.click()

            logging.info("Step 4: Verifying Download Current BSUT Report Data button availability after Cancel")
            download_button = self.wait.until(EC.presence_of_element_located((By.XPATH, Download_BSUT_report)))
            assert download_button.is_displayed(), "Download Current BSUT Report Data button disappeared after Cancel."
            logging.info("Step 4 Result: Download Current BSUT Report Data button is available after Cancel")

            logging.info("Step 5: Clicking Download Current BSUT Report Data button again")
            download_button.click()

            logging.info("Step 6: Clicking OK in popup")
            popup_ok = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_OK)))
            popup_ok.click()

            logging.info("Step 7: Waiting for error popup to appear")
            error_popup = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_Error_Message)))
            assert error_popup.is_displayed(), "Error popup did not appear after clicking OK."
            logging.info(f"Step 7 Result: Error popup text - {error_popup.text}")

            logging.info("Step 8: Waiting for error popup to disappear (max 15 seconds)")
            WebDriverWait(self.driver, 15).until(EC.invisibility_of_element(error_popup))

            logging.info("Step 9: Verifying Download Current BSUT Report Data button availability after error popup")
            download_button = self.wait.until(EC.presence_of_element_located((By.XPATH, Download_BSUT_report)))
            assert download_button.is_displayed(), "Download Current BSUT Report Data button not available after error popup disappears."
            logging.info("====== Completed Download Current BSUT Report Data Button Flow Successfully ======")

            return True

        except Exception as e:
            logging.error(f"Download Current BSUT Report Data flow failed: {e}")
            self.driver.save_screenshot(f"failure_bsut_{int(time.time())}.png")
            logging.info("Screenshot saved for debugging.")
            raise
            
    def handle_report_data_management_flow(self):
        try:
            logging.info("====== Starting Report Data Management Flow ======")

            # Step 1
            logging.info("Step 1: Clicking Report Data Management button")
            report_data_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, report_data_management)))
            report_data_btn.click()

            # Step 2
            logging.info("Step 2: Checking Delete Test Report button availability")
            delete_test_report_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, Delete_test_report)))
            assert delete_test_report_btn.is_displayed(), "Delete Test Report button is not available"

            # Step 3
            logging.info("Step 3: Checking Test results folder size label")
            folder_size_label = self.wait.until(EC.presence_of_element_located((By.XPATH, total_size_txt)))
            assert folder_size_label.is_displayed(), "Test results folder size text not found"
            logging.info(f"Test results folder info: {folder_size_label.text}")

            # Step 4
            logging.info("Step 4: Checking Delete Report button availability")
            delete_report_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, delete_report)))
            assert delete_report_btn.is_displayed(), "Delete Report button not available"

            # Step 5
            logging.info("Step 5: Clicking Delete Report button")
            delete_report_btn.click()

            logging.info("Step 5.1: Checking OK and Cancel buttons in popup")
            popup_ok = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_OK)))
            popup_cancel = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_Cancel)))
            assert popup_ok.is_displayed(), "Popup OK button not available"
            assert popup_cancel.is_displayed(), "Popup Cancel button not available"

            logging.info("Step 5.2: Clicking Cancel on popup")
            popup_cancel.click()

            # Step 6
            logging.info("Step 6: Clicking Download Report button")
            download_report_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, dowwload_report)))
            download_report_btn.click()
            logging.info("Step 6.1: Waiting for 10 seconds for download to process")
            time.sleep(10)

            # Step 7
            logging.info("Step 7: Clicking Delete Test Report button (Re-fetching due to possible stale)")
            delete_test_report_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, Delete_test_report)))
            delete_test_report_btn.click()

            # Step 8
            logging.info("Step 8: Checking Confirmation Text")
            confirmation_popup_text = self.wait.until(EC.presence_of_element_located((By.XPATH, txt_del_test_report_btn)))
            assert confirmation_popup_text.is_displayed(), "Delete confirmation popup text not visible"
            logging.info(f"Confirmation popup text: {confirmation_popup_text.text}")

            # Step 9
            logging.info("Step 9: Checking OK and Cancel buttons in confirmation popup")
            popup_ok = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_OK)))
            popup_cancel = self.wait.until(EC.presence_of_element_located((By.XPATH, Popup_Cancel)))
            assert popup_ok.is_displayed(), "OK button not available in confirmation popup"
            assert popup_cancel.is_displayed(), "Cancel button not available in confirmation popup"

            logging.info("Step 9.1: Clicking Cancel on confirmation popup")
            popup_cancel.click()

            close_btn_report = self.wait.until(EC.presence_of_element_located((By.XPATH, close_btn)))
            close_btn_report.click()

            


            logging.info("====== Completed Report Data Management Flow Successfully ======")
            return True

        except Exception as e:
            logging.error(f"Report Data Management flow failed: {e}")
            self.driver.save_screenshot(f"failure_report_data_management_{int(time.time())}.png")
            raise
   
 
    def handle_synthetic_file_popup(self):

        try:
            logging.info("====== Starting Synthetic File Popup Dropdown Value Print ======")

            # Step 1: Click Synthetic File button
            logging.info("Step 1: Clicking Synthetic File button")
            synthetic_file_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, Synthetic_File)))
            synthetic_file_btn.click()

            # Step 2: Wait for popup to load
            logging.info("Waiting for popup to be fully loaded...")
            self.wait.until(EC.presence_of_element_located((By.XPATH, file_path)))

            # Step 3: Input box check
            logging.info("Step 3: Validating input box")
            file_input = self.wait.until(EC.presence_of_element_located((By.XPATH, file_path)))
            test_values = ["12345", "abcDEF", "!@#$%", "abc123!@#"]
            for value in test_values:
                file_input.clear()
                file_input.send_keys(value)
                assert file_input.get_attribute("value") == value, f"Failed input: {value}"
                logging.info(f"Typed and verified: {value}")

            # Step 4: Checkbox toggle
            logging.info("Step 4: Toggling VC-Tx checkbox")
            checkbox = self.wait.until(EC.presence_of_element_located((By.XPATH, VC_chckbox)))
            checkbox.click()
            logging.info("Checkbox clicked")
            checkbox.click()

            # Step 5: Dropdown extraction
            dropdowns = {
                "File Source": '(//div[@class="synthetic_channel_wrapper_MPP_TPT"]//child::button)[1]',
                "Test Mode":   '(//div[@class="synthetic_channel_wrapper_MPP_TPT"]//child::button)[2]',
                "Test Type":   '(//div[@class="synthetic_channel_wrapper_MPP_TPT"]//child::button)[3]',
                "Channel Type":'(//div[@class="synthetic_channel_wrapper_MPP_TPT"]//child::button)[4]'
            }

            for label, xpath in dropdowns.items():
                logging.info(f"Step 5: Handling dropdown: {label}")
                try:
                    dropdown_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))

                    # Scroll into view using JS
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_btn)
                    time.sleep(0.2)

                    # Click using JS to avoid intercept
                    self.driver.execute_script("arguments[0].click();", dropdown_btn)
                    time.sleep(0.3)

                    # Get dropdown options (support divs, buttons, links, spans)
                    options = self.wait.until(EC.presence_of_all_elements_located((
                        By.XPATH,
                        "//div[contains(@class,'dropdown-menu') and contains(@class,'show')]//div[@role='option' or @role='menuitem' or @role='presentation'] | " +
                        "//div[contains(@class,'dropdown-menu') and contains(@class,'show')]//button | " +
                        "//div[contains(@class,'dropdown-menu') and contains(@class,'show')]//a | " +
                        "//div[contains(@class,'dropdown-menu') and contains(@class,'show')]//span"
                    )))

                    # Log option texts
                    logging.info(f"{label} dropdown options:")
                    for opt in options:
                        option_text = opt.text.strip()
                        if option_text:
                            print(f"    {label} --> {option_text}")
                            logging.info(f"    {label} --> {option_text}")
                    time.sleep(0.5)

                    # Click dropdown again to close it
                    self.driver.execute_script("arguments[0].click();", dropdown_btn)

                except Exception as e:
                    logging.error(f"Error fetching options for dropdown '{label}': {e}")
                    self.driver.save_screenshot(f"failure_dropdown_{label}_{int(time.time())}.png")
                    raise

            logging.info("====== Completed Synthetic File Popup Dropdown Value Print Successfully ======")
            return True

        except Exception as e:
            logging.error(f"Synthetic File Popup Dropdown Print Failed: {e}")
            self.driver.save_screenshot(f"failure_dropdown_general_{int(time.time())}.png")
            raise
    
    def write_close_btn_verification(self):
        try:
            logging.info("====== Starting Write Button Verification Flow ======")

            # Step 1 - Check Write button availability
            logging.info("Step 1: Checking Write button availability")
            write_btn_xpath = "//button[@class='ms-1 grl-button']"
            write_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, write_btn_xpath)))
            assert write_btn.is_displayed(), "Write button is not visible"
            logging.info("Write button is available and visible.")

            # Step 2 - Check if Write button is clickable
            logging.info("Step 2: Checking Write button clickability")
            write_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, write_btn_xpath)))

            # Step 3 - Click Write button
            logging.info("Step 3: Clicking Write button")
            write_btn.click()

            # Optional delay before checking popup
            logging.info("Waiting 1.5 seconds to allow popup to render")
            time.sleep(5)

            # Step 4 - Wait for Error Popup
            logging.info("Step 4: Verifying Error popup")
            error_popup_xpath = "//div[contains(@class, 'Toastify__toast--error')]"
            error_popup = self.wait.until(
                EC.presence_of_element_located((By.XPATH, error_popup_xpath))
            )
            assert error_popup.is_displayed(), "Error popup did not appear after clicking Write"
            logging.info("Error popup appeared as expected")

            # Step 5 - Click Close/Cancel button on popup
            close_btn_xpath = "//button[@class='btn-close']"
            logging.info("Step 5: Clicking Close button on error popup")
            close_btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, close_btn_xpath)))
            close_btn.click()

            # Step 6 - Verify if navigated back to Report Page
            logging.info("Step 6: Verifying navigation back to Report page")
            report_label_xpath = "//button[@id='report_toolbar_refresh_button']"
            report_label = self.wait.until(EC.presence_of_element_located((By.XPATH, report_label_xpath)))
            assert report_label.is_displayed(), "Not navigated back to Report page properly"
            logging.info("Successfully navigated back to Report page after closing the popup")

            logging.info("====== Completed Write Button Verification Flow Successfully ======")
            return True

        except Exception as e:
            logging.error(f"Write button flow failed: {e}")
            self.driver.save_screenshot(f"failure_write_button_flow_{int(time.time())}.png")
            raise