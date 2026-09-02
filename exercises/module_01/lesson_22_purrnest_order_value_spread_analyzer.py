"""
Module 1 - Lesson 22
PurrNest Order Value Spread Analyzer

Learning objective:
Calculate one derived metric after repeated input:
Order Value Spread = Highest Order Value - Lowest Order Value

Business scenario:
The seller enters today's Shopee order amounts and wants to identify the
highest order, lowest order, and the difference between them.

Requirements:
1. Display exactly:
   PurrNest Order Value Spread Analyzer
2. Ask the user for:
   Enter Order Amount:
3. Convert input using float().
4. Continue processing until the user enters the sentinel 0.

Positive Order Amount:
- It is one valid order.
- Maintain Highest and Lowest using the Lesson 21 logic.
- Ask for another Order Amount.

Negative Order Amount:
- Display exactly:
  Invalid Order Amount
- It must affect neither endpoint nor the Spread.
- Continue accepting input.

Order Amount equal to 0:
- End the session naturally.
- Do not treat it as an order or let it affect any metric.

After the loop, when at least one valid order exists:
- Calculate Order Value Spread as Highest minus Lowest.
- Display exactly:
  Highest Order Value: RMxx.xx
  Lowest Order Value: RMxx.xx
  Order Value Spread: RMxx.xx

When no valid order exists, display exactly:
Highest Order Value: N/A
Lowest Order Value: N/A
Order Value Spread: N/A

Format numeric money output to exactly two decimal places.

Allowed Python:
- print(), input(), float()
- variables, subtraction, and comparisons
- if / elif / else
- while
- a counter if genuinely needed
- f-string two-decimal formatting

Do not use:
- min(), max(), or abs()
- for loops
- break or continue
- functions
- lists or dictionaries
- try / except

You must personally decide:
- how the first valid order establishes Highest and Lowest
- how both endpoints are maintained
- where the Spread calculation belongs
- how no-order handling works
- where repeated input and final output belong
"""

# TODO: Write your implementation below this line.
print("PurrNest Order Value Spread Analyzer")
valid_highest_order=0
valid_lowest_order=0
order_amount=float(input("Enter Order Amount:"))

while order_amount!=0:
    if order_amount>0:
        if valid_highest_order==0 or order_amount>valid_highest_order:
            valid_highest_order=order_amount
        if valid_lowest_order==0 or order_amount<valid_lowest_order:
            valid_lowest_order=order_amount
        order_amount=float(input("Enter Order Amount:"))
        
    else:
        print("Invalid Order Amount")
        order_amount=float(input("Enter Order Amount:"))

if valid_highest_order>0 and valid_lowest_order>0:
    order_value_spread=valid_highest_order-valid_lowest_order
    print(f"Highest Order Value: RM{valid_highest_order:.2f}")
    print(f"Lowest Order Value: RM{valid_lowest_order:.2f}")
    print(f"Order Value Spread: RM{order_value_spread:.2f}")
else:
    print("Highest Order Value: N/A")
    print("Lowest Order Value: N/A")
    print("Order Value Spread: N/A")
    
