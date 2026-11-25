"""
Module 2 - Lesson 19
PurrNest Python Environment Verification
Date: 2026-11-25 | Tracker: JR-19

Write the small verification program personally below.

Requirements:
1. Import datetime.
2. Import requests.
3. Obtain today's date dynamically using datetime.date.today(), storing
   it in a variable. Do not hard-code the date.
4. Display exactly:
   PurrNest Python Environment Verification
   Verification Date: <dynamic date>
   Requests package imported successfully.
5. The success message may run only after the imports have succeeded.

Run using the verified project .venv interpreter. PowerShell activation
was blocked by script execution policy; use the environment's python.exe
explicitly, without changing system execution policy.
Do not use requests.get(), requests.post(), or any HTTP request.
No JSON, CSV, API processing, requirements file, or other new concepts.
Do not commit .venv or installed package files.

After code review:
- Personally run the program with the explicit .venv Python.
- Design a title/text change and predict output BEFORE running.
- Verify environment reuse with the same explicit interpreter, without
  reinstalling packages. Activation/deactivation were not completed;
  document this limitation rather than claiming them successful.

Do not start Lesson 20.
"""

# STUDENT CODE AREA
import datetime
import requests
today_date = datetime.date.today()
print("PurrNest Python Verification")
print(f"Verification Date: {today_date}")
print("Requests package imported successfully.")
