import os
import logging

def check_file_exists(file_path):
    """Check if a file exists at the given path."""
    if os.path.isfile(file_path):
        logging.info(f"File found: {file_path}")
        return True
    else:
        logging.error(f"File not found: {file_path}")
        return False

def check_directory_exists(directory_path):
    """Check if a directory exists at the given path."""
    if os.path.isdir(directory_path):
        logging.info(f"Directory found: {directory_path}")
        return True
    else:
        logging.error(f"Directory not found: {directory_path}")
        return False

def check_file_content(file_path, expected_content):
    """Check if the file contains the expected content."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            if expected_content in content:
                logging.info(f"File content verified: {file_path}")
                return True
            else:
                logging.error(f"File content mismatch in: {file_path}")
                return False
    except Exception as e:
        logging.error(f"Error reading file {file_path}: {str(e)}")
        return False

def check_firmware_files(directory_path, expected_files):
    """Check if all expected firmware files are present in the directory."""
    missing_files = []
    for file_name in expected_files:
        file_path = os.path.join(directory_path, file_name)
        if not check_file_exists(file_path):
            missing_files.append(file_name)
    if missing_files:
        logging.error(f"Missing firmware files: {missing_files}")
        return False
    else:
        logging.info("All firmware files are present.")
        return True