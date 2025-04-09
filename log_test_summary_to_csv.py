import json
import csv
import os
from datetime import datetime

# Load environment variable for build version
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

# Extract test summary
summary = data.get("summary", {})
total = summary.get("total", 0)
passed = summary.get("passed", 0)
failed = summary.get("failed", 0)
skipped = summary.get("skipped", 0)
expected = "Pass"
result = "Passed" if failed == 0 else "Failed"

# Collect remarks
remarks = ""
if "tests" in data:
    for test in data["tests"]:
        if test.get("outcome") == "failed":
            remarks += f"{test['nodeid']} failed. "

# Jenkins Environment Variable for Build Number
job_number = os.getenv("BUILD_NUMBER", "Unknown")
timestamp = datetime.now().strftime("%m/%d/%Y %H:%M")

# CSV log
csv_file = "build_results_log.csv"
file_exists = os.path.isfile(csv_file)

with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["Job #", "SW Version", "Result", "Expected", "Total", "Passed", "Failed", "Skipped", "Timestamp", "Remarks"])
    writer.writerow([f"#{job_number}", build_version, result, expected, total, passed, failed, skipped, timestamp, remarks])
