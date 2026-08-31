"""
Module 1 - Lesson 20
PurrNest Lowest Order Value Tracker

Learning objective:
Track the lowest valid value seen so far during repeated input without using
the built-in min() function.

Business scenario:
The seller enters today's Shopee order amounts and wants to know the smallest
valid order amount entered during the session.

Requirements:
1. Display exactly:
   PurrNest Lowest Order Value Tracker
2. Ask the user for:
   Enter Order Amount:
3. Convert input using float().
4. Continue processing until the user enters the sentinel 0.

Positive Order Amount:
- Represents one valid order.
- Compare it with the stored lowest valid order value.
- If the new amount is smaller, update the stored lowest value.
- If it is equal to or larger, keep the stored lowest value unchanged.
- Ask for the next Order Amount.

Negative Order Amount:
- Display exactly:
  Invalid Order Amount
- Do not let it change the lowest value.
- Continue accepting input.

Order Amount equal to 0:
- End the session naturally.
- Do not treat 0 as an order or as the lowest value.

After the loop:
- If at least one valid positive order was processed, display:
  Lowest Order Value: RMxx.xx
- Otherwise display:
  Lowest Order Value: N/A

Format numeric money output to exactly two decimal places.

Allowed Python:
- print(), input(), float()
- variables and comparison operators
- if / elif / else
- while
- a counter if useful
- f-string two-decimal formatting

Do not use:
- min() or max()
- for loops
- break or continue
- functions
- lists or dictionaries
- try / except

You must personally decide:
- how the lowest-value state begins
- how the first valid order is handled
- whether a counter is useful for no-order detection
- where comparison and repeated input belong
- where final output belongs
"""

# TODO: Write your implementation below this line.

print("PurrNest Lowest Order Value Tracker")
valid_lowest_order=0
order_amount=float(input("Enter Order Amount:"))
while order_amount!=0:
    if order_amount>0:
        if valid_lowest_order==0 or order_amount<valid_lowest_order:
            valid_lowest_order=order_amount
        else:
            valid_lowest_order=valid_lowest_order
        order_amount=float(input("Enter Order Amount:"))
    else:
        print("Invalid Order Amount")
        order_amount=float(input("Enter Order Amount:"))

if valid_lowest_order>0:
    print(f"Lowest Order Value: RM{valid_lowest_order:.2f}")
else:
    print("Lowest Order Value: N/A")
        
