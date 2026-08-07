"""
Friday Review #2
PurrNest Financial Decision System

Requirements:
1. Display: PurrNest Financial Decision System
2. Ask for: Selling Price
3. Ask for: Product Cost
4. Ask for: Packaging Cost
5. Convert every money input using float().
6. If any input is negative, print exactly:
   - INVALID INPUT
7. Invalid input must stop further calculation and business-result output.
8. Otherwise, calculate Total Cost and Profit.
9. If Selling Price is equal to 0, print:
   - Profit Margin: N/A
10. Otherwise, calculate:
    - Profit Margin = (Profit / Selling Price) * 100
11. For valid input, print:
    - Total Cost: RMxx.xx
    - Profit: RMxx.xx
    - Profit Margin: xx.xx% (or Profit Margin: N/A)
12. Print exactly one final status for valid input:
    - PROFIT
    - BREAK-EVEN
    - LOSS
13. Format every money value and calculated percentage to exactly two decimal places.

Required manual tests:
- Selling Price 20 / Product Cost 10 / Packaging Cost 2
- Selling Price 12 / Product Cost 10 / Packaging Cost 2
- Selling Price 10 / Product Cost 10 / Packaging Cost 2
- Selling Price 0 / Product Cost 0 / Packaging Cost 0
- Selling Price -1 / Product Cost 10 / Packaging Cost 2
- Selling Price 10 / Product Cost -5 / Packaging Cost 2
- One additional student-designed test
"""

# Write your implementation below this line.

print("PurrNest Financial Decision System")
selling_price=float(input("Enter selling price:"))
product_cost=float(input("Enter product cost:"))
packaging_cost=float(input("Enter packaging cost:"))
if selling_price<0 or product_cost<0 or packaging_cost<0:
    print("INVALID INPUT")
else:
    total_cost=product_cost+packaging_cost
    profit=selling_price-total_cost
    print(f"Total Cost: RM{total_cost:.2f}")
    print(f"Profit: RM{profit:.2f}")

    if selling_price==0:
        print("Profit Margin: N/A")
    else:
        profit_margin=(profit/selling_price)*100
        print(f"Profit Margin: {profit_margin:.2f}%")

    if profit>0:
        print("PROFIT")
    elif profit==0:
        print("BREAK-EVEN")
    else:
        print("LOSS")
