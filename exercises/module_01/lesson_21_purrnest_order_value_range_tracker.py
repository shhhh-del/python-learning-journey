"""
Module 1 - Lesson 21
PurrNest Order Value Range Tracker

Learning objective:
Track both the highest and lowest valid values during the same repeated-input
session without using min() or max().

Business scenario:
The seller enters today's Shopee order amounts and wants to identify both the
largest and smallest valid order amounts.

Requirements:
1. Display exactly:
   PurrNest Order Value Range Tracker
2. Ask the user for:
   Enter Order Amount:
3. Convert input using float().
4. Continue processing until the user enters the sentinel 0.

Positive Order Amount:
- It is one valid order.
- Evaluate whether it should update Highest Order Value.
- Also evaluate whether it should update Lowest Order Value.
- The first valid order establishes both values.
- Ask for another Order Amount.

Negative Order Amount:
- Display exactly:
  Invalid Order Amount
- It must change neither Highest nor Lowest.
- Continue accepting input.

Order Amount equal to 0:
- End the session naturally.
- Do not treat 0 as an order.
- It must change neither Highest nor Lowest.

Final output when at least one valid order exists:
Highest Order Value: RMxx.xx
Lowest Order Value: RMxx.xx

Final output when no valid order exists:
Highest Order Value: N/A
Lowest Order Value: N/A

Format money output to exactly two decimal places.

Allowed Python:
- print(), input(), float()
- variables and comparisons
- if / elif / else
- while
- a counter if genuinely needed
- f-string two-decimal formatting

Do not use:
- min() or max()
- for loops
- break or continue
- functions
- lists or dictionaries
- try / except

You must personally decide:
- how first-valid-value handling works
- how Highest and Lowest begin
- when each value updates or stays unchanged
- how no-order handling works
- where repeated input and final output belong
"""

# TODO: Write your implementation below this line.

print("PurrNest Order Value Range Tracker")
order_amount=float(input("Enter Order Amount:"))
valid_highest_order=0
valid_lowest_amount=0

while order_amount!=0: 
    if order_amount>0:
        if valid_highest_order==0 or order_amount>valid_highest_order:
            valid_highest_order=order_amount
        if valid_lowest_amount==0 or valid_lowest_amount>order_amount:
            valid_lowest_amount=order_amount
        order_amount=float(input("Enter Order Amount:"))
    else:
        print("Invalid Order Amount")
        order_amount=float(input("Enter Order Amount:"))

if valid_highest_order>0:
    print(f"Highest Order Value: RM{valid_highest_order:.2f}")
    print(f"Lowest Order Value: RM{valid_lowest_amount:.2f}")
else:
    print("Highest Order Value: N/A")
    print("Lowest Order Value: N/A")
