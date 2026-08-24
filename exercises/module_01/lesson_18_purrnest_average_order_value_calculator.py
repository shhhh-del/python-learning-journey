"""
Module 1 - Lesson 18
PurrNest Average Order Value Calculator

Learning objective:
Calculate an average from a completed accumulator and valid-event counter.

Business scenario:
The seller enters today's Shopee order amounts and wants to see the number of
valid orders, total sales, and Average Order Value.

Requirements:
1. Display exactly:
   PurrNest Average Order Value Calculator
2. Create total_sales starting at 0.
3. Create order_count starting at 0.
4. Ask the user for:
   Enter Order Amount:
5. Convert input using float().
6. Continue processing until the user enters the sentinel 0.

Positive Order Amount:
- Represents one valid order.
- Add the actual amount to total_sales.
- Increase order_count by exactly 1.
- Ask for the next Order Amount.

Negative Order Amount:
- Display exactly:
  Invalid Order Amount
- Do not change total_sales.
- Do not increase order_count.
- Continue accepting input so later valid orders can be processed.

Order Amount equal to 0:
- End the session naturally.
- Do not change total_sales or order_count.

After the input loop:
- If order_count is greater than 0, calculate:
  Average Order Value = Total Sales / Total Orders
- If order_count is 0, do not divide.

Display final output exactly as:
Total Orders: X
Total Sales: RMxx.xx

Then display either:
Average Order Value: RMxx.xx

or, when there are no valid orders:
Average Order Value: N/A

Format money values to exactly two decimal places.

Allowed Python:
- print()
- input()
- float()
- variables
- arithmetic and division
- comparison operators
- != if needed
- if / elif / else
- while
- f-string two-decimal formatting

Do not use:
- for loops
- break or continue
- functions
- lists or dictionaries
- try / except
- CSV or JSON
- APIs or databases
- Streamlit

You must personally decide:
- where total_sales and order_count are initialized
- where both are updated
- where repeated input belongs
- where average calculation and zero-count protection belong
- where final output belongs

You must personally write and understand the core implementation.
"""

# TODO: Write your implementation below this line.
print("PurrNest Average Order Value Calculator")
total_sales=0.0
order_count=0
order_amount=float(input("Enter Order Amount:"))
while order_amount!=0:
    if order_amount>0:
        total_sales+=order_amount
        order_count+=1
        order_amount=float(input("Enter Order Amount:"))
    else:
        print("Invalid Order Amount")
        order_amount=float(input("Enter Order Amount:"))

if order_count>0:
    average_order_value=total_sales/order_count
else:
    average_order_value="N/A"

print(f"Total Orders: {order_count}")
print(f"Total Sales: RM{total_sales:.2f}")
if average_order_value!="N/A":
    print(f"Average Order Value: RM{average_order_value:.2f}")
else:
    print("Average Order Value: N/A")