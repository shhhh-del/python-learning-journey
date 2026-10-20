"""
Module 2 - Lesson 09
PurrNest Inventory Report Sections
Date: 2026-10-20 | Tracker: JR-19

Write the function definitions, calls, and business logic personally below.
Only new concept: basic no-parameter function definition and calling.

Define show_report_header with no parameters.
Its body displays exactly these three lines:
==============================
PurrNest Inventory Report
==============================

Define show_inventory_rules with no parameters.
Its body displays exactly these three lines:
Inventory Rules:
- Stock 0 is valid
- Price and stock must not be negative
These are informational messages only; do not add validation logic.

Use ONE products List containing three Dictionaries with these fields:
sku / name / price / stock
PN001 / Cat Brush / 15.90 / 20
PN002 / Cat Bowl  / 12.50 / 8
PN003 / Cat Toy   / 8.90  / 15

Main flow after defining both functions:
1. Call show_report_header.
2. Display Product Count: <len(products)>.
3. Directly iterate over products. For each current record display:
   SKU: <sku>
   Product Name: <name>
   Price: RMxx.xx
   Stock: <stock>
4. Accumulate total_stock and total_inventory_value (current price * stock).
   Initialize accumulators before the product loop.
5. After processing display:
   Total Stock: <total>
   Total Inventory Value: RMxx.xx
6. Call show_inventory_rules.
7. At the very end, call show_report_header again using the SAME definition.
Do not manually duplicate header output outside the function.
Original business results: count 3, stock 43, inventory value RM551.50.

First step: Write ONLY the two function definitions and their text bodies.
Do not add calls or business processing yet. Wait for Codex review.

Allowed: previously learned data structures, iteration, key reading, len,
counters/accumulators, arithmetic, if/else, print, f-strings, .2f.
Do not introduce parameters, arguments, return, scope theory, lambda,
type hints, recursion, classes, tuples, sets, CSV, JSON, file handling,
exceptions, modules, requests, HTTP, APIs, pandas, databases, or Streamlit.

Manual tests (Codex will guide each test after code review):
1. Definition only: no header call; verify definition does not print header.
2. One header call: three header lines appear once.
3. Two header calls: same body executes twice without duplicate print code.
4. Rules function: verify full text appears only when called.
5. Original business data: count 3 / stock 43 / RM551.50.
6. Design a call order using header, rules, and one normal print statement.
   Predict exact complete output BEFORE running, then compare actual output.
"""

# STUDENT CODE AREA
def show_report_header():
      print("==============================")
      print("PurrNest Inventory Report")
      print("==============================")
def show_inventory_rules():
      print("Inventory Rules:")
      print("- Stock 0 is valid")
      print("- Price and stock must not be negative")
products=[
      {"sku": "PN001", "name": "Cat Brush", "price": 15.90, "stock": 20},
      {"sku": "PN002", "name": "Cat Bowl",  "price": 12.50, "stock": 8},
      {"sku": "PN003", "name": "Cat Toy",   "price": 8.90,  "stock": 15}
]
show_report_header()
print(f"Product Count: {len(products)}")
total_stock = 0
total_inventory_value = 0.0
for product in products:
      print(f"SKU: {product['sku']}")
      print(f"Product Name: {product['name']}")
      print(f"Price: RM{product['price']:.2f}")
      print(f"Stock: {product['stock']}")
      total_stock += product['stock']
      total_inventory_value += product['price'] * product['stock']
print(f"Total Stock: {total_stock}")
print(f"Total Inventory Value: RM{total_inventory_value:.2f}")
show_inventory_rules()
show_report_header()

