
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://localhost:2004/v3220136.html")
wait = WebDriverWait(driver, 10)

rand_str = ''.join(random.choices(string.ascii_lowercase, k=8))

# XPath locators
test_config = "//*[text()='Test Configuration']"
create_proj = "//span[@class='project-name-label cursorPointer']"
input_project = "//input[@placeholder='New Project name']"
pre_compliance = "//label[contains(text(), 'Pre-Compliance')]"
power_profile_xpath = "//label[text()='PowerProfile']/following-sibling::select"
supported_specification_xpath = "//label[text()='SupportedSpecification']/following-sibling::select"
get_default_sdf_r = "//input[@id='uploadType' and @name='uploadType' and @type='radio']"
get_default_sdf = "//button[@class='grl-button' and text()='Get Default ESDF']"
create_project = "//button[@class='grl-button' and text()='Create Project']"
test_case_count = "//div[@class='testCaseSelectionCount']"

# Step 1-5 setup
wait.until(EC.element_to_be_clickable((By.XPATH, test_config))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, create_proj))).click()
wait.until(EC.presence_of_element_located((By.XPATH, input_project))).send_keys(rand_str)
wait.until(EC.element_to_be_clickable((By.XPATH, pre_compliance))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, get_default_sdf_r))).click()

# Loop through PowerProfile and SupportedSpecification
power_profile_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, power_profile_xpath))))
for i in range(len(power_profile_dropdown.options)):
    power_profile_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, power_profile_xpath))))
    power_profile_dropdown.select_by_index(i)
    power_profile_value = power_profile_dropdown.options[i].text.strip()

    spec_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, supported_specification_xpath))))
    for j in range(len(spec_dropdown.options)):
        try:
            spec_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, supported_specification_xpath))))
            option = spec_dropdown.options[j]
            if option.get_attribute("disabled"):
                continue

            spec_dropdown.select_by_index(j)
            spec_value = option.text.strip()

            wait.until(EC.element_to_be_clickable((By.XPATH, get_default_sdf))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, create_project))).click()

            count_text = wait.until(EC.presence_of_element_located((By.XPATH, test_case_count))).text
            print(f"{power_profile_value}, {spec_value} = {count_text}")

            # Re-open project popup to continue testing next combinations
            wait.until(EC.element_to_be_clickable((By.XPATH, create_proj))).click()
            input_box = wait.until(EC.presence_of_element_located((By.XPATH, input_project)))
            input_box.clear()
            input_box.send_keys(rand_str)
            wait.until(EC.element_to_be_clickable((By.XPATH, pre_compliance))).click()
            wait.until(EC.element_to_be_clickable((By.XPATH, get_default_sdf_r))).click()
            power_profile_dropdown = Select(wait.until(EC.presence_of_element_located((By.XPATH, power_profile_xpath))))
            power_profile_dropdown.select_by_index(i)

        except Exception as e:
            print(f"Error while processing {power_profile_value}, {j}: {e}")
            continue

driver.quit()
