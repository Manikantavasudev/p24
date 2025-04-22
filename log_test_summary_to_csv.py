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

# import json
# import csv
# import os
# from datetime import datetime

# # Load software version from version.properties
# def load_version(file_path):
#     build_version = "Unknown"
#     if os.path.exists(file_path):
#         with open(file_path) as f:
#             for line in f:
#                 if line.startswith("BUILD_VERSION="):
#                     build_version = line.strip().split("=")[1]
#     return build_version

# # Load pytest JSON report
# def load_pytest_report(file_path):
#     with open(file_path, "r") as f:
#         return json.load(f)

# # Write results to CSV (matching your Excel format)
# def write_to_csv(file_path, job_number, timestamp, test_name, sw_v1_result, sw_v2_result, error_message):
#     file_exists = os.path.exists(file_path)

#     with open(file_path, "a", newline="") as f:
#         writer = csv.writer(f)
#         if not file_exists:
#             writer.writerow([
#                 "Job number from jenkins", "Date time", "Test case name",
#                 "SWv Result 1.1", "SWv Result1.2", "Error Message (if any)"
#             ])
#         writer.writerow([
#             job_number, timestamp, test_name,
#             sw_v1_result, sw_v2_result, error_message
#         ])

# # Main execution
# if __name__ == "__main__":
#     # File paths
#     version_file = "version.properties"
#     json_file = "pytest-report.json"
#     csv_file = "build_results_log.csv"

#     # Load build version (if needed)
#     build_version = load_version(version_file)

#     # Load pytest results
#     data = load_pytest_report(json_file)

#     # Jenkins build number and timestamp
#     job_number = os.getenv("BUILD_NUMBER", "Unknown")
#     timestamp = datetime.now().strftime("%d:%m:%Y %I:%M:%S %p")

#     # Previous version test results (simulate or load from DB/CSV)
#     previous_version_results = {
#         "test_TC35_Coil_Type_dropdown_checking": "PASS",
#         "test_TC36_Coil_Type_dropdown_checking": "PASS",
#         # Add more mappings as needed
#     }

#     # Iterate over each test result in the JSON
#     for test in data.get("tests", []):
#         test_name = test.get("nodeid", "unknown_test")
#         sw_v2_result = test.get("outcome", "UNKNOWN").upper()
#         sw_v1_result = previous_version_results.get(test_name, "UNKNOWN")

#         # If failed, get long error message
#         error_message = ""
#         if sw_v2_result == "FAILED":
#             error_message = test.get("call", {}).get("longrepr", "No details")
#         elif sw_v1_result != sw_v2_result:
#             error_message = f"Comparison mismatch: Sw v1: {sw_v1_result} vs Sw v2: {sw_v2_result}"

#         # Write to CSV
#         write_to_csv(
#             csv_file,
#             job_number,
#             timestamp,
#             test_name,
#             sw_v1_result,
#             sw_v2_result,
#             error_message
#         )

#     print(f"✅ Test results logged to {csv_file}")

import json
import csv
import os
import sys
import re
from datetime import datetime
from colorama import init, Fore, Style

init()

def load_previous_results(file_path):
    previous_results = {}
    if os.path.exists(file_path):
        with open(file_path, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                test_case_name = row["Test case name"].strip()
                sw_v1_result = row["SWv Result 1.1"].strip().upper()
                previous_results[test_case_name] = sw_v1_result
    return previous_results

def load_pytest_report(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def extract_counts_from_console(log_text):
    selected = deselected = total = 0
    match = re.search(r"collected (\d+) items \/ (\d+) deselected \/ (\d+) selected", log_text)
    if match:
        total, deselected, selected = map(int, match.groups())
    return total, selected, deselected

def write_to_csv(file_path, job_number, timestamp, test_name, sw_v1_result, sw_v2_result, error_message):
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "Job number from jenkins", "Date time", "Test case name",
                "SWv Result 1.1", "SWv Result1.2", "Error Message (if any)"
            ])
        writer.writerow([
            job_number, timestamp, test_name,
            sw_v1_result, sw_v2_result, error_message
        ])
    return file_exists

def generate_summary(test_results):
    summary = {
        "total": len(test_results),
        "passed": 0,
        "failed": 0,
        "unknown": 0,
        "mismatch": 0
    }
    for result in test_results:
        sw_v2_result = result["sw_v2_result"]
        if sw_v2_result == "PASSED":
            summary["passed"] += 1
        elif sw_v2_result == "FAILED":
            summary["failed"] += 1
        else:
            summary["unknown"] += 1
        if result["sw_v1_result"] != result["sw_v2_result"] and result["sw_v1_result"] != "UNKNOWN":
            summary["mismatch"] += 1
    return summary

def print_summary(summary, sw_version, job_number, selected, deselected):
    border = "=" * 80
    print(border)
    print(f"{Fore.CYAN}TEST EXECUTION SUMMARY - SW Version: {sw_version} (Build: {job_number}){Style.RESET_ALL}")
    print(border)
    print(f"Total Tests: {summary['total']}")
    print(f"{Fore.GREEN}Passed: {summary['passed']}{Style.RESET_ALL}")
    print(f"{Fore.RED}Failed: {summary['failed']}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Unknown: {summary['unknown']}{Style.RESET_ALL}")
    print(f"{Fore.MAGENTA}Mismatches between v1.1 and v1.2: {summary['mismatch']}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Selected: {selected}, Deselected: {deselected}{Style.RESET_ALL}")
    print(border)
    if summary['total'] > 0:
        print(f"Pass Rate: {(summary['passed'] / summary['total']) * 100:.2f}%")
    print(border)

if __name__ == "__main__":
    previous_csv = "previous_results.csv"
    json_file = "pytest-report.json"
    output_csv = "build_results_log.csv"
    console_log = "jenkins_console.log"  # log saved from Jenkins if needed

    # Extract SW version
    sw_version = "UNKNOWN"
    try:
        with open("ReadMe.txt", "r") as version_file:
            for line in version_file:
                if "Version" in line:
                    sw_version = line.split(":")[-1].strip()
                    break
    except:
        sw_version = os.getenv("SOFTWARE_VERSION", "3.210.1.20")

    # Jenkins job details
    job_number = os.getenv("BUILD_NUMBER", "104")
    timestamp = datetime.now().strftime("%d:%m:%Y %I:%M:%S %p")

    # Load previous results
    previous_results = load_previous_results(previous_csv)

    # Load pytest data
    try:
        test_data = load_pytest_report(json_file)
    except FileNotFoundError:
        print(f"{Fore.RED}Could not find pytest report at {json_file}{Style.RESET_ALL}")
        sys.exit(1)

    all_test_results = []
    for test in test_data.get("tests", []):
        test_name = test.get("nodeid", "unknown_test").strip()
        sw_v2_result = test.get("outcome", "UNKNOWN").upper()
        sw_v1_result = previous_results.get(test_name, "UNKNOWN")
        error_message = ""

        if sw_v2_result == "FAILED":
            error_message = test.get("call", {}).get("longrepr", "No details")
        elif sw_v1_result != sw_v2_result:
            error_message = f"Mismatch: v1={sw_v1_result} vs v2={sw_v2_result}"

        write_to_csv(output_csv, job_number, timestamp, test_name, sw_v1_result, sw_v2_result, error_message)
        all_test_results.append({
            "test_name": test_name,
            "sw_v1_result": sw_v1_result,
            "sw_v2_result": sw_v2_result,
            "error_message": error_message
        })

    # Get selected/deselected counts from console
    selected = deselected = total = 0
    try:
        with open(console_log, "r") as log:
            log_data = log.read()
            total, selected, deselected = extract_counts_from_console(log_data)
    except:
        pass  # optional if log not saved

    summary = generate_summary(all_test_results)
    print_summary(summary, sw_version, job_number, selected, deselected)

    # Write to text file too
    with open("test_summary.txt", "w") as f:
        f.write(f"Test Summary - SW Version: {sw_version}, Build: {job_number}\n")
        f.write(f"Total: {summary['total']}, Passed: {summary['passed']}, Failed: {summary['failed']}, Unknown: {summary['unknown']}, Mismatches: {summary['mismatch']}\n")
        f.write(f"Selected: {selected}, Deselected: {deselected}, Pass Rate: {(summary['passed'] / summary['total']) * 100:.2f}%\n")

    print(f"{Fore.CYAN}Report saved to: {output_csv} and test_summary.txt{Style.RESET_ALL}")
