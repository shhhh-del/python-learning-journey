"""
Module 2 - Lesson 13
PurrNest Order Discount Calculator
Date: 2026-11-02 | Tracker: JR-19

Write the implementation personally below.
Only major new concept: basic local function scope.

Function requirements:
- Define calculate_discounted_total with two parameters, price and quantity.
- Create these local working variables INSIDE the function:
  original_total: price * quantity
  discount: 10% of original_total if original_total >= 50, otherwise 0
  final_total: original_total minus discount
- Return only final_total's numeric value.
- Do not print inside the function or expose internal variables outside it.
- Do not use global variables as a workaround.

Original orders List: three Dictionaries with sku/price/quantity:
PN001 / 15.90 / 2
PN002 / 20.00 / 3
PN003 / 8.90 / 1

Final main program:
- Display exactly: PurrNest Order Discount Calculator
- Initialize grand_total outside the processing loop.
- Iterate directly over orders.
- Display SKU: <current sku>.
- Pass current price and quantity to the function in that order.
- Store returned final amount in a caller variable of your choice.
- Display Final Order Total: RMxx.xx using the caller variable.
- Add that caller variable's value to grand_total.
- After the loop display Grand Total: RMxx.xx.
Original final amounts: RM31.80 / RM54.00 / RM8.90; grand total RM94.70.
The caller must use its receiving variable, not the function's local names.

FIRST STEP ONLY:
Write the function definition, local calculations, if/else, and return.
Do not add main program, List, calls, or loop yet. Wait for review.

Allowed: verified function definitions/calls, two positional arguments,
return, if/else, arithmetic, comparisons, Lists/records, direct iteration,
accumulators, print, f-strings, .2f.
Do not introduce global, nonlocal, closures, nested functions, default or
keyword arguments, *args, **kwargs, lambda, recursion, classes, tuples,
sets, CSV, JSON, files, exceptions, modules, requests, HTTP, APIs, pandas,
databases, or Streamlit.

Manual tests after pre-run review:
1. Below threshold: price 10 / quantity 2 -> final 20.00.
2. Exact boundary: price 25 / quantity 2 -> original 50.00, final 45.00.
3. Above threshold: price 20 / quantity 3 -> final 54.00.
4. Zero quantity: price 20 / quantity 0 -> final 0.00.
5. Original full orders List -> Grand Total RM94.70.
6. Design non-negative price and quantity and choose below/equal/above
   threshold. BEFORE running predict original total, discount eligibility,
   discount amount and final returned result; then compare actual output.
"""

# STUDENT CODE AREA
def calculate_discounted_total(price,quantity):
    original_total=price*quantity
    if original_total >=50:
        discount=original_total*0.10
    else:
        discount=0
    final_total=original_total-discount
    return final_total
products=[
    {"sku": "PN001","price": 15.90, "quantity": 2},
    {"sku": "PN002","price": 20.00, "quantity": 3},
    {"sku": "PN003","price": 8.90, "quantity": 1}
]

print("PurrNest Order Discount Calculator")
grand_total=0
for product in products:
    print(f"SKU: {product['sku']}")
    final_amount=calculate_discounted_total(product['price'],product['quantity'])
    print(f"Final Order Total: RM{final_amount:.2f}")
    grand_total+=final_amount
print(f"Grand Total: RM{grand_total:.2f}")
