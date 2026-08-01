"""
PurrNest Shopee Order Profit Calculator
Stage 1A - Single Order Net Profit Decision

Your task:
1. Ask for these six values and convert each one with float(input(...)):
   - selling_price
   - product_cost
   - packaging_cost
   - shopee_fee
   - seller_discount
   - other_cost
2. If any value is below zero, print exactly: INVALID INPUT
3. Otherwise, calculate total_cost and net_profit.
4. Classify the valid order as PROFITABLE, BREAK-EVEN, or LOSS.
5. For valid input, print exactly these two result lines:
   Net Profit: RMxx.xx
   Order Status: STATUS

Keep this version to one order and use only the Python concepts specified
for Stage 1A. You must personally write the core calculations and decisions.
"""

# Write your implementation below this line.

selling_price=float(input("Enter selling price:"))
product_cost=float(input("Enter product cost:"))
packaging_cost=float(input("Enter packaging cost:"))
shopee_fee=float(input("Enter shopee fee:"))
seller_discount=float(input("Enter seller discount:"))
other_cost=float(input("Enter other cost:"))
if selling_price<0 or product_cost<0 or packaging_cost<0 or shopee_fee<0 or seller_discount<0 or other_cost<0:
    print("INVALID INPUT")
else:
    total_cost=product_cost+packaging_cost+shopee_fee+seller_discount+other_cost
    net_profit=selling_price-total_cost
    if net_profit>0:
        status="PROFITABLE"
    elif net_profit==0:
        status="BREAK-EVEN"
    else:
        status="LOSS"

    print(f"Net Profit: RM{net_profit:.2f}")
    print(f"Order Status: {status}")