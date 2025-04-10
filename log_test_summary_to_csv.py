# import json
# import csv
# import os
# from datetime import datetime

# # Load software version from version.properties
# version_file = "version.properties"
# build_version = "Unknown"
# if os.path.exists(version_file):
#     with open(version_file) as f:
#         for line in f:
#             if line.startswith("BUILD_VERSION="):
#                 build_version = line.strip().split("=")[1]

# # Load pytest JSON report
# json_file = "pytest-report.json"
# with open(json_file, "r") as f:
#     data = json.load(f)

# # Extract summary
# summary = data.get("summary", {})
# total = summary.get("total", 0)
# passed = summary.get("passed", 0)
# failed = summary.get("failed", 0)
# skipped = summary.get("skipped", 0)
# expected = "Pass"
# result = "Passed" if failed == 0 else "Failed"

# # Gather remarks from failed tests
# remarks = ""
# if "tests" in data:
#     for test in data["tests"]:
#         if test.get("outcome") == "failed":
#             nodeid = test.get("nodeid", "unknown_test")
#             msg = test.get("call", {}).get("longrepr", "No details")
#             remarks += f"{nodeid} failed. "

# if not remarks:
#     remarks = "All tests passed."

# # Jenkins build number and timestamp
# job_number = os.getenv("BUILD_NUMBER", "Unknown")
# timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")

# # Output CSV
# csv_file = "build_results_log.csv"
# file_exists = os.path.exists(csv_file)

# with open(csv_file, "a", newline="") as f:
#     writer = csv.writer(f)
#     if not file_exists:
#         writer.writerow([ "SW Version", "Result", "Expected", "Total", "Passed", "Failed", "Skipped", "Timestamp", "Remarks"])
#     writer.writerow([build_version, result, expected, total, passed, failed, skipped, timestamp, remarks])

import json
import csv
import os
from datetime import datetime

# Load software version from version.properties
def load_version(file_path):
    build_version = "Unknown"
    if os.path.exists(file_path):
        with open(file_path) as f:
            for line in f:
                if line.startswith("BUILD_VERSION="):
                    build_version = line.strip().split("=")[1]
    return build_version

# Load pytest JSON report and extract summary
def load_pytest_report(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

# Extract the summary details from the pytest report
def extract_summary(data):
    summary = data.get("summary", {})
    return summary.get("total", 0), summary.get("passed", 0), summary.get("failed", 0), summary.get("skipped", 0)

# Gather remarks from failed tests and comparison with previous version
def gather_remarks(data, previous_version_results):
    remarks = []
    if "tests" in data:
        for test in data["tests"]:
            nodeid = test.get("nodeid", "unknown_test")
            outcome = test.get("outcome")
            if outcome == "failed":
                msg = test.get("call", {}).get("longrepr", "No details")
                remarks.append(f"{nodeid} failed. Details: {msg}")
            # Check for comparison between versions if result is different
            test_name = test.get("nodeid")
            if previous_version_results.get(test_name) != outcome:
                remarks.append(f"Comparison mismatch for {test_name}: Sw v1: {previous_version_results.get(test_name)} vs Sw v2: {outcome}")
    return remarks if remarks else ["All tests passed."]

# Write results to CSV
def write_to_csv(file_path, test_category, test_name, sw_v1_result, sw_v2_result, comparison, error_message, timestamp):
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            # Write headers only if the file is new
            writer.writerow([ "Test Category", "Test Case Name", "Sw v1 Result", "Sw v2 Result", "Comparison", "Error Message (if any)"])
        writer.writerow([test_category, test_name, sw_v1_result, sw_v2_result, comparison, error_message])

# Main execution
if __name__ == "__main__":
    # Load software version
    version_file = "version.properties"
    build_version = load_version(version_file)

    # Load pytest JSON report
    json_file = "pytest-report.json"
    data = load_pytest_report(json_file)

    # Extract summary data
    total, passed, failed, skipped = extract_summary(data)
    expected = "Pass"
    result = "Passed" if failed == 0 else "Failed"

    # Assume that we get previous test results from a CSV or another file. Here, using a sample comparison dictionary.
    previous_version_results = {
        "test_TC35_Coil_Type_dropdown_checking": "PASS",
        "test_TC36_Coil_Type_dropdown_checking": "PASS",
        # Add more test results here for Sw v1
    }

    # Gather remarks and comparison results
    remarks = gather_remarks(data, previous_version_results)

    # Jenkins build number and timestamp
    job_number = os.getenv("BUILD_NUMBER", "Unknown")
    timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")

    # Output CSV file
    csv_file = "build_results_log.csv"
    
    for remark in remarks:
        test_category = "test_Qi_Exerciser_checks"  # You can change the logic to extract actual test categories from data
        test_name = "test_TC35_Coil_Type_dropdown_checking"  # Example, extract test name from data
        sw_v1_result = "PASS"  # Assume v1 result from previous version or stored somewhere
        sw_v2_result = "PASS"  # This will be from the current test run
        comparison = "PASS" if sw_v1_result == sw_v2_result else "FAIL"
        error_message = remark if "failed" in remark else ""
        
        write_to_csv(csv_file, test_category, test_name, sw_v1_result, sw_v2_result, comparison, error_message, timestamp)

    print(f"Test result logged to {csv_file}")
