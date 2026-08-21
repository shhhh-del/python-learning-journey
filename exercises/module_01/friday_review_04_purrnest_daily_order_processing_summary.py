"""
Module 1 - Friday Review #4
PurrNest Daily Order Processing Summary

Business scenario:
The seller enters order amounts and wants to track:
- the number of valid orders
- the number of invalid negative entries
- total sales from valid orders

Requirements:
1. Display exactly:
   PurrNest Daily Order Processing Summary
2. Before processing, create variables representing:
   - Total Sales
   - Valid Order Count
   - Invalid Entry Count
3. Ask the user for:
   Enter Order Amount:
4. Convert input using float().
5. Continue processing until the user enters the sentinel 0.

Positive Order Amount:
- Represents one valid order.
- Increase Valid Order Count by exactly 1.
- Add the actual amount to Total Sales.
- Do not increase Invalid Entry Count.

Negative Order Amount:
- Represents one invalid entry.
- Display exactly:
  Invalid Order Amount
- Increase Invalid Entry Count by exactly 1.
- Do not increase Valid Order Count.
- Do not change Total Sales.
- Continue accepting input afterward.

Order Amount equal to 0:
- End the session naturally.
- Do not change any metric.

After processing, display exactly:
Valid Orders: X
Invalid Entries: X
Total Sales: RMxx.xx

Format Total Sales to exactly two decimal places.

Allowed Python:
- print()
- input()
- float()
- variables
- arithmetic
- comparison operators
- !=
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
- where all three metrics are initialized
- which branch changes each metric
- where repeated input belongs
- how 0 ends processing
- where final output belongs

You must personally write and understand the core implementation.
"""

# TODO: Write your implementation below this line.

print("PurrNest Daily Order Processing Summary")
total_sales=0.0
valid_order_count=0
invalid_entry_count=0
order_amount=float(input("Enter Order Amount:"))
while order_amount!=0:
    if order_amount>0:
        valid_order_count+=1
        total_sales+=order_amount
        order_amount=float(input("Enter Order Amount:"))
    else:
         print("Invalid Order Amount")
         invalid_entry_count+=1
         order_amount=float(input("Enter Order Amount:"))

print(f"Valid Orders: {valid_order_count}")
print(f"Invalid Entries: {invalid_entry_count}")
print(f"Total Sales: RM{total_sales:.2f}")
