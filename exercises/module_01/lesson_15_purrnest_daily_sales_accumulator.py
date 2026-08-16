"""
Module 1 - Lesson 15
PurrNest Daily Sales Accumulator

Learning objective:
Use an accumulator variable to maintain a running total across repeated
while-loop iterations.

Business scenario:
The seller manually enters today's Shopee order amounts and wants to see the
total sales amount.

Requirements:
1. Display exactly:
   PurrNest Daily Sales Accumulator
2. Create a Total Sales variable that begins at zero.
3. Ask the user for:
   Enter Order Amount:
4. Convert the input using float().
5. While the Order Amount is positive:
   - Add the Order Amount to Total Sales.
   - Ask for the next Order Amount.
6. When the user enters 0, stop the loop naturally.
7. Display the final total exactly in this format:
   Total Sales: RMxx.xx
8. Format Total Sales to exactly two decimal places.

Negative input:
- A negative Order Amount is invalid.
- Display exactly:
  Invalid Order Amount
- Do not add a negative amount to Total Sales.
- Do not build a complicated nested validation system.

Allowed Python:
- print()
- input()
- float()
- variables
- arithmetic
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
- CSV or JSON
- APIs or databases
- Streamlit

You must personally decide:
- where Total Sales is initialized
- where each positive amount is added
- where the next input belongs
- how zero terminates the loop

You must personally write and understand the core implementation.
"""

# TODO: Write your implementation below this line.

print("PurrNest Daily Sales Accumulator")
total_sales=0.0
order_amount=float(input("Enter Order Amount:"))
while order_amount>0:
    total_sales+=order_amount
    order_amount=float(input("Enter Order Amount:"))
if order_amount<0:
   print("Invalid Order Amount")
print(f"Total Sales: RM{total_sales:.2f}")
