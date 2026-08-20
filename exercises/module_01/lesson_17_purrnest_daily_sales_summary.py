"""
Module 1 - Lesson 17
PurrNest Daily Sales Summary

Learning objective:
Maintain both an accumulator and a counter inside one while-loop processing
flow.

Business scenario:
The seller enters today's Shopee order amounts and wants to know both the
number of valid orders and the total sales value.

Requirements:
1. Display exactly:
   PurrNest Daily Sales Summary
2. Create total_sales starting at 0.
3. Create order_count starting at 0.
4. Ask the user for:
   Enter Order Amount:
5. Convert the input using float().
6. Continue processing until the user enters 0.
7. For every positive Order Amount:
   - Add the amount to total_sales.
   - Increase order_count by exactly 1.
   - Ask for the next Order Amount.
8. For every negative Order Amount:
   - Display exactly:
     Invalid Order Amount
   - Do not change total_sales.
   - Do not change order_count.
   - Continue asking so later valid orders can be processed.
9. When the user enters 0:
   - Do not add it to total_sales.
   - Do not increase order_count.
   - End the loop naturally.
10. Display the final results exactly as:
    Total Orders: X
    Total Sales: RMxx.xx
11. Format Total Sales to exactly two decimal places.

Allowed Python:
- print()
- input()
- float()
- variables
- arithmetic
- comparisons
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
- where both variables are updated
- where repeated input belongs
- how negative input is excluded from both metrics
- how 0 ends the session

You must personally write and understand the core implementation.
"""

# TODO: Write your implementation below this line.

print("PurrNest Daily Sales Summary")
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
print("Total Orders:", order_count)
print(f"Total Sales: RM{total_sales:.2f}")