"""
Module 1 - Lesson 10
PurrNest Product Margin Calculator

Requirements:
1. Display: PurrNest Product Margin Calculator
2. Ask for: Selling Price
3. Ask for: Product Cost
4. Ask for: Packaging Cost
5. Convert every money input using float().
6. Calculate Total Cost.
7. Calculate Profit.
8. Print money in these formats:
   - Total Cost: RMxx.xx
   - Profit: RMxx.xx
9. Print exactly one final status:
   - Profit greater than 0: PROFIT
   - Profit equal to 0: BREAK-EVEN
   - Otherwise: LOSS
10. Format every money value to exactly two decimal places.

Required manual tests:
- Selling Price 20.00 / Product Cost 10.00 / Packaging Cost 2.00
- Selling Price 12.00 / Product Cost 10.00 / Packaging Cost 2.00
- Selling Price 10.00 / Product Cost 10.00 / Packaging Cost 2.00
- Selling Price 0.00 / Product Cost 0.00 / Packaging Cost 0.00
- One additional student-selected test
"""

# Write your implementation below this line.

print("PurrNest Product Margin Calculator")
selling_price=float(input("Enter Selling Price:"))
product_cost=float(input("Enter Product Cost:"))
packaging_cost=float(input("Enter Packaging Cost:"))
total_cost=product_cost+packaging_cost
profit=selling_price-total_cost
print(f"Total Cost: RM{total_cost:.2f}")
print(f"Profit: RM{profit:.2f}")
if profit>0:
    print("PROFIT")
elif profit==0:
    print("BREAK-EVEN")
else:
    print("LOSS")