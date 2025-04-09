
# import logging
# import pytest
# from pages.fileverification import *
# import os



# # -----------------------------
# # Test Case 1: Check for ReadMe.txt
# # -----------------------------
# def test_check_readme_file():
#     """
#     Test Case: Verify ReadMe File Existence and Content """

# #    """ Steps:
# #         1. Verify if the 'ReadMe.txt' file exists in the installation directory.
# #         2. Open the file and check if it contains the keyword 'Software Version'.
# #         3. Log success if both conditions are met.
# #         4. If missing or content mismatch, log error and fail the test.
# #     """
#     logging.info("Starting test: Check for the Readme file")
#     assert check_file_exists(README_FILE), "Readme file not found."
#     assert check_file_content(README_FILE, "Software Version"), "Readme file content mismatch."
#     logging.info("Readme file verification passed.")

# # -----------------------------
# # Test Case 2: Check for Release Notes PDF
# # -----------------------------
# def test_check_release_notes_file():
#     """
#     Test Case: Verify Release Notes File Existence

#     Steps:
#         1. Verify if the 'GRL-C3-TPT Release Notes.pdf' file exists in the installation directory.
#         2. Log success if the file exists.
#         3. If missing, log error and fail the test.
#     """
#     logging.info("Starting test: Check for the Release Notes file")
#     assert check_file_exists(RELEASE_NOTES_FILE), "Release Notes file not found."
#     logging.info("Release Notes file verification passed.")

# # -----------------------------
# # Test Case 3: Check for ELOAD Firmware File
# # -----------------------------
# def tc1_test_check_eload_files():
#     """
#     Test Case: Verify ELOAD Firmware File Existence

#     Steps:
#         1. Verify if the 'PPS_ELOAD.bin' firmware file exists in the Firmware_Files/BPP_EPP folder.
#         2. Log success if the file exists.
#         3. If missing, log error and fail the test.
#     """
#     logging.info("Starting test: Check for the Eload files")
#     assert check_file_exists(ELOAD_FILE), "Eload file not found."
#     logging.info("Eload file verification passed.")

# # -----------------------------
# # Test Case 4: Check for Mandatory Firmware Files
# # -----------------------------
# def test_check_firmware_files():
#     """
#     Test Case: Verify Presence of Mandatory Firmware Files

#     Steps:
#         1. Verify if the firmware directory 'Firmware_Files/BPP_EPP' exists.
#         2. Verify that all expected files ['BOOT.BIN', 'image.ub', 'start.sh'] are present inside the directory.
#         3. Log success if all files are found.
#         4. If directory or files are missing, log error and fail the test.
#     """
#     logging.info("Starting test: Check for the Firmware files")
#     assert check_directory_exists(FIRMWARE_DIRECTORY), "Firmware directory not found."
#     assert check_firmware_files(FIRMWARE_DIRECTORY, EXPECTED_FIRMWARE_FILES), "Firmware files missing."
#     logging.info("Firmware files verification passed.")

# # -----------------------------
# # Optional: Debug Mode
# # -----------------------------
# if __name__ == "__main__":
#     pytest.main([__file__, "-v"])


import logging
import pytest
from pages.fileverification import *
import os
# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Constants
INSTALLATION_PATH = r"C:\GRL\GRL-C3-MP-TPT"
README_FILE = os.path.join(INSTALLATION_PATH, "ReadMe.txt")
RELEASE_NOTES_FILE = os.path.join(INSTALLATION_PATH, "GRL-C3-TPT Release Notes.pdf")
ELOAD_FILE = os.path.join(INSTALLATION_PATH, r"Firmware_Files\BPP_EPP\PPS_ELOAD.bin")
FIRMWARE_DIRECTORY = os.path.join(INSTALLATION_PATH, r"Firmware_Files\BPP_EPP")
EXPECTED_FIRMWARE_FILES = ["BOOT.BIN", "image.ub", "start.sh"]

# -----------------------------
# TC1: Check for ReadMe File
# -----------------------------
def tc1_test_check_readme_file():
    """
    Test Case: Verify ReadMe File Existence and Content
    """
    logging.info("Starting test: Check for the Readme file")
    assert check_file_exists(README_FILE), "Readme file not found."
    assert check_file_content(README_FILE, "Software Version"), "Readme file content mismatch."
    logging.info("Readme file verification passed.")

# -----------------------------
# TC2: Check for Release Notes PDF
# -----------------------------
def tc2_test_check_release_notes_file():
    """
    Test Case: Verify Release Notes File Existence
    """
    logging.info("Starting test: Check for the Release Notes file")
    assert check_file_exists(RELEASE_NOTES_FILE), "Release Notes file not found."
    logging.info("Release Notes file verification passed.")

# -----------------------------
# TC3: Check for ELOAD Firmware File
# -----------------------------
def tc3_test_check_eload_files():
    """
    Test Case: Verify ELOAD Firmware File Existence
    """
    logging.info("Starting test: Check for the Eload files")
    assert check_file_exists(ELOAD_FILE), "Eload file not found."
    logging.info("Eload file verification passed.")

# -----------------------------
# TC4: Check for Mandatory Firmware Files
# -----------------------------
def tc4_test_check_firmware_files():
    """
    Test Case: Verify Presence of Mandatory Firmware Files
    """
    logging.info("Starting test: Check for the Firmware files")
    assert check_directory_exists(FIRMWARE_DIRECTORY), "Firmware directory not found."
    assert check_firmware_files(FIRMWARE_DIRECTORY, EXPECTED_FIRMWARE_FILES), "Firmware files missing."
    logging.info("Firmware files verification passed.")

# -----------------------------
# Optional: Debug Mode
# -----------------------------
if __name__ == "__main__":
    pytest.main([__file__, "-v"])
