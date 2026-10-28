"""
Module 2 - Lesson 12
PurrNest Order Total Calculator
Date: 2026-10-28 | Tracker: JR-19

Write the implementation personally below.
Only new concept: exactly TWO parameters and TWO positional arguments.

Function requirements:
- Name: calculate_order_total
- Exactly two parameters, in this order: price, quantity.
- Calculate price * quantity using both parameters.
- RETURN one numeric result; do not print it inside the function.

Create ONE orders List containing three Dictionaries:
sku / price / quantity
PN001 / 15.90 / 2
PN002 / 12.50 / 3
PN003 / 8.90 / 1

Main program requirements:
- Display exactly: PurrNest Order Total Calculator
- Initialize grand_total before processing.
- Directly iterate over orders, taking one order Dictionary at a time.
- Display SKU: <current sku>.
- Pass current price and current quantity as TWO separate positional
  arguments in the correct order to calculate_order_total.
- Store the returned result in a variable.
- Display Order Total: RMxx.xx using that result.
- Accumulate the returned result into grand_total.
- After the loop display:
  Order Count: <len(orders)>
  Grand Total: RMxx.xx
Original order totals: RM31.80, RM37.50, RM8.90.
Original final result: count 3, Grand Total RM78.20.

FIRST STEP ONLY:
Write the function definition, two parameters, calculation, and return.
Do not add calls or a loop yet. Wait for review.

Allowed: previously learned function definitions/calls, return, variables,
Lists, Dictionaries, List of Dictionaries, iteration, field access,
arithmetic, accumulators, len, print, f-strings, .2f.
Do not introduce default parameters, keyword arguments, *args, **kwargs,
scope theory, global, lambda, recursion, classes, tuples, sets, CSV, JSON,
files, exceptions, modules, requests, HTTP, APIs, pandas, databases,
or Streamlit.

Six manual tests after code review:
1. Direct call with price 10 and quantity 2: predict before running.
2. Decimal price 12.50 and quantity 3: returned result 37.50.
3. Price 15.90 and quantity 0: returned result 0.00; zero is valid here.
4. Position test with a small subtract(first, second) function: predict
   subtract(10, 3) and subtract(3, 10) before running; verify position.
5. All original orders: count 3 and RM78.20, accumulated from return values.
6. Design ONE order Dictionary with sku/price/quantity, non-negative price
   and quantity, preferably decimal price. Predict price * quantity BEFORE
   running. Pass the two field values separately; compare returned result.
"""

# STUDENT CODE AREA
def calculate_order_total(price, quantity):
    result = price * quantity
    return result
orders=[
    {"sku": "PN001", "price": 15.90, "quantity": 2},
    {"sku": "PN002", "price": 12.50, "quantity": 3},
    {"sku": "PN003", "price": 8.90, "quantity": 1}
]
print("PurrNest Order Total Calculator")
grand_total=0
for order in orders:
    print(f"SKU: {order['sku']}")
    order_total=calculate_order_total(order['price'], order['quantity'])
    print(f"Order Total: RM{order_total:.2f}")
    grand_total+=order_total
print(f"Order Count: {len(orders)}")
print(f"Grand Total: RM{grand_total:.2f}")
