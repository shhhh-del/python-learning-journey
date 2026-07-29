"""
Module 1 - Lesson 07
Shopee Inventory Action Checker

Requirements:
1. Display: Shopee Inventory Action Checker
2. Ask the user: Current Stock Quantity
3. Convert the input into an integer.
4. Print exactly one classification:
   - Stock below 0: Invalid Stock
   - Stock equal to 0: Restock Immediately
   - Stock up to and including 5: Low Stock - Reorder Soon
   - Stock up to and including 20: Stock Level Normal
   - Any higher stock: Stock Sufficient

Use an ordered if / elif / else chain.
"""

# Write your implementation below this line.

print("Shopee Inventory Action Checker")
stock_quantity=int(input("Current Stock Quantity:"))
if stock_quantity<0:
    print("Invalid Stock")
elif stock_quantity==0:
    print("Restock Immediately")
elif stock_quantity<=5:
    print("Low Stock - Reorder Soon")
elif stock_quantity<=20:
    print("Stock Level Normal")
else:
    print("Stock Sufficient")