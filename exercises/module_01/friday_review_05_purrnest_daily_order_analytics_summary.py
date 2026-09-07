"""
Friday Review #5
PurrNest Daily Order Analytics Summary

Objective:
Combine previously verified analytics patterns into one repeated-input
business flow. Maintain raw metrics during processing and calculate derived
metrics after processing ends.

Display exactly:
PurrNest Daily Order Analytics Summary

Ask repeatedly:
Enter Order Amount:

Convert input using float().

Raw metrics to maintain:
- Total Orders
- Total Sales
- High-Value Orders
- Highest Order Value
- Lowest Order Value

High-Value rule:
Order Amount >= RM20.00

Positive Order Amount:
- Increase Total Orders by exactly 1.
- Add the amount to Total Sales.
- Independently check whether it increases High-Value Orders.
- Independently check whether Highest should change.
- Independently check whether Lowest should change.
- Ask for another Order Amount.

Negative Order Amount:
- Display exactly:
  Invalid Order Amount
- Change none of the business metrics.
- Continue accepting input.

Order Amount equal to 0:
- End the session naturally.
- Change none of the metrics.

After the loop, when Total Orders > 0, calculate:
- Average Order Value = Total Sales / Total Orders
- High-Value Rate = (High-Value Orders / Total Orders) * 100
- Order Value Spread = Highest Order Value - Lowest Order Value

Final output with at least one valid order:
Total Orders: X
Total Sales: RMxx.xx
Average Order Value: RMxx.xx
High-Value Orders: X
High-Value Rate: xx.xx%
Highest Order Value: RMxx.xx
Lowest Order Value: RMxx.xx
Order Value Spread: RMxx.xx

Final output with no valid orders:
Total Orders: 0
Total Sales: RM0.00
Average Order Value: N/A
High-Value Orders: 0
High-Value Rate: N/A
Highest Order Value: N/A
Lowest Order Value: N/A
Order Value Spread: N/A

Allowed Python:
- print(), input(), float()
- variables and arithmetic
- division, multiplication, subtraction
- comparisons
- if / elif / else
- while
- f-string two-decimal formatting

Do not use:
- for loops
- break or continue
- functions
- lists or dictionaries
- try / except
- min(), max(), or abs()

You must personally decide:
- how every raw metric starts
- where each valid-event update belongs
- how the first valid value establishes Highest and Lowest
- which calculations wait until after the loop
- how the no-order case is protected
- where repeated input and final output belong
"""

# TODO: Write your implementation below this line.

print("PurrNest Daily Order Analytics Summary")
order_amount=float(input("Enter Order Amount:"))

total_orders=0
total_sales= 0.0
high_value_orders=0
highest_order_value=0
lowest_order_value=0

while order_amount!=0:
    if order_amount>0:
        total_orders+=1
        total_sales+=order_amount
        if highest_order_value==0 or order_amount>highest_order_value:
            highest_order_value=order_amount
        if lowest_order_value==0 or lowest_order_value>order_amount:
            lowest_order_value=order_amount
        if order_amount>=20.00:
            high_value_orders+=1
    else:
        print("Invalid Order Amount")
    order_amount=float(input("Enter Order Amount:"))

if total_orders>0:
    average_order_value = total_sales / total_orders
    high_value_rate = (high_value_orders/ total_orders) * 100
    order_value_spread = highest_order_value - lowest_order_value
    print(f"Total Orders: {total_orders}")
    print(f"Total Sales: RM{total_sales:.2f}")
    print(f"Average Order Value: RM{average_order_value:.2f}")
    print(f"High-Value Orders: {high_value_orders}")
    print(f"High-Value Rate: {high_value_rate:.2f}%")
    print(f"Highest Order Value: RM{highest_order_value:.2f}")
    print(f"Lowest Order Value: RM{lowest_order_value:.2f}")
    print(f"Order Value Spread: RM{order_value_spread:.2f}")
else:
    print("Total Orders: 0")
    print("Total Sales: RM0.00")
    print("Average Order Value: N/A")
    print("High-Value Orders: 0")
    print("High-Value Rate: N/A")
    print("Highest Order Value: N/A")
    print("Lowest Order Value: N/A")
    print("Order Value Spread: N/A")


    



