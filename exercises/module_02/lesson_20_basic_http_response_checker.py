"""
Module 2 - Lesson 20: Basic HTTP Response Checker
Date: 2026-11-26 | Tracker: JR-19

Write the implementation personally in the student code area.

Requirements:
1. Import requests and store https://example.com in a URL variable.
2. Display the title: Basic HTTP Response Checker
3. Send exactly one GET request per run, including timeout=10.
4. Store the returned Response Object in a variable.
5. Read its status_code attribute into another variable; do not hard-code it.
6. Display Target URL: <url> and HTTP Status Code: <actual status code>.

Use the existing .venv/Scripts/python.exe interpreter.
Wait for code review before running the program.
Use only the designated URL. Do not disable TLS verification or add
headers, body processing, JSON, scanning, extra requests, or credentials.
An HTTP 200 response does not prove that the whole website is secure.

After review: verify actual output, explain timeout, then predict output
before a safe title-only change and one further run if needed.
Do not intentionally create network failures.
"""

# STUDENT CODE AREA
import requests
url = "https://example.com"
print("Basic HTTP Response")
response = requests.get(url, timeout=10)
code = response.status_code
print(f"Target URL: {url}")
print(f"HTTP Status Code: {code}")
