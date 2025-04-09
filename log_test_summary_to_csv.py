import json
import csv
import os
from datetime import datetime

# Jenkins environment variables
job_num = os.getenv("BUILD_NUMBER", "NA")
sw_version = "Unknown"
build_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Extract Software Version from version.properties
try:
    with open("version.properties", "r") as f:
        for line in f:
            if line.startswith("BUILD_VERSION="):
                sw_version = line.strip().split("=")[1]
except:
    pass

# Load pytest results
pytest_report = "pytest-report.json"
total = passed = failed = skipped = 0
status = "Unknown"

if os.path.exists(pytest_report):
    with open(pytest_report, "r") as f:
        data = json.load(f)
        summary = data.get("summary", {})
        total = summary.get("total", 0)
        passed = summary.get("passed", 0)
        failed = summary.get("failed", 0)
        skipped = summary.get("skipped", 0)
        status = "Passed" if failed == 0 else "Failed"

# Prepare CSV line
csv_file = "build_results_log.csv"
header = ["Job #", "SW Version", "Result", "Expected", "Total", "Passed", "Failed", "Skipped", "Timestamp"]
row = [f"#{job_num}", sw_version, status, "Pass", total, passed, failed, skipped, build_time]

# Write or append
file_exists = os.path.exists(csv_file)
with open(csv_file, "a", newline="") as f:
    writer = csv.writer(f)
    if not file_exists:
        writer.writerow(header)
    writer.writerow(row)

print(f"Test results logged to: {csv_file}")
