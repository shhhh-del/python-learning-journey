"""
Module 2 - Lesson 11
PurrNest Product Inventory Value Calculator
Date: 2026-10-22 | Tracker: JR-19

Write the implementation personally below.
Only major new concept: one returned value.

Function requirements:
- Define calculate_inventory_value with exactly ONE parameter: product.
- The parameter receives one product Dictionary.
- Read current price and stock by key, calculate price * stock.
- RETURN the calculated number to the caller.
- Do not print the calculated result inside the function.

Original products List: three Dictionaries, each with sku/name/price/stock:
PN001 / Cat Brush / 15.90 / 20
PN002 / Cat Bowl  / 12.50 / 8
PN003 / Cat Toy   / 8.90  / 15

Final main program:
- Display: PurrNest Product Inventory Value Calculator
- Initialize total_inventory_value before processing.
- Directly iterate over the products List.
- Display current SKU: <sku>.
- Call the function with the current Dictionary and store its returned
  number in a variable of your choice.
- Display Inventory Value: RMxx.xx using the received number.
- Add that received number to total_inventory_value.
- After the loop display:
  Product Count: <len(products)>
  Total Inventory Value: RMxx.xx
Original values: PN001 RM318.00, PN002 RM100.00, PN003 RM133.50;
count 3, total RM551.50.

FIRST STEP ONLY:
Write the function definition, calculation, and return statement.
Do not add a loop or calls yet. Wait for review.

Allowed: previously learned function definition/calls, one parameter and
argument, Dictionary reads, Lists/records, direct iteration, multiplication,
accumulators, len(), print, f-strings, .2f.
Do not use multiple parameters, default/keyword arguments, *args, **kwargs,
advanced scope, global, lambda, recursion, classes, tuples, sets, CSV, JSON,
files, exceptions, modules, requests, HTTP, APIs, pandas, databases,
Streamlit, or functions returning multiple values.

Manual tests after code review:
1. PN001 direct call: predict before running; verify caller receives result.
2. PN002 direct call: same function, expected 100.00.
3. Zero stock: price 15.90, stock 0 -> returned value 0.00.
4. Decimal result: price 12.75, stock 3; predict BEFORE running.
5. All original records: count 3 / total RM551.50, accumulated from returned
   values rather than separately recalculated in the caller.
6. Design one Dictionary with sku/name/price/stock, non-negative price and
   stock, preferably decimal price. Predict price * stock BEFORE running,
   then verify returned result matches.
"""

# STUDENT CODE AREA
def calculate_inventory_value(product):
    result=product["price"]*product["stock"]
    return result
products=[
    {"sku": "PN001", "name": "Cat Brush", "price": 15.90, "stock": 20},
    {"sku": "PN002", "name": "Cat Bowl",  "price": 12.50, "stock": 8},
    {"sku": "PN003", "name": "Cat Toy",   "price": 8.90,  "stock": 15}
]

print("PurrNest Product Inventory Value Calculator")
total_inventory_value=0
for product in products:
    print(f"SKU: {product['sku']}")
    inventory_value = calculate_inventory_value(product)
    print(f"Inventory Value: RM{inventory_value:.2f}")
    total_inventory_value += inventory_value
print(f"Product Count: {len(products)}")
print(f"Total Inventory Value: RM{total_inventory_value:.2f}")

