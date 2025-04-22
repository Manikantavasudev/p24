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
                sw_v1_result = row.get("SWv Result 1.1", "").strip().upper()
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

def write_to_csv(file_path, job_number, timestamp, test_name, sw_v1_result, sw_v2_result, error_message, sw_version_v1, sw_version_v2):
    file_exists = os.path.exists(file_path)
    with open(file_path, "a", newline="") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "Job number from jenkins", "Date time", "Test case name",
                f"SW v1.1 ({sw_version_v1})", f"SW v1.2 ({sw_version_v2})", "Error Message (if any)"
            ])
        writer.writerow([
            job_number, timestamp, test_name,
            sw_v1_result, sw_v2_result, error_message
        ])

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
    console_log = "jenkins_console.log"

    # Extract current SW version from ReadMe.txt or fallback
    sw_version_v2 = "UNKNOWN"
    try:
        with open("ReadMe.txt", "r") as version_file:
            for line in version_file:
                if "Version" in line:
                    sw_version_v2 = line.split(":")[-1].strip()
                    break
    except:
        sw_version_v2 = os.getenv("SOFTWARE_VERSION", "3.210.1.20")

    # Define previous version manually or load dynamically if needed
    sw_version_v1 = "3.210.1.19"

    job_number = os.getenv("BUILD_NUMBER", "104")
    timestamp = datetime.now().strftime("%d:%m:%Y %I:%M:%S %p")

    previous_results = load_previous_results(previous_csv)

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

        write_to_csv(output_csv, job_number, timestamp, test_name, sw_v1_result, sw_v2_result, error_message, sw_version_v1, sw_version_v2)
        all_test_results.append({
            "test_name": test_name,
            "sw_v1_result": sw_v1_result,
            "sw_v2_result": sw_v2_result,
            "error_message": error_message
        })

    selected = deselected = total = 0
    try:
        with open(console_log, "r") as log:
            log_data = log.read()
            total, selected, deselected = extract_counts_from_console(log_data)
    except:
        pass

    summary = generate_summary(all_test_results)
    print_summary(summary, sw_version_v2, job_number, selected, deselected)

    with open("test_summary.txt", "w") as f:
        f.write(f"Test Summary - SW Version: {sw_version_v2}, Build: {job_number}\n")
        f.write(f"Total: {summary['total']}, Passed: {summary['passed']}, Failed: {summary['failed']}, Unknown: {summary['unknown']}, Mismatches: {summary['mismatch']}\n")
        f.write(f"Selected: {selected}, Deselected: {deselected}, Pass Rate: {(summary['passed'] / summary['total']) * 100:.2f}%\n")

    print(f"{Fore.CYAN}Report saved to: {output_csv} and test_summary.txt{Style.RESET_ALL}")
