"""
Module 1 - Lesson 09
PurrNest Product Profit Preview

Requirements:
1. Display: PurrNest Product Profit Preview
2. Ask for: Selling Price
3. Ask for: Product Cost
4. Convert both inputs using float().
5. Calculate profit by subtracting product cost from selling price.
6. Print profit in this format: Profit: RMxx.xx
7. Print exactly one final status:
   - Profit greater than 0: PROFIT
   - Profit equal to 0: BREAK-EVEN
   - Otherwise: LOSS
8. Format the profit to exactly two decimal places.

Required manual tests:
- Selling Price 17.90 / Product Cost 10.00
- Selling Price 20.00 / Product Cost 20.00
- Selling Price 15.00 / Product Cost 20.00
- Selling Price 0.00 / Product Cost 0.00
- One additional student-selected test
"""

# Write your implementation below this line.
print("PurrNest Product Profit Preview")
selling_price=float(input("Selling Price:"))
product_cost=float(input("Product Cost:"))
profit=selling_price-product_cost
print(f"Profit: RM{profit:.2f}")
if profit>0:
    print("PROFIT")
elif profit==0:
    print("BREAK-EVEN")
else:
    print("LOSS")
