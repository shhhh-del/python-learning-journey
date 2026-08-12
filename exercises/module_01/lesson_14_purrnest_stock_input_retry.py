"""
Module 1 - Lesson 14
PurrNest Stock Input Retry

Learning objective:
Use a while loop to repeatedly request input until the user enters a valid
business value.

Business rule:
A valid current stock quantity must be 0 or greater.

Requirements:
1. Display exactly:
   PurrNest Stock Input Retry
2. Ask the user for:
   Enter Current Stock Quantity
3. Convert the entered value using int().
4. While the stock quantity is negative:
   - Display exactly:
     Invalid Stock
   - Ask for the current stock quantity again.
   - Store the new value so the while condition can check it again.
5. Once the stock quantity is 0 or greater, stop repeating.
6. Display the accepted value in this format:
   Valid Stock: X

Expected behavior:
If the user enters -3, then -1, then 5, the program should:
- display Invalid Stock after -3
- ask again
- display Invalid Stock after -1
- ask again
- stop repeating after 5
- display Valid Stock: 5

Allowed Python:
- print()
- input()
- int()
- variables
- comparison operators
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

You must personally write and understand the core implementation.
"""

# TODO: Write your implementation below this line.

print("PurrNest Stock Input Retry")
stock_quantity=int(input("Enter Current Stock Quantity:"))
while stock_quantity<0:
    print("Invalid Stock")
    stock_quantity=int(input("Enter Current Stock Quantity:"))
print("Valid Stock:", stock_quantity)