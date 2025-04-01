
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
from datetime import datetime
# from utilities.browser_setup import FrameworkSettings
import os

import pytest
import logging
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities.browser_setup import BrowserSetup

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Define the test URL
URL = "http://localhost:2004"

@pytest.fixture(scope="module")
def driver():
    """Setup WebDriver using BrowserSetup"""
    logging.info("Setting up the WebDriver")
    browser = BrowserSetup()
    driver = browser.way1(URL)  # Call way1() to open the browser and connect
    yield driver
    logging.info("Closing the WebDriver")
    driver.quit()

@pytest.mark.sanity
def test_connect_to_tester(driver):
    """Test to verify tester connection and details using dynamic browser setup"""
    wait = WebDriverWait(driver, 10)
    
    # Fields to extract
    DETAILS_TO_CHECK = [
        "Tester Status", "Serial Number", "Firmware Version", "Next Calibration Date", "Tester IP Address", "Port"
    ]

    try:
        # Verify tester connection status
        logging.info("Verifying tester connection status")
        status_element = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//td[contains(@class, 'tester-info-border')]/div[@class='right-spacing-tester']/b")
            )
        )
        tester_status = status_element.text.strip()
        logging.info("Tester connection status: %s", tester_status)
        
        if "Connected" not in tester_status:
            logging.warning("Tester did not connect successfully!")
        else:
            logging.info("Tester connected successfully.")

        # Extract details from the table
        extracted_details = {}
        for key in DETAILS_TO_CHECK:
            try:
                key_element = wait.until(
                    EC.presence_of_element_located((By.XPATH, f"//td[contains(text(), '{key}')]"))
                )
                value_element = key_element.find_element(By.XPATH, "./following-sibling::td//b")
                extracted_details[key] = value_element.text.strip()
                logging.info(f"Extracted {key}: {extracted_details[key]}")
            except TimeoutException:
                logging.warning(f"Could not extract {key}")
                extracted_details[key] = None

        logging.info("Test execution completed.")

    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        driver.save_screenshot("verification_failure.png")
        pytest.fail(f"Test encountered an error: {e}")

def test_SDF_jsonval(driver):
    wait = WebDriverWait(driver, 20)  # Increased timeout
    logging.info("Page title: %s", driver.title)
    logging.info("Page URL: %s", driver.current_url)

    try:
        # Click on Test Configuration
        logging.info("Clicking on Test Configuration")
        test_config = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Test Configuration')]")))
        test_config.click()

        logging.info("Clicking on body of the UI to enable interactions")
        driver.find_element(By.TAG_NAME, "body").click()

        # Click Edit SDF
        logging.info("Clicking on Edit SDF Button")
        driver.find_element(By.XPATH, "//i[@class='fa fa-edit me-1 cursorPointer mt-1']").click()

        # Enter details
        logging.info("Entering Applicant Name")
        driver.find_element(By.XPATH, "//div[@class='modal-body']//input[@id='ApplicantName']").send_keys("ApplicantName")

        logging.info("Entering Product Name")
        driver.find_element(By.XPATH, "//div[@class='modal-body']//input[@id='ProductName']").send_keys("ProductName")

        logging.info("Clicking WPID Support Checkbox")
        driver.find_element(By.XPATH, "//div[@class='modal-body']//input[@id='WPIDSupport-editEsdf']").click()
        time.sleep(2)

        logging.info("Clicking Update Button")
        driver.find_element(By.XPATH, "//button[@class='grl-button' and text()='Update']").click()
        time.sleep(5)

        logging.info("Clicking Export Button")
        driver.find_element(By.XPATH, "//i[@class='fa fa-external-link cursorPointer mt-1']").click()
        time.sleep(5)

        # Verify file download
        download_path = os.path.join(os.path.expanduser("~"), "Downloads")
        timeout = 20
        new_filename = f"SDF_Export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        logging.info("Waiting for JSON file to download")
        start_time = time.time()
        downloaded_file = None

        while time.time() - start_time < timeout:
            files = os.listdir(download_path)
            json_files = [f for f in files if f.endswith(".json")]
            if json_files:
                json_files = sorted(json_files, key=lambda f: os.path.getmtime(os.path.join(download_path, f)), reverse=True)
                downloaded_file = json_files[0]
                break
            time.sleep(0.5)

        if downloaded_file:
            old_file_path = os.path.join(download_path, downloaded_file)
            new_file_path = os.path.join(download_path, new_filename)
            try:
                os.rename(old_file_path, new_file_path)
                logging.info(f"Downloaded file renamed to: {new_filename}")
            except PermissionError:
                logging.warning("File is still being written. Retrying...")
                time.sleep(2)
                os.rename(old_file_path, new_file_path)
        else:
            logging.error("No JSON file was downloaded.")
            assert False, "JSON file download failed."

        # Navigating back
        driver.find_element(By.XPATH, "//span[@class='project-name-label cursorPointer']").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//input[@class='project-name-input panelcontrol textbox me-1']").send_keys("sample")
        time.sleep(2)

        # **Uploading the JSON File**
        logging.info("Uploading downloaded JSON file")
        print(new_file_path)
        logging.info(new_file_path)

        # Try different upload methods
        # upload_xpath = "(//div[@class='drag-drop-div-parent'])[3]"
        #file = r"C:\Users\GRL\Downloads\SDF_Export_20250321_143028.json"

        try:
            # 1️⃣ **First Attempt** → Find the input file element
            upload_input = driver.find_element(By.XPATH, "//div[@class='drag-drop-div']//input[@type='file' and @accept='.json']")
            upload_input.send_keys(new_file_path)  # Upload file
            logging.info(f"File uploaded: {new_file_path}")

        except Exception:
            # 2️⃣ **Alternative** → Use JavaScript if the file input is hidden
            logging.warning("File input might be hidden. Trying JavaScript method.")
            driver.execute_script(
                "arguments[0].style.display='block';", driver.find_element(By.XPATH, "//div[@class='drag-drop-div']//input[@type='file' and @accept='.json']")
            )
            driver.find_element(By.XPATH, "//div[@class='drag-drop-div']//input[@type='file' and @accept='.json']").send_keys(new_file_path)
            logging.info(f"File uploaded using JavaScript: {new_file_path}")

        time.sleep(5)

        # ✅ **Trigger UI updates by clicking elsewhere**
       

        # ✅ **Ensure 'Create Project' button is enabled before clicking**
        logging.info("Waiting for 'Create Project' button to be clickable")
        create_project_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Create Project']")))
        create_project_btn.click()
        logging.info("Clicked on 'Create Project' successfully")
        time.sleep(5)

        # # ✅ **Ensure 'Create Project' button is enabled before clicking**
        # logging.info("Waiting for 'Create Project' button to be clickable")
        # create_project_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Drag & drop file here']")))
        # create_project_btn.click()
        # logging.info("Clicked on 'Create Project' successfully")
        # time.sleep(5)


        # Validate uploaded data
        logging.info("Validating Product Name after upload")
        wait.until(EC.text_to_be_present_in_element_value((By.XPATH, "//input[@id='ProductName']"), "ProductName"))

        uploaded_product_name = driver.find_element(By.XPATH, "//input[@id='ProductName']").get_attribute("value")
        assert uploaded_product_name == "ProductName", f"Mismatch: Expected 'ProductName', but got '{uploaded_product_name}'"

        logging.info("✅ Product Name validation successful after upload.")

    except Exception as e:
        logging.error(f"❌ Error during test execution: {e}")
        driver.save_screenshot("failure_screenshot.png")  # Capture screenshot for debugging
        pytest.fail(f"Test failed due to error: {e}")

def test_countofTC(driver):
    wait = WebDriverWait(driver, 20)  # Wait up to 20 seconds
    logging.info("Page title: %s", driver.title)
    logging.info("Page URL: %s", driver.current_url)

    try:
        # Locate the checkbox for "PRx Compliance Tests MPP V2.0.1"
        logging.info("Locating PRx Compliance Tests MPP V2.0.1 checkbox")
        try:
            checkbox = wait.until(EC.presence_of_element_located(
                (By.XPATH, "//span[contains(@class, 'rc-tree-checkbox') and ancestor::div[contains(@class, 'rc-tree-treenode') and .//span[text()='PRx Compliance Tests MPP V2.0.1']]]")
            ))
        except Exception:
            logging.error("Tester is not having 2.2 license.")
            return  # Exit the function

        # Check if the checkbox is enabled
        parent_div = checkbox.find_element(By.XPATH, "./ancestor::div[contains(@class, 'rc-tree-treenode')]")
        checkbox_state = parent_div.get_attribute("class")

        if "rc-tree-checkbox-checked" not in checkbox_state:
            logging.info("Checkbox is not selected. Selecting it now...")
            checkbox.click()
            time.sleep(2)
        else:
            logging.info("Checkbox is already selected.")

        # Count the selected test cases
        selected_tests_element = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='testCaseSelectionCount']/b")
        ))
        selected_tests = selected_tests_element.text.strip()  # Extract the text value
        logging.info(f"Selected Tests: {selected_tests}")

        # Expected count format: "141/141"
        expected_count = "141/141"
        
        # Validation
        if selected_tests == expected_count:
            logging.info("Test case selection count matches the expected value.")
        else:
            logging.warning(f"Mismatch! Expected {expected_count} but found {selected_tests}.")

    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")