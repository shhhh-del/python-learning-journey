"""
Friday Review #8 - PurrNest Multi-Product Inventory Audit
Date: 2026-10-16 | Tracker: JR-19

Write the implementation personally in the STUDENT CODE AREA.
No new Python concepts are needed. Do not copy the previous solution.

Business rule:
A complete product record contains all four keys: sku, name, price, stock.
A missing key differs from a present key whose value is zero.
Incomplete records contribute nothing to inventory totals.

Original data: ONE List named products containing FOUR Dictionary records:
1. sku PN001, name Cat Brush, price 15.90, stock 20
2. sku PN002, name Cat Bowl, price 12.50, stock 8
3. sku PN003, name Cat Toy, price 8.90; NO stock key (intentional)
4. sku PN004, name Cat Comb, price 10.00, stock 0

Display title exactly:
PurrNest Multi-Product Inventory Audit

Initialize before processing:
complete_count, incomplete_count, total_stock, total_inventory_value.

Use direct List iteration over the current product record.
Check that ALL four required keys exist using membership and known logic.
Do not use nested loops.

For each COMPLETE record display exactly:
SKU: <current sku>
Record Status: COMPLETE
Increase the complete counter.
Safely read current stock and price, accumulate stock and price * stock.

For each INCOMPLETE record display exactly:
Record Status: INCOMPLETE
Increase the incomplete counter.
Do not read missing fields or include incomplete records in either total.

After processing display exactly:
Product Records: <len(products)>
Complete Records: <count>
Incomplete Records: <count>
Total Stock: <total>
Total Inventory Value: RMxx.xx

Original expected summary: 4 / 3 / 1 / 28 / RM418.00.
You determine the condition, structure, safe-read placement, increments,
initial values, calculations, and output placement.

Allowed: already learned List/Dictionary syntax, direct iteration, len(),
key access, in, if/else, and, counters, accumulators, arithmetic,
print(), f-strings, .2f.
Do not introduce nested loops, items(), keys(), values(), get(), tuples,
sets, functions, classes, CSV, JSON, files, exceptions, modules, requests,
HTTP, APIs, pandas, databases, or Streamlit.

Manual tests: wait for Codex's pre-run review.
1. Original data -> records 4, complete 3, incomplete 1, stock 28, RM418.00.
2. Add stock 15 to PN003. Predict counters and totals BEFORE running.
3. Remove only PN002 price. Agree exact remaining data before running;
   verify incomplete status, no crash, and no contribution from PN002.
4. Verify PN004 stock 0 is COMPLETE; explain zero versus absent key.
5. Test one record containing sku/name/stock but no price; verify safe
   incomplete handling without reading the absent price.
6. Design four modified records: at least one incomplete, at least one
   complete with stock 0, at least one decimal price, all existing numeric
   values non-negative. BEFORE running, provide data and predict all five
   summary results. Then compare actual output with your prediction.

Do not change the core logic just to match a test's expected output.
"""

# STUDENT CODE AREA
products=[
    {"sku" : "PN001","name" : "Cat Brush","price" : 15.80,"stock" : 20},
    {"sku" : "PN002","name" : "Cat Bowl","stock" : 5},
    {"sku" : "PN003","name" : "Cat Toy","price" : 8.90,"stock" : 12},
    {"sku" : "PN004","name" : "Cat Comb","price" : 10.00,"stock" : 0}
]
print("PurrNest Multi-Product Inventory Audit")
complete_count = 0
incomplete_count = 0
total_stock = 0
total_inventory_value = 0.0

for product in products:
    if "sku" in product and "name" in product and "price" in product and "stock" in product:
        print("SKU:",product["sku"])
        print("Record Status: COMPLETE")
        complete_count+=1
        total_stock+=product["stock"]
        total_inventory_value+=product["price"]*product["stock"]
    else:
        print("Record Status: INCOMPLETE")
        incomplete_count+=1

print("Product Records:",len(products))
print("Complete Records:",complete_count)
print("Incomplete Records:",incomplete_count)
print("Total Stock:",total_stock)
print(f"Total Inventory Value: RM{total_inventory_value:.2f}")