import random
import string
import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utilities.browser_setup import BrowserSetup

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

URL = "http://localhost:2004/v3220136.html"

@pytest.fixture(scope="module")
def driver():
    logging.info("Initializing WebDriver")
    browser = BrowserSetup()
    driver = browser.way1(URL)
    yield driver
    logging.info("Closing WebDriver")
    driver.quit()

def get_random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

@pytest.mark.sanity
def test_project_creation_and_spec_combinations(driver):
    wait = WebDriverWait(driver, 10)
    rand_str = get_random_string()

    # Locators
    locators = {
        "test_config": "//*[text()='Test Configuration']",
        "create_proj": "//span[@class='project-name-label cursorPointer']",
        "input_project": "//input[@placeholder='New Project name']",
        "pre_compliance": "//label[contains(text(), 'Pre-Compliance')]",
        "power_profile": "//label[text()='PowerProfile']/following-sibling::select",
        "supported_spec": "//label[text()='SupportedSpecification']/following-sibling::select",
        "get_default_sdf_r": "//input[@id='uploadType' and @name='uploadType' and @type='radio']",
        "get_default_sdf": "//button[@class='grl-button' and text()='Get Default ESDF']",
        "create_project": "//button[@class='grl-button' and text()='Create Project']",
        "test_case_count": "//div[@class='testCaseSelectionCount']"
    }

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, locators["test_config"]))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, locators["create_proj"]))).click()
        wait.until(EC.presence_of_element_located((By.XPATH, locators["input_project"]))).send_keys(rand_str)
        wait.until(EC.element_to_be_clickable((By.XPATH, locators["pre_compliance"]))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, locators["get_default_sdf_r"]))).click()

        power_profile_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, locators["power_profile"]))))

        for i in range(len(power_profile_dropdown.options)):
            power_profile_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, locators["power_profile"]))))
            power_profile_dropdown.select_by_index(i)
            power_profile_value = power_profile_dropdown.options[i].text.strip()

            spec_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, locators["supported_spec"]))))

            for j in range(len(spec_dropdown.options)):
                try:
                    spec_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, locators["supported_spec"]))))
                    spec_option = spec_dropdown.options[j]

                    if spec_option.get_attribute("disabled"):
                        continue

                    spec_dropdown.select_by_index(j)
                    spec_value = spec_option.text.strip()

                    wait.until(EC.element_to_be_clickable((By.XPATH, locators["get_default_sdf"]))).click()
                    wait.until(EC.element_to_be_clickable((By.XPATH, locators["create_project"]))).click()

                    count_text = wait.until(EC.presence_of_element_located((By.XPATH, locators["test_case_count"]))).text
                    logging.info(f"{power_profile_value}, {spec_value} = {count_text}")

                    # Reopen modal for next loop
                    wait.until(EC.element_to_be_clickable((By.XPATH, locators["create_proj"]))).click()
                    input_box = wait.until(EC.presence_of_element_located((By.XPATH, locators["input_project"])))
                    input_box.clear()
                    input_box.send_keys(rand_str)
                    wait.until(EC.element_to_be_clickable((By.XPATH, locators["pre_compliance"]))).click()
                    wait.until(EC.element_to_be_clickable((By.XPATH, locators["get_default_sdf_r"]))).click()
                    power_profile_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, locators["power_profile"]))))
                    power_profile_dropdown.select_by_index(i)

                except Exception as inner_e:
                    logging.warning(f"Skipping {power_profile_value} - {j} due to error: {inner_e}")
                    continue

    except Exception as e:
        logging.error(f"Test failed due to error: {e}")
        driver.save_screenshot("test_failure_screenshot.png")
        pytest.fail(f"Test failed due to error: {e}")
