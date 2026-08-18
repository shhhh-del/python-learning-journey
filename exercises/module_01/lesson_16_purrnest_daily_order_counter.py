"""
Module 1 - Lesson 16
PurrNest Daily Order Counter

Learning objective:
Use a counter variable inside a while loop to count valid business events.

Business scenario:
The seller wants to know how many valid Shopee orders were entered during
the day.

Requirements:
1. Display exactly:
   PurrNest Daily Order Counter
2. Create order_count starting at 0.
3. Ask the user for:
   Enter Order Amount:
4. Convert the input using float().
5. A positive Order Amount represents one valid order:
   - Increase order_count by exactly 1.
   - Ask for the next Order Amount.
6. A negative Order Amount is invalid:
   - Display exactly:
     Invalid Order Amount
   - Do not increase order_count.
   - Ask for the next Order Amount so the session can continue.
7. When the user enters 0, end the input session naturally.
8. Do not count 0 as an order.
9. After the loop ends, display:
   Total Orders: X

Allowed Python:
- print()
- input()
- float()
- variables
- arithmetic
- comparisons
- if / elif / else
- while

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
- where order_count is initialized
- where the counter increases
- where repeated input belongs
- how invalid input is excluded while the session continues
- how entering 0 ends the session

You must personally write and understand the core implementation.
"""

# TODO: Write your implementation below this line.

print("PurrNest Daily Order Counter")
order_count=0
order_amount=float(input("Enter Order Amount:"))
while order_amount!=0:
   if order_amount>0:
      order_count+=1
      order_amount=float(input("Enter Order Amount:"))
   else:
      print("Invalid Order Amount")
      order_amount=float(input("Enter Order Amount:"))
print("Total Orders:", order_count)