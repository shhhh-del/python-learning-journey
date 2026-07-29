"""
Module 1 - Lesson 08
Shopee Order Acceptance Checker

Requirements:
1. Display: Shopee Order Acceptance Checker
2. Ask the user: Current Stock Quantity
3. Convert the input into an integer.
4. Print exactly one final result:
   - Stock below 0: Invalid Stock Data
   - Stock equal to 0: Reject Order
   - Stock up to and including 3: Accept Order - Low Stock Warning
   - Any higher stock: Accept Order

Check business rules from most specific to most general.
"""

# Write your implementation below this line.

print("Shopee Order Acceptance Checker")
stock_quantity=int(input("Current Stock Quantity:"))
if stock_quantity<0:
    print("Invalid Stock Data")
elif stock_quantity==0:
    print("Reject Order")
elif stock_quantity<=3:
    print("Accept Order - Low Stock Warning")
else:
    print("Accept Order")