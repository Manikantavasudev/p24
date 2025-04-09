import json
import csv
import os
from datetime import datetime

json_file = "pytest-report.json"
csv_file = "build_results_log.csv"
job_number = os.getenv("BUILD_NUMBER", "#Unknown")
sw_version = os.getenv("BUILD_VERSION", "Unknown")

# Check if the JSON report exists
if not os.path.exists(json_file):
    print(f"Error: {json_file} not found.")
    exit(1)

# Load test result JSON
with open(json_file, "r") as f:
    data = json.load(f)

summary = data.get("summary", {})
tests = data.get("tests", [])

# Extract test counts
total = summary.get("collected", 0)
passed = summary.get("passed", 0)
failed = summary.get("failed", 0)
skipped = summary.get("skipped", 0)

# Determine result
result = "Passed" if failed == 0 else "Failed"
expected = "Pass"

# Capture failed test names
failed_tests = [t["nodeid"] for t in tests if t["outcome"] == "failed"]
remarks = ", ".join(failed_tests) if failed_tests else "All Passed"

# Timestamp
timestamp = datetime.now().strftime("%-m/%-d/%Y %H:%M")

# Write to CSV
file_exists = os.path.exists(csv_file)
with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(["Job #", "SW Version", "Result", "Expected", "Total", "Passed", "Failed", "Skipped", "Timestamp", "Remarks"])
    writer.writerow([f"#{job_number}", sw_version, result, expected, total, passed, failed, skipped, timestamp, remarks])
