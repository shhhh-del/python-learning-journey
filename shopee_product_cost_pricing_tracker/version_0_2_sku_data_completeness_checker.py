"""
PurrNest Shopee Product Cost and Pricing Tracker
Version 0.2 - SKU Data Completeness Checker

Use simulated data only. Write the implementation personally below.

Business objective:
Check each product for all four required keys: sku, price, cost, stock.
Check key presence only; stock 0 is valid when all keys exist.

Create one products List with these records:
1. sku CAT001, price 15.0, cost 6.0, stock 10
2. sku CAT002, price 12.0, stock 5 (cost intentionally missing)
3. sku CAT003, price 18.0, cost 8.0, stock 0
4. sku CAT004, price 9.0, cost 4.0 (stock intentionally missing)

Required original output:
SKU Data Completeness Report
CAT001: COMPLETE
CAT002: INCOMPLETE
CAT003: COMPLETE
CAT004: INCOMPLETE
Total Products: 4
Complete Records: 2
Incomplete Records: 2

Requirements:
- Use direct List iteration and Dictionary key membership.
- All four required keys must exist for COMPLETE.
- Produce exactly one status per record.
- If sku is absent, safely display UNKNOWN SKU as the label.
- Do not read a possibly missing key before checking its presence.
- Initialize counters before processing; display totals after processing.
- Total Products must equal Complete Records plus Incomplete Records.

Scope:
Do not calculate profits or inventory value, edit prices, or add data-type
or negative-number validation. Do not use functions, CSV, JSON, file I/O,
sets, tuples, APIs, databases, Streamlit, or other unverified concepts.
Do not modify Version 0.1 or the Profit Calculator.

First step:
Write the products List and a loop that checks whether all four keys exist.
For now, display only COMPLETE or INCOMPLETE for each record.
Wait for review before adding SKU labels and counters.

Required manual tests after code review:
1. Original four records: total 4 / complete 2 / incomplete 2.
2. One complete record: total 1 / complete 1 / incomplete 0.
3. Missing cost: INCOMPLETE, no KeyError.
4. Complete record with stock 0: COMPLETE.
5. Empty products List: all counts 0, no error.
6. Missing sku: INCOMPLETE, safe UNKNOWN SKU label, no KeyError.
"""

# STUDENT CODE AREA
products = [
    {"price": 15.0, "cost": 6.0, "stock": 10}
    
]
complete_count = 0
incomplete_count = 0
print("SKU Data Completeness Report")
for product in products:
    if "sku" in product:    
        sku_label = product["sku"]
    else:
        sku_label = "UNKNOWN SKU"

    if "sku" in product and "price" in product and "cost" in product and "stock" in product:
        complete_count += 1
        print(f"{sku_label}: COMPLETE")
    else:
        incomplete_count += 1
        print(f"{sku_label}: INCOMPLETE")

print(f"Total Products: {len(products)}")
print(f"Complete Records: {complete_count}")
print(f"Incomplete Records: {incomplete_count}")
