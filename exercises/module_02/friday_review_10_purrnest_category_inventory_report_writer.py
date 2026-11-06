"""
Friday Review #10 - PurrNest Category Inventory Report Writer
Date: 2026-11-06 | Tracker: JR-19
Initial closed-book knowledge score: 11 / 12. Preserve original score.

Write core implementation personally below. No new syntax today.

Create ONE List of Dictionaries named products with fields:
sku / name / category / price / stock
PN001 / Cat Brush Basic / brush / 15.90 / 20
PN002 / Cat Bowl / bowl / 12.50 / 8
PN003 / Cat Toy Ball / toy / 8.90 / 15
PN004 / Cat Brush Premium / brush / 20.00 / 5

Independently write two functions:
1. normalize_category: ONE parameter category; create local normalized text
   using strip() and lower(), then return it. No print inside function.
2. calculate_inventory_value: TWO parameters price, stock, in that order;
   create local price * stock result, then return it. No internal print.

Main program:
- Display exactly: PurrNest Category Inventory Report Writer
- Ask: Enter Product Category:
- Store raw input, normalize with your function and store returned text.
- Accept only brush, bowl, toy using previously verified comparisons.
- Invalid input: display Invalid Category and request FRESH input;
  normalize each retry. Continue until valid; do not hard-code acceptance.
- Initialize matching_count, total_stock, total_inventory_value.
- Directly iterate over products. Only for records whose category matches
  the normalized user choice: increment count, accumulate stock, call the
  calculation function with current price and stock as separate positional
  arguments, receive its result, and accumulate that returned value.
- Do not duplicate price * stock in the caller.

Write purrnest_category_inventory_report.txt using with open and mode w.
Inside the block use file.write to produce exactly five logical lines:
PurrNest Category Inventory Report
Category: <normalized category>
Matching Products: <count>
Total Stock: <total>
Total Inventory Value: RMxx.xx
Use calculated values and newline characters; money uses .2f.
After the with block display exactly: Category inventory report saved.
The actual report must be stored in the file, not just printed.
Run from repository root to locate the output there.

Original expected results:
brush: matching 2 / stock 25 / value RM418.00
bowl: matching 1 / stock 8 / value RM100.00
toy: matching 1 / stock 15 / value RM133.50

Use only verified concepts. Do not introduce file reading, append mode,
exceptions, try/except, CSV, JSON, modules/imports, requests, HTTP, APIs,
items(), get(), tuples, sets, classes, pathlib, os, pandas, databases,
or Streamlit. Do not start Lesson 16.

Seven manual tests after pre-run review:
1. brush: manually open generated report and verify original brush values.
2. Surrounding spaces and BrUsH: same normalized brush report.
3. BOWL: original bowl report.
4. toy: original toy report.
5. food rejected, then surrounding spaces and ToY accepted; normal exit.
6. Manually put OLD REPORT in output, run again, verify overwritten and
   explain why.
7. Design changes to four records, categories within brush/bowl/toy, at
   least one zero stock, decimal price, non-negative numbers. Choose input
   with mixed case or surrounding spaces. BEFORE running predict normalized
   category, count, stock, each matching value, total and exact five report
   lines. Run and manually inspect generated file; compare with prediction.

Do not obtain a completed solution from AI. Ask for hints after attempting.
"""

# STUDENT CODE AREA
products =[
    {"sku": "PN001", "name": "Cat Brush Basic", "category": "brush", "price": 15.80, "stock": 20},
    {"sku": "PN002", "name": "Cat Bowl",        "category": "bowl",  "price": 12.60, "stock": 0},
    {"sku": "PN003", "name": "Cat Toy Ball",    "category": "toy",   "price": 7.90,  "stock": 15},
    {"sku": "PN004", "name": "Cat Brush Premium","category": "brush", "price": 21.00, "stock": 5}
]
def normalize_category(category):
    normarized_category=category.strip().lower()
    return normarized_category
def calculate_inventory_value(price,stock):
    result=price*stock
    return result
print("PurrNest Category Inventory Report Writer")
product_category=input("Enter Product Category: ")
normalized_category=normalize_category(product_category)
while normalized_category !="brush" and normalized_category !="bowl" and normalized_category !="toy":
    print("Invalid Category")
    product_category=input("Enter Product Category: ")
    normalized_category=normalize_category(product_category)
matching_count=0
total_stock=0
total_inventory_value=0.0
for product in products:
    if product["category"]==normalized_category:
        matching_count+=1
        total_stock+=product["stock"]
        inventory_value=calculate_inventory_value(product["price"],product["stock"])
        total_inventory_value+=inventory_value
with open("purrnest_category_inventory_report.txt","w") as file:
    file.write("PurrNest Category Inventory Report\n")
    file.write(f"Category: {normalized_category}\n")
    file.write(f"Matching Products: {matching_count}\n")
    file.write(f"Total Stock: {total_stock}\n")
    file.write(f"Total Inventory Value: RM{total_inventory_value:.2f}\n")
print("Category inventory report saved.")