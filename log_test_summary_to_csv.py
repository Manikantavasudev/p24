import json
import csv
import os
from datetime import datetime

# Load software version from version.properties
version_file = "version.properties"
build_version = "Unknown"
if os.path.exists(version_file):
    with open(version_file) as f:
        for line in f:
            if line.startswith("BUILD_VERSION="):
                build_version = line.strip().split("=")[1]

# Load pytest JSON report
json_file = "pytest-report.json"
with open(json_file, "r") as f:
    data = json.load(f)

# Extract summary
summary = data.get("summary", {})
total = summary.get("total", 0)
passed = summary.get("passed", 0)
failed = summary.get("failed", 0)
skipped = summary.get("skipped", 0)
expected = "Pass"
result = "Passed" if failed == 0 else "Failed"

# Gather remarks from failed tests
remarks = ""
if "tests" in data:
    for test in data["tests"]:
        if test.get("outcome") == "failed":
            nodeid = test.get("nodeid", "unknown_test")
            msg = test.get("call", {}).get("longrepr", "No details")
            remarks += f"{nodeid} failed. "

if not remarks:
    remarks = "All tests passed."

# Jenkins build number and timestamp
job_number = os.getenv("BUILD_NUMBER", "Unknown")
timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")

# Output CSV
csv_file = "build_results_log.csv"
file_exists = os.path.exists(csv_file)

with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow([ "SW Version", "Result", "Expected", "Total", "Passed", "Failed", "Skipped", "Timestamp", "Remarks"])
    writer.writerow([build_version, result, expected, total, passed, failed, skipped, timestamp, remarks])
