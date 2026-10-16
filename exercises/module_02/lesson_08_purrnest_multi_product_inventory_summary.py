"""
Module 2 - Lesson 08
PurrNest Multi-Product Inventory Summary

Business problem:
Process three product records together and summarize stock and inventory value.
Write all implementation personally in the STUDENT CODE AREA.

Requirements:
1. Display exactly: PurrNest Multi-Product Inventory Summary
2. Create ONE List named products containing exactly THREE Dictionaries.
   Each Dictionary represents one product with sku, name, price, stock.
   Original data:
   PN001 / Cat Brush / price 15.90 / stock 20
   PN002 / Cat Bowl  / price 12.50 / stock 8
   PN003 / Cat Toy   / price 8.90  / stock 15
   Do not use three unrelated standalone variables as the main structure.
3. Use direct List iteration to process one product Dictionary at a time.
   For every current record display exactly:
   SKU: <sku>
   Product Name: <name>
   Price: RMxx.xx
   Stock: <stock>
   Read all displayed values from the CURRENT Dictionary by key.
4. Initialize total_stock and total_inventory_value before processing.
   During iteration, add current stock to total_stock.
   Calculate each product's inventory value as its price multiplied by stock;
   accumulate these values into total_inventory_value.
   Do not create a second List for inventory values.
5. After all records are processed, display exactly:
   Product Count: <count from len(products)>
   Total Stock: <total>
   Total Inventory Value: RMxx.xx
   Original expected summary: 3 products / stock 43 / RM551.50.

You determine the List/Dictionary syntax, record placement, loop syntax,
current-record field access, accumulator initial values and updates,
calculation placement, formatting, and final output placement.

Allowed: Lists, Dictionary literals, key-based reads, direct List iteration,
accumulators, arithmetic/multiplication, if, f-strings, .2f, len(), print().
Only major new concept: List of Dictionaries.
Do not use nested Dictionaries (Dictionary inside Dictionary), items(), keys(),
values(), get(), tuples, sets, functions, classes, CSV, JSON, file handling,
exceptions, modules, requests, HTTP, APIs, pandas, databases, or Streamlit.
Do not add user-input record creation; use fixed records.

Manual tests (wait for Codex's code review before running):
1. Original data: Product Count 3 / Total Stock 43 / value RM551.50.
2. Change only PN002 stock to 10. Predict all three summary values BEFORE
   running; compare prediction with actual output.
3. Change PN003 price to 10.00. Confirm the exact test data with Codex and
   predict BEFORE running; keep iteration logic unchanged.
4. Set PN001 stock to 0. It remains a record, product count stays 3,
   and its inventory value is RM0.00. Confirm other records for this test.
5. Temporary records: A / price 5.00 / stock 2;
   B / price 10.00 / stock 3; C / price 20.00 / stock 1.
   Keep name fields too. BEFORE running, trace each current Dictionary,
   SKU, price, stock, and individual inventory value.
6. Design three records, changing values while retaining sku/name/price/stock.
   One product must have stock 0; at least one decimal price; all stocks
   non-negative. BEFORE running, supply the records and predict count,
   processing order, total stock, and total inventory value.
During tests change data only, keeping the core logic unchanged.
"""

# STUDENT CODE AREA
print("PurrNest Multi-Product Inventory Summary")
products=[
    {"sku":"A","name":"Cat Brush","price":5.00,"stock":0},
    {"sku":"B","name":"Cat Bowl","price":10.50,"stock":3},
    {"sku":"C","name":"Cat Toy","price":20.00,"stock":1}
]
for product in products:
    print(f"SKU: {product['sku']}")
    print(f"Product Name: {product['name']}")
    print(f"Price: RM{product['price']:.2f}")
    print(f"Stock: {product['stock']}")
total_stock=0
total_inventory_value=0.0
for product in products:
    total_stock+=product['stock']
    total_inventory_value+=product['price']*product['stock']
print(f"Product Count: {len(products)}")
print(f"Total Stock: {total_stock}")   
print(f"Total Inventory Value: RM{total_inventory_value:.2f}")