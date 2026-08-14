"""
Module 1 - Friday Review #3
PurrNest Restock Quantity Validator

Business problem:
PurrNest needs to record how many units should be reordered.

Business rule:
A restock quantity is valid only when it is greater than 0.
Therefore, 0 and negative quantities are invalid.

Requirements:
1. Display exactly:
   PurrNest Restock Quantity Validator
2. Ask the user for:
   Enter Restock Quantity:
3. Convert the input using int().
4. While the quantity is invalid:
   - Display exactly:
     Invalid Quantity
   - Ask for the restock quantity again.
   - Store the new input in the controlling variable.
5. Stop the loop naturally when the quantity is valid.
6. Display the accepted value in this format:
   Restock Quantity Accepted: X

Allowed Python:
- print()
- input()
- int()
- variables
- comparisons
- if, if needed
- while

Do not use:
- break or continue
- for loops
- functions
- lists or dictionaries
- try / except
- CSV or JSON
- APIs or databases
- Streamlit

Derive the while condition yourself from the business rule.
You must personally write and understand the core implementation.
"""

# TODO: Write your implementation below this line.

print("PurrNest Restock Quantity Validator")
restock_quantity=int(input("Enter Restock Quantity:"))
while restock_quantity<=0:
    print("Invalid Quantity")
    restock_quantity=int(input("Enter Restock Quantity:"))
 
print("Restock Quantity Accepted:", restock_quantity)