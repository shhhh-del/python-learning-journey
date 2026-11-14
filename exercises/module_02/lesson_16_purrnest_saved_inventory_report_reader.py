"""
Module 2 - Lesson 16
PurrNest Saved Inventory Report Reader
Lesson continued on 2026-11-15 | Tracker: JR-19

Write the implementation personally below.
Only major new concept: reading an entire text file in mode r.

Use the EXISTING report at repository root:
purrnest_inventory_summary.txt
Current baseline content:
PurrNest Inventory Summary
Product Count: 3
Total Stock: 45
Total Inventory Value: RM610.50

Requirements:
1. Display exactly: PurrNest Saved Inventory Report Reader
2. Open the named existing file in READ mode using with open.
3. Inside the indented block read the entire file using file.read().
4. Store the returned String in a variable you choose.
5. After the with block display exactly: Saved Report:
6. Print the variable containing the loaded text.
Do not hard-code the report content in output statements or recalculate it.
Do not create/write the report from this reader.
Run from repository root so the relative filename locates the existing file.

FIRST STEP:
Write the reader above. Wait for Codex review before running.
The optional header search is omitted to keep this lesson focused on the
single new concept of reading; String membership is not yet verified.

Allowed: variables, strings, print, with open, file objects, filenames,
functions, parameters, return, strip, lower, if/else, len, and today's
read mode and file.read pattern.
Do not introduce readline, readlines, iteration over file lines, append
mode, exceptions/try/except, missing-file handling, pathlib, os, CSV, JSON,
modules/imports, requests, HTTP, APIs, regex, pandas, databases, or Streamlit.
The file must exist; ask for guidance if it cannot be found.

Seven manual tests after pre-run review:
1. Verify report exists, run reader, verify no write operation in source.
2. Verify complete file content displayed, explain it came from file.read.
3. Note file content before run, manually inspect afterward, verify unchanged;
   explain read versus write mode.
4. Manually change one line to Total Stock: 99; run unchanged reader and
   verify changed text appears automatically.
5. Verify multiple file lines loaded together in ONE String; explain that
   a String can contain newline characters.
6. Verify receiving variable is printed after with closes the file; explain
   that already-loaded text remains in the variable.
7. Manually choose new safe file content with at least four lines and one
   RM amount, no secrets/private data. Predict exact displayed report BEFORE
   running, then compare actual reader output.

Do not start Lesson 17.
"""

# STUDENT CODE AREA
print("PurrNest Saved Inventory Report Reader")

with open("purrnest_inventory_summary.txt", "r") as file:
    report_content = file.read()

print("Saved Report:")
print(report_content)