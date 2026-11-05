"""
Module 2 - Lesson 15
PurrNest Inventory Summary File Writer
Date: 2026-11-05 | Tracker: JR-19

Write the implementation personally below.
Only major new concept: writing plain text to a file.

Create ONE products List with three Dictionaries (sku/name/price/stock):
PN001 / Cat Brush / 15.90 / 20
PN002 / Cat Bowl / 12.50 / 8
PN003 / Cat Toy / 8.90 / 15

Before writing, calculate:
- Product Count with len(products).
- Total Stock using an accumulator and direct List iteration.
- Total Inventory Value by accumulating each current price * stock.
Do not use sum().

Write to purrnest_inventory_summary.txt using with open and mode "w".
Inside the indented block use file.write() to produce these four lines:
PurrNest Inventory Summary
Product Count: 3
Total Stock: 43
Total Inventory Value: RM551.50
Counts/totals must come from calculated variables, not hard-coded results.
Use f-strings, two decimal places for money, and newline characters so
all four logical lines are separate. Write mode overwrites old contents.

After the with block print exactly: Inventory summary saved.
Do not substitute terminal output for a stored file.
Run from the repository root so the relative filename is created there.

FIRST STEP ONLY:
Write the products data and calculate the count, total stock, and total
inventory value. Do not add file writing yet. Wait for review.

Allowed: verified data structures, iteration, accumulators, arithmetic,
len, variables, strings, functions, parameters, return, f-strings, .2f,
and today's with open / write mode / file.write / newline pattern.
Do not introduce reading, read(), readline(), readlines(), append mode,
binary files, seek(), pathlib, os, CSV, JSON, exceptions, try/except,
modules, requests, HTTP, APIs, pandas, databases, or Streamlit.

Seven manual tests after pre-run review:
1. Verify output file did not exist, run, then verify it is created.
2. Manually open it and verify original four lines and formatting.
3. Confirm terminal message and explain terminal versus saved report.
4. Change PN002 stock to 10; predict stock/value BEFORE running, then
   verify updated content in the SAME file.
5. Manually replace file content with OLD REPORT, run again, verify it
   disappears and explain overwrite behavior.
6. Temporarily remove one newline, run, inspect joined text; restore it,
   rerun and explain why newline matters.
7. Design changes to all three records: decimal price, at least one stock
   zero, non-negative numbers. BEFORE running predict count, stock, value
   and exact four file lines; run and manually inspect stored content.

Do not write the finished exercise solution using AI.
"""

# STUDENT CODE AREA
products = [
    {"sku": "PN001", "name": "Cat Brush", "price": 15.90, "stock": 30},
    {"sku": "PN002", "name": "Cat Bowl",  "price": 13.50, "stock": 0},
    {"sku": "PN003", "name": "Cat Toy",   "price": 8.90,  "stock": 15}
]
product_count=len(products)
total_stock=0
total_inventory_value=0.0
for product in products:
    total_stock+=product["stock"]
    total_inventory_value+=product["price"]*product["stock"]
with open("purrnest_inventory_summary.txt","w") as file:
    file.write("PurrNest Inventory Summary\n")
    file.write(f"Product Count: {product_count}\n")
    file.write(f"Total Stock: {total_stock}\n")
    file.write(f"Total Inventory Value: RM{total_inventory_value:.2f}\n")
print("Inventory summary saved.")