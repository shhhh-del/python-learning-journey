"""
Module 1 - Lesson 13
PurrNest Low Stock Countdown

Learning objective:
Use a basic while loop to repeat an action while a condition remains true,
and update the loop state so the loop eventually stops.

Business scenario:
PurrNest wants a simple Shopee stock countdown that shows each remaining
unit until the stock reaches zero.

Requirements:
1. Ask the user for a starting stock quantity.
2. Convert the input using int().
3. If the starting stock is negative, display exactly:
   Invalid Stock
   Do not run the countdown.
4. If the starting stock is 0, display exactly:
   Out of Stock
   Do not run the countdown.
5. If the starting stock is greater than 0:
   - Use a while loop.
   - For each remaining positive quantity, display:
     Stock Remaining: X
   - Decrease the stock by one during each repetition.
   - When the stock reaches zero, display:
     Out of Stock

Expected behavior for starting stock 3:
Stock Remaining: 3
Stock Remaining: 2
Stock Remaining: 1
Out of Stock

Allowed Python:
- print()
- input()
- int()
- variables
- arithmetic
- comparisons
- if / elif / else
- while

Do not use:
- for loops
- lists or dictionaries
- functions
- break or continue
- CSV or JSON
- APIs or databases
- Streamlit
- exception handling

You must personally write and understand the core implementation.
"""

# TODO: Write your implementation below this line.

stock_quantity=int(input("enter starting stock quantity:"))
if stock_quantity<0:
    print("Invalid Stock")
elif stock_quantity==0:
    print("Out of Stock")
else:
    while stock_quantity>0:
        print("Stock Remaining:",stock_quantity)
        stock_quantity-=1
    print("Out of Stock")