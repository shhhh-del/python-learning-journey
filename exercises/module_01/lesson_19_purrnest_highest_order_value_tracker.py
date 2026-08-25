"""
Module 1 - Lesson 19
PurrNest Highest Order Value Tracker

Learning objective:
Track the highest valid value seen so far during repeated input without using
the built-in max() function.

Business scenario:
The seller enters today's Shopee order amounts and wants to know the largest
valid order amount entered during the session.

Requirements:
1. Display exactly:
   PurrNest Highest Order Value Tracker
2. Create a variable representing the highest valid Order Amount seen so far.
3. Use previously verified counter logic if needed to distinguish between no
   valid orders and at least one valid order.
4. Ask the user for:
   Enter Order Amount:
5. Convert input using float().
6. Continue processing until the user enters the sentinel 0.

Positive Order Amount:
- Represents one valid order.
- Compare it with the stored highest valid order value.
- If the new amount is larger, update the stored highest value.
- If it is smaller or equal, keep the stored highest value unchanged.
- Ask for the next Order Amount.

Negative Order Amount:
- Display exactly:
  Invalid Order Amount
- Do not let it change the highest value.
- Continue accepting input so later valid orders can be processed.

Order Amount equal to 0:
- End the session naturally.
- Do not treat 0 as an order or highest value.

After the loop:
- If at least one valid positive order was processed, display:
  Highest Order Value: RMxx.xx
- Otherwise display:
  Highest Order Value: N/A

Format the numeric money output to exactly two decimal places.

Allowed Python:
- print()
- input()
- float()
- variables
- arithmetic if needed
- comparison operators
- if / elif / else
- while
- a counter if needed
- f-string two-decimal formatting

Do not use:
- min() or max()
- for loops
- break or continue
- functions
- lists or dictionaries
- try / except
- CSV or JSON
- APIs or databases
- Streamlit

You must personally decide:
- how the highest-value variable begins
- whether a counter is needed for the no-order case
- where comparison and updates belong
- where repeated input belongs
- where final output belongs

You must personally write and understand the core implementation.
"""

# TODO: Write your implementation below this line.

print("PurrNest Highest Order Value Tracker")
valid_highest_order=0

order_amount=float(input("Enter Order Amount:"))
while order_amount!=0:
    if order_amount>0:
        if order_amount>valid_highest_order:
            valid_highest_order=order_amount
        else:
            valid_highest_order=valid_highest_order
        order_amount=float(input("Enter Order Amount:"))

    else:
        print("Invalid Order Amount")
        order_amount=float(input("Enter Order Amount:"))

if valid_highest_order>0:
    print(f"Highest Order Value: RM{valid_highest_order:.2f}")
else:
    print("Highest Order Value: N/A")