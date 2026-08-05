"""
Module 1 - Lesson 11
PurrNest Profit Margin Calculator

Requirements:
1. Display: PurrNest Profit Margin Calculator
2. Ask for: Selling Price
3. Ask for: Product Cost
4. Ask for: Packaging Cost
5. Convert every money input using float().
6. Calculate Total Cost.
7. Calculate Profit.
8. If Selling Price is equal to 0, print:
   - Profit Margin: N/A
9. Otherwise, calculate the profit margin percentage and print it as:
   - Profit Margin: xx.xx%
10. Also print money in these formats:
    - Total Cost: RMxx.xx
    - Profit: RMxx.xx
11. Print exactly one final status:
    - Profit greater than 0: PROFIT
    - Profit equal to 0: BREAK-EVEN
    - Otherwise: LOSS
12. Format every money value and calculated percentage to exactly two decimal places.

Required manual tests:
- Selling Price 20.00 / Product Cost 10.00 / Packaging Cost 2.00
- Selling Price 12.00 / Product Cost 10.00 / Packaging Cost 2.00
- Selling Price 10.00 / Product Cost 10.00 / Packaging Cost 2.00
- Selling Price 0.00 / Product Cost 0.00 / Packaging Cost 0.00
- One additional student-selected test
"""

# Write your implementation below this line.
print("PurrNest Profit Margin Calculator")
selling_price=float(input("Enter selling price:"))
product_cost=float(input("Enter product cost:"))
packaging_cost=float(input("Enter packaging cost:"))
total_cost=product_cost+packaging_cost
profit=selling_price-total_cost
if selling_price==0:
    print("Profit Margin: N/A")
else:
    profit_margin=(profit/selling_price)*100
    print(f"Profit Margin: {profit_margin:.2f}%")

print(f"Total Cost: RM{total_cost:.2f}")
print(f"Profit: RM{profit:.2f}")
if profit>0:
    print("PROFIT")
elif profit==0:
    print("BREAK-EVEN")
else:
    print("LOSS")
