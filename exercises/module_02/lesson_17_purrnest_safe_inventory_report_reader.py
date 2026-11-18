"""
Module 2 - Lesson 17
PurrNest Safe Inventory Report Reader
Date: 2026-11-18 | Tracker: JR-19

Write the implementation personally below.
Only major new concept: try / except for FileNotFoundError.

Display exactly: PurrNest Safe Inventory Report Reader

Inside try:
- Open existing purrnest_inventory_summary.txt in read mode using with.
- Read entire text with file.read() and store returned String in a variable.
- After reading display Saved Report: and the loaded String.
- Display Report read successfully. ONLY after successful report display.

Use exactly one handler: except FileNotFoundError.
When the file cannot be found display exactly: Report file not found.
Do not display success after failure. Do not create a missing file,
use write mode, fabricate report content, or silently ignore the problem.
You determine try/except placement, indentation, variable and output order.
Run from repository root so the relative filename finds the report.

Allowed: previously learned with open, r, file.read, variables, strings,
print, functions, return, if/else and basic string processing.
Do not use bare except, except Exception, multiple handlers, try/else,
finally, raise, custom exceptions, traceback handling, logging, CSV, JSON,
modules/imports, pip, virtual environments, requests, HTTP, APIs, regex,
classes, pandas, databases or Streamlit.

Seven manual tests after code review:
1. Existing file: report and success message, no missing-file message.
2. Temporarily rename report, run: missing-file message, no success or
   unhandled FileNotFoundError; preserve original file for restoration.
3. Restore filename, run: success again.
4. Manually modify safe report text, run: new content appears with unchanged
   reader logic.
5. Temporarily request a nonexistent filename in code: predict BEFORE
   running, verify handler, then restore correct filename.
6. Conceptual check: a separate undefined-variable error is not handled by
   FileNotFoundError. Do not add a broad handler.
7. Choose existing safe file or deliberately missing filename. BEFORE
   running predict try outcome, exception occurrence and exact relevant
   output path; then compare actual result. No secrets/private data.

Do not start Lesson 18.
"""

# STUDENT CODE AREA
print("PurrNest Safe Inventory Report Reader")
try:
    with open("purrnest_inventory_summary.txt", "r") as file:
        report_content = file.read()
    print("Saved Report:")
    print(report_content)
    print("Report read successfully.")
except FileNotFoundError:
      print("Report file not found.")