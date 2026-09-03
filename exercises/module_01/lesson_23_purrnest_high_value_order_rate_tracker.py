"""
Module 1 - Lesson 23
PurrNest High-Value Order Rate Tracker

Learning objective:
Maintain one counter for all valid events and a conditional counter for valid
events that meet a fixed business rule.

Business scenario:
PurrNest wants to know what percentage of today's valid Shopee orders are
high-value orders.

High-Value rule:
Order Amount >= RM20.00

Requirements:
1. Display exactly:
   PurrNest High-Value Order Rate Tracker
2. Maintain counters for:
   - Total Valid Orders
   - High-Value Orders
3. Ask the user for:
   Enter Order Amount:
4. Convert input using float().
5. Continue processing until the user enters the sentinel 0.

Positive Order Amount:
- Increase Total Valid Orders by exactly 1.
- Independently check whether Order Amount >= 20.00.
- If it meets the threshold, increase High-Value Orders by exactly 1.
- Otherwise leave High-Value Orders unchanged.
- Ask for another Order Amount.

Negative Order Amount:
- Display exactly:
  Invalid Order Amount
- Increase neither counter.
- Continue accepting input.

Order Amount equal to 0:
- End the session naturally.
- It is not an order and must increase neither counter.

After the loop, when Total Valid Orders > 0:
- Calculate:
  High-Value Rate = (High-Value Orders / Total Valid Orders) * 100
- Display exactly:
  Total Orders: X
  High-Value Orders: X
  High-Value Rate: xx.xx%

When Total Valid Orders == 0:
- Do not divide.
- Display exactly:
  Total Orders: 0
  High-Value Orders: 0
  High-Value Rate: N/A

Allowed Python:
- print(), input(), float()
- variables and arithmetic
- division and multiplication
- comparison operators
- if / elif / else
- while
- f-string two-decimal formatting

Do not use:
- for loops
- break or continue
- functions
- lists or dictionaries
- try / except
- min() or max()

You must personally decide:
- where both counters begin
- where each counter increases
- how the >= 20.00 boundary is handled
- where repeated input belongs
- where rate calculation belongs
- how division by zero is prevented
- where final output belongs
"""

# TODO: Write your implementation below this line.
print("PurrNest High-Value Order Rate Tracker")
total_valid_orders=0
high_value_orders=0
order_amount=float(input("Enter Order Amount:"))
while order_amount!=0:
    if order_amount>0:
        total_valid_orders+=1
        if order_amount>=20.00:
            high_value_orders+=1
        
    elif order_amount<0:
        print("Invalid Order Amount")
    order_amount=float(input("Enter Order Amount:"))

if total_valid_orders>0:
    high_value_rate=(high_value_orders/total_valid_orders)*100
    print(f"Total Orders: {total_valid_orders}")
    print(f"High-Value Orders: {high_value_orders}")
    print(f"High-Value Rate: {high_value_rate:.2f}%")
else:
    print("Total Orders: 0")
    print("High-Value Orders: 0")
    print("High-Value Rate: N/A")