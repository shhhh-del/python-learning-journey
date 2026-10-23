"""
Friday Review #9 - PurrNest Inventory Valuation Audit
Date: 2026-10-23 | Tracker: JR-19
Initial closed-book knowledge score: 9 / 12 (preserve original score).

Write the implementation personally in the STUDENT CODE AREA.
No new syntax. Do not copy the previous exercise solution.

Create ONE products List containing FOUR Dictionary records:
sku / name / price / stock
PN001 / Cat Brush / 15.90 / 20
PN002 / Cat Bowl / 12.50 / 8
PN003 / Cat Toy / NO price key / 15
PN004 / Cat Comb / 10.00 / 0
PN003 intentionally lacks price; do not add it to the original test data.

Function requirements:
Define calculate_inventory_value with exactly ONE parameter representing
one complete product Dictionary. Calculate current price * stock and RETURN
the number. Do not print the result inside the function.

Main program:
Display exactly: PurrNest Inventory Valuation Audit
Initialize complete_count, incomplete_count, total_inventory_value before
processing. Directly iterate through products.
Check that all four keys sku/name/price/stock exist in the current record.
Use previously learned membership and logic; no nested loops.

For each COMPLETE record:
SKU: <sku>
Record Status: COMPLETE
Increase complete_count. Call the calculation function with the current
Dictionary, store its returned value in a variable, display:
Inventory Value: RMxx.xx
Add that same returned variable to total_inventory_value.
Do not duplicate price * stock calculation in the caller.

For each INCOMPLETE record:
Display SKU: <sku> only if sku exists, then:
Record Status: INCOMPLETE
Increase incomplete_count. Do not call the calculation function or read
missing fields. Incomplete records contribute nothing to the value total.

Business rule: stock 0 is valid, not a missing key. A complete zero-stock
record must reach the calculation function and produce RM0.00.

After processing display exactly:
Product Records: <len(products)>
Complete Records: <count>
Incomplete Records: <count>
Total Inventory Value: RMxx.xx
Original summary: 4 / 3 / 1 / RM418.00.

You personally determine the function definition, calculation and return,
membership condition, loop, receiving variable, counters and accumulator,
safe access placement, formatting, and final output placement.
Do not use multiple/default parameters, keyword arguments, advanced scope,
global, tuples, sets, nested loops, get(), items(), keys(), values(), CSV,
JSON, files, exceptions, modules, requests, HTTP, APIs, classes, pandas,
databases, or Streamlit.

Six manual tests (wait for pre-run code review):
1. Original data: count 4 / complete 3 / incomplete 1 / RM418.00.
2. Add PN003 price 8.90. BEFORE running predict both counters, PN003 value,
   and total, then compare actual output.
3. Remove PN002 stock. Agree remaining dataset before running. Verify no
   function call for that record, no crash, and no contribution.
4. Verify PN004 stock 0 is COMPLETE, function is called, and value is 0.00.
5. For a complete record, verify the SAME returned variable is printed and
   accumulated; no duplicate multiplication in main loop.
6. Design four modified records: at least one incomplete, one complete,
   one complete with stock 0, and at least one decimal price. BEFORE
   execution predict record count, both counters, each complete record's
   value and total. Compare actual output with prediction.

Do not start Lesson 12.
"""

# STUDENT CODE AREA
products= [
      {"sku": "PN001", "name": "Cat Brush", "price": 15.90},
      {"sku": "PN002", "name": "Cat Bowl",  "price": 12.50, "stock": 8},
      {"sku": "PN003", "name": "Cat Toy",   "price": 8.90, "stock": 15}, 
      {"sku": "PN004", "name": "Cat Comb",  "price": 10.00, "stock": 0}
]
def calculate_inventory_value(product):
    inventory_value=product["price"]*product["stock"]
    return inventory_value
print("PurrNest Inventory Valuation Audit")
complete_count=0
incomplete_count=0
total_inventory_value=0

for product in products:
    if "sku" in product and "name" in product and "price" in product and "stock" in product:
        print(f"SKU: {product['sku']}")
        print("Record Status: COMPLETE")
        complete_count+=1
        inventory_value=calculate_inventory_value(product)
        print(f"Inventory Value: RM{inventory_value:.2f}")
        total_inventory_value+=inventory_value
    elif "sku" in product:
        print(f"SKU: {product['sku']}")
        print("Record Status: INCOMPLETE")
        incomplete_count+=1
    else:
        print("Record Status: INCOMPLETE")
        incomplete_count+=1

print(f"Product Records: {len(products)}")
print(f"Complete Records: {complete_count}")
print(f"Incomplete Records: {incomplete_count}")
print(f"Total Inventory Value: RM{total_inventory_value:.2f}")
