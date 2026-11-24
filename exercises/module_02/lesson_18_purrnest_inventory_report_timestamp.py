"""
Module 2 - Lesson 18
PurrNest Inventory Report Timestamp
Date: 2026-11-24 | Tracker: JR-19

Write the implementation personally below.
Only major new concept: basic modules/imports using the datetime standard library.

Requirements:
- Near the top of executable code, write import datetime yourself.
- Call datetime.date.today() and store the returned date in a variable.
- Do not hard-code a report date; use default date display, no strftime.
- Store safe business summary values in variables:
  product count 3, total stock 43, inventory value 551.50.
- Display these five logical lines in the terminal:
  PurrNest Inventory Report
  Report Date: <date from module>
  Product Count: 3
  Total Stock: 43
  Total Inventory Value: RM551.50
- Using with open in mode w, write the SAME five lines to:
  purrnest_inventory_timestamped_report.txt
- Use newlines and .2f currency formatting.
- After writing display exactly: Timestamped inventory report saved.
Run from repository root so the generated file is located there.

FIRST STEP ONLY:
Write import, obtain date, save date in a variable, and print the variable.
Do not write the full report/file integration yet; wait for review.

Only import datetime. Do not use from-import, aliases, custom modules,
multiple Python files for imports, pip, virtual environments, third-party
packages, requests, HTTP, APIs, JSON, CSV, regex, command-line arguments,
pathlib, os, classes, or date formatting methods.

Seven manual tests after pre-run review:
1. Import and today call work without import error.
2. Returned date stored in a variable and printed.
3. Source review: date not hard-coded.
4. Original five-line terminal report and confirmation correct.
5. Manually open generated report; same date and values as terminal.
6. Predict behavior if import is commented while module name is still
   used. Test only after guidance; restore import afterward.
7. Choose new safe count/stock/value. BEFORE running predict five report
   lines; keep date dynamic. Run and verify terminal and stored file.
No secrets/private data.

Do not start Lesson 19.
"""

# STUDENT CODE AREA
import datetime
report_date= datetime.date.today()

product_count = 4
total_stock = 44
inventory_value = 651.50
print(f"PurrNest Inventory Report")
print(f"Report Date: {report_date}")
print(f"Product Count: {product_count}")
print(f"Total Stock: {total_stock}")
print(f"Total Inventory Value: RM{inventory_value:.2f}")
with open("purrnest_inventory_timestamped_report.txt", "w")as file:
    file.write(f"PurrNest Inventory Report\n")
    file.write(f"Report Date: {report_date}\n")
    file.write(f"Product Count: {product_count}\n")
    file.write(f"Total Stock: {total_stock}\n")
    file.write(f"Total Inventory Value: RM{inventory_value:.2f}\n")
print("Timestamped inventory report saved.")
