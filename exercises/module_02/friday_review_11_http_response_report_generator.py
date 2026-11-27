"""
Friday Review #11 - HTTP Response Report Generator
2026-11-27 | JR-19 | Review only; Lesson 21 not started

Write all core logic personally below. Use only previously verified concepts.

Requirements:
- Import datetime and requests only.
- Define get_http_status with exactly one parameter, url.
  Send one GET with timeout=10, store the Response Object, and return
  its actual status_code. This function does not print or write reports.
- Display: HTTP Response Report Generator
- Read root-level target_url.txt in r mode with file.read().
  Scope try/except FileNotFoundError to configuration reading.
  If missing, print: Target configuration file not found.
- Strip surrounding whitespace; do not lowercase the URL.
  Accept only exactly https://example.com.
  Reject empty or different text with:
  Invalid or unauthorized demonstration URL.
- Missing/rejected configuration must cause NO request, NO report
  creation/overwrite, and NO saved confirmation. Use known variables and
  if/else to control the next stage; no try-else or exit commands.
- Only after successful reading and validation, call the function,
  receive its returned status code, and obtain datetime.date.today().
- Write root-level http_response_report.txt using w mode, five lines:
  HTTP Response Report
  Report Date: <dynamic date>
  Target URL: <normalized URL>
  HTTP Status Code: <actual returned status>
  This status code alone does not establish website security.
- After successful writing only, print: HTTP response report saved.

No new imports, network exception handling, broad except, headers,
body processing, JSON, credentials, scanning, or TLS verification changes.
No extra HTTP requests while writing. Keep existing lessons unchanged.
Run from repository root using the existing .venv interpreter.
Wait for code review before execution.

Manual tests after review:
1. Environment/import verification.
2. Successful approved URL; inspect the real report.
3. Missing configuration: predict before running, preserve old report.
4. Empty configuration: reject, preserve old report.
5. not-an-approved-url: reject, preserve old report.
6. Student-designed surrounding whitespace: predict before execution.
7. Replace OLD REPORT using w mode; explain overwrite behavior.
Combine compatible successful tests to avoid unnecessary requests.
Restore safe fixture contents after testing.
"""

# STUDENT CODE AREA
import datetime
import requests

def get_http_status(url):
    response = requests.get(url, timeout=10)
    return response.status_code
print("HTTP Response Report Generator")
file_load = False
try:
    with open("target_url.txt", "r") as file:
        url = file.read().strip()
        file_load = True
except FileNotFoundError:
    print("Target configuration file not found.")
if file_load:
    if url == "https://example.com":
        status_code = get_http_status(url)
        report_date = datetime.date.today()
        with open("http_response_report.txt", "w") as report_file:
            report_file.write("HTTP Response Report\n")
            report_file.write(f"Report Date: {report_date}\n")
            report_file.write(f"Target URL: {url}\n")
            report_file.write(f"HTTP Status Code: {status_code}\n")
            report_file.write("This status code alone does not establish website security.\n")
        print("HTTP response report saved.")
    else:
        print("Invalid or unauthorized demonstration URL.")