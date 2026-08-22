"""
PurrNest Shopee Order Profit Calculator
Version 1 - Stage 1B.2: Multi-Order Session Summary

Business problem:
A seller may calculate multiple Shopee orders in one working session, with
each order containing multiple units of the same product.

Your task:
1. Ask for the following inputs:
   - Selling Price Per Unit (float)
   - Quantity (int)
   - Product Cost Per Unit (float)
   - Packaging Cost (float)
   - Shopee Fee (float)
   - Seller Discount (float)
   - Other Cost (float)

2. Print exactly "INVALID INPUT" when:
   - any money value is negative, or
   - Quantity is zero or negative.

3. Invalid input must not continue to financial calculations or results.

4. For valid input, calculate:
   Total Sales Revenue = Selling Price Per Unit * Quantity
   Total Product Cost = Product Cost Per Unit * Quantity
   Total Order Cost = Total Product Cost + Packaging Cost + Shopee Fee
                      + Seller Discount + Other Cost
   Net Profit = Total Sales Revenue - Total Order Cost

5. For valid input, display:
   Total Sales Revenue: RMxx.xx
   Total Product Cost: RMxx.xx
   Total Order Cost: RMxx.xx
   Net Profit: RMxx.xx

6. Then display exactly one status:
   Order Status: PROFITABLE
   Order Status: BREAK-EVEN
   Order Status: LOSS

All money output must use two decimal places.

Scope:
Use while loops only for repeated input validation and repeated order
processing. Do not use functions, for loops, lists, dictionaries, CSV, JSON,
databases, APIs, GUIs, Streamlit, profit margin, or multiple different products.

You must personally write and understand the core implementation.
"""

# Write your Stage 1B implementation below this line

orders_processed=0
session_total_sales_revenue=0.0
session_total_net_profit=0.0

process_another_order ="yes"
while process_another_order=="yes":

    selling_price=float(input("Enter selling price per unit:"))
    while selling_price<0:
        print("Invalid Selling Price")
        selling_price=float(input("Enter selling price per unit:"))
    quantity=int(input("Enter quantity:"))
    while quantity<=0:
        print("invalid Quantity")
        quantity=int(input("Enter quantity:"))
    product_cost=float(input("Enter product cost per unit:"))
    while product_cost<0:
        print("Invalid Product Cost")
        product_cost=float(input("Enter product cost per unit:"))
    packaging_cost=float(input("Enter packaging cost:"))
    while packaging_cost<0:
        print("Invalid Packaging Cost")
        packaging_cost=float(input("Enter packaging cost:"))
    shopee_fee=float(input("Enter shopee fee:"))
    while shopee_fee<0:
        print("Invalid Shopee Fee")
        shopee_fee=float(input("Enter shopee fee:"))
    seller_discount=float(input("Enter seller discount:"))
    while seller_discount<0:
        print("Invalid Seller Discount")
        seller_discount=float(input("Enter seller discount:"))
    other_cost=float(input("Enter other cost:"))
    while other_cost<0:
        print("Invalid Other Cost")
        other_cost=float(input("Enter other cost:"))

    if selling_price<0 or quantity<=0 or product_cost<0 or packaging_cost<0 or shopee_fee<0 or seller_discount<0 or other_cost<0:
        print("INVALID INPUT")
    else:
        total_sales_revenue=selling_price*quantity
        total_product_cost=product_cost*quantity
        total_order_cost=total_product_cost+packaging_cost+shopee_fee+seller_discount+other_cost
        net_profit=total_sales_revenue-total_order_cost

        print(f"Total Sales Revenue: RM{total_sales_revenue:.2f}")
        print(f"Total Product Cost: RM{total_product_cost:.2f}")
        print(f"Total Order Cost: RM{total_order_cost:.2f}")
        print(f"Net Profit: RM{net_profit:.2f}")

        if net_profit>0:
            status="PROFITABLE"
        elif net_profit==0:
            status="BREAK-EVEN"
        else:
            status="LOSS"

        print(f"Order Status: {status}")

        orders_processed+=1
        session_total_sales_revenue+=total_sales_revenue
        session_total_net_profit+=net_profit
        process_another_order = input("Process Another Order? (yes/no):")


print("Session Summary")
print(f"Orders Processed: {orders_processed}")
print(f"Total Sales Revenue: RM{session_total_sales_revenue:.2f}")
print(f"Total Net Profit: RM{session_total_net_profit:.2f}")
