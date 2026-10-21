"""
Module 2 - Lesson 10
PurrNest Reusable Product Display
Date: 2026-10-21 | Tracker: JR-19

Write the implementation personally in the STUDENT CODE AREA.
Only major new concept: ONE function parameter and its argument.

Define one main function named show_product with exactly ONE parameter.
The parameter represents one product Dictionary.
Inside its body, read values from that parameter and display exactly:
SKU: <sku>
Product Name: <name>
Price: RMxx.xx
Stock: <stock>
Do not hard-code product values inside the function.

Create ONE products List containing three Dictionaries:
sku / name / price / stock
PN001 / Cat Brush / 15.90 / 20
PN002 / Cat Bowl  / 12.50 / 8
PN003 / Cat Toy   / 8.90  / 15

Final main program:
- Display: PurrNest Reusable Product Display
- Iterate directly over products, passing the current Dictionary as the
  argument to show_product on each iteration.
- Do not repeat the four display print lines in the loop.
- After the loop, call the same function once more with products[0].
The loop supplies each record; the function displays one record.

First step ONLY:
Write the show_product definition and its four-line display body.
Use one parameter to receive the Dictionary and read its fields by key.
Do not add calls or the main loop yet. Wait for review.

Allowed: previous Lists, Dictionaries, List of Dictionaries, key reads,
direct iteration, len(), f-strings, .2f, and basic function definitions/calls.
Do not use return, multiple parameters, default parameters, keyword
arguments, *args, **kwargs, type hints, lambda, recursion, scope theory,
classes, CSV, JSON, files, exceptions, modules, requests, HTTP, APIs,
pandas, databases, or Streamlit.

Manual tests after code review:
1. First product only: pass products[0], verify PN001 and its values.
2. Second product only: pass products[1], no function-body changes.
3. Third product only: pass products[2], verify PN003 and its values.
4. Full List iteration: pass each current record, order PN001/PN002/PN003.
5. Change PN002 name to Cat Food Bowl and price to 14.90; verify same
   function displays new values without function-body changes.
6. Design one new Dictionary with sku/name/price/stock. Predict complete
   output BEFORE calling the function, then compare actual output.
"""

# STUDENT CODE
def show_product(product):
    print(f"SKU: {product['sku']}")
    print(f"Product Name: {product['name']}")
    print(f"Price: RM{product['price']:.2f}")
    print(f"Stock: {product['stock']}")
products=[
    {"sku": "PN001", "name": "Cat Brush", "price": 15.90, "stock": 20},
    {"sku": "PN002", "name": "Cat Bowl",  "price": 12.50, "stock": 8},
    {"sku": "PN003", "name": "Cat Toy",   "price": 8.90,  "stock": 15}
]
print("PurrNest Reusable Product Display")
for product in products:
    show_product(product)
show_product(products[0])


             