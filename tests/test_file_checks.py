import logging
import pytest
from pages.fileverification  import *
# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

# Constants
INSTALLATION_PATH = r"C:\GRL\GRL-C3-MP-TPT"
README_FILE = os.path.join(INSTALLATION_PATH, "ReadMe.txt")
RELEASE_NOTES_FILE = os.path.join(INSTALLATION_PATH, "GRL-C3-TPT Release Notes.pdf")
ELOAD_FILE = os.path.join(INSTALLATION_PATH, r"Firmware_Files\BPP_EPP\PPS_ELOAD.bin")
FIRMWARE_DIRECTORY = os.path.join(INSTALLATION_PATH, r"Firmware_Files\BPP_EPP")
EXPECTED_FIRMWARE_FILES = ["BOOT.BIN", "image.ub", "start.sh"]

# Test Case 1: Check for the Readme file
def test_check_readme_file():
    """Verify the Readme file exists and contains the correct content."""
    logging.info("Starting test: Check for the Readme file")
    assert check_file_exists(README_FILE), "Readme file not found."
    assert check_file_content(README_FILE, "Software Version"), "Readme file content mismatch."
    logging.info("Readme file verification passed.")

# Test Case 2: Check for the Release Notes file
def test_check_release_notes_file():
    """Verify the Release Notes file exists."""
    logging.info("Starting test: Check for the Release Notes file")
    assert check_file_exists(RELEASE_NOTES_FILE), "Release Notes file not found."
    logging.info("Release Notes file verification passed.")

# Test Case 3: Check for the Eload files
def test_check_eload_files():
    """Verify the Eload file exists."""
    logging.info("Starting test: Check for the Eload files")
    assert check_file_exists(ELOAD_FILE), "Eload file not found."
    logging.info("Eload file verification passed.")

# Test Case 4: Check for the Firmware files
def test_check_firmware_files():
    """Verify all expected firmware files are present."""
    logging.info("Starting test: Check for the Firmware files")
    assert check_directory_exists(FIRMWARE_DIRECTORY), "Firmware directory not found."
    assert check_firmware_files(FIRMWARE_DIRECTORY, EXPECTED_FIRMWARE_FILES), "Firmware files missing."
    logging.info("Firmware files verification passed.")

# Main execution (for debugging purposes)
if __name__ == "__main__":
    pytest.main([__file__, "-v"])