"""
Friday Review Exercise
Shopee Inventory Decision System

Requirements:
1. Display: Shopee Inventory Decision System
2. Ask: Current Stock Quantity
3. Convert the stock input into an integer.
4. Ask: VIP Customer (yes/no)
5. Print exactly one final result:
   - Stock below 0: Invalid Stock Data
   - Stock equal to 0: Reject Order
   - Stock up to and including 3: Accept Order - Low Stock Warning
   - Stock above 3 and VIP is yes: Priority Packing
   - Stock above 3 and VIP is not yes: Normal Packing

Use a nested if statement for the VIP decision.

Required manual tests:
- Stock=-1, VIP=yes
- Stock=0, VIP=no
- Stock=2, VIP=yes
- Stock=4, VIP=yes
- Stock=4, VIP=no
- One additional test chosen by the student
"""

# Write your implementation below this line.

print("Shopee Inventory Decision System")
stock_quantity=int(input("Current Stock Quantity:"))
vip_confirmation=input("VIP Customer (yes/no):")
if stock_quantity<0:
    print("Invalid Stock Data")
elif stock_quantity==0:
    print("Reject Order")
elif stock_quantity<=3:
    print("Accept Order - Low Stock Warning")
else:
    if vip_confirmation=="yes":
        print("Priority Packing")
    else:
        print("Normal Packing")
    