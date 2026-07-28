"""
Module 1 - Lesson 06
Shopee Stock Input Validator

Requirements:
1. Display: Shopee Stock Input Validator
2. Ask the user: Enter Current Stock Quantity
3. Convert the input into an integer.
4. Print exactly one classification:
   - Below 0: Invalid Stock
   - Equal to 0: Out of Stock
   - Greater than 0: Valid Stock

Use only:
- print()
- input()
- int()
- comparison operators
- if / elif / else
"""

# Write your implementation below this line.

print("Shopee Stock Input Validator")
stock_quantity=int(input("Enter Current Stock Quantity: "))
if stock_quantity<0:
    print("Invalid Stock")
elif stock_quantity==0:
    print("Out of Stock")   
else:
    print("Valid Stock")