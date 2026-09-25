"""
Module 2 - Lesson 01
PurrNest 5-SKU Price Editor

Write the program personally in the STUDENT CODE AREA below.

Requirements:
- Display: PurrNest 5-SKU Price Editor
- Store these five prices in ONE List, in SKU order:
  SKU 1 = RM12.90
  SKU 2 = RM18.50
  SKU 3 = RM9.90
  SKU 4 = RM22.00
  SKU 5 = RM15.50
- Read and display SKU 1, SKU 3, and SKU 5 using List indexes.
- Ask: Enter New Price for SKU 3:
- Convert the input with float().
- A price greater than or equal to zero is valid.
- For every negative price, display: Invalid Price
- Keep asking until the price is valid.
- Replace only the SKU 3 element using its index.
- Display the updated SKU 3 price.
- Display SKU 1 and SKU 5 again to verify they did not change.
- Format every displayed price to two decimal places.

Do not use append(), insert(), remove(), pop(), len(), negative indexing,
slicing, List methods, iteration through the List, nested Lists, tuples,
dictionaries, sets, functions, classes, CSV, JSON, APIs, pandas,
databases, or Streamlit.
"""


# STUDENT CODE AREA
print("PurrNest 5-SKU Price Editor")
SKU=[12.90,18.50,9.90,22.00,15.50]
print(f"SKU 1 Price: RM{SKU[0]:.2f}")
print(f"SKU 3 Price: RM{SKU[2]:.2f}")
print(f"SKU 5 Price: RM{SKU[4]:.2f}")
new_price=float(input("Enter New Price for SKU 3:"))
while new_price<0:
    print("Invalid Price")
    new_price=float(input("Enter New Price for SKU 3:"))
SKU[2]=new_price
print(f"Updated SKU 3 Price: RM{SKU[2]:.2f}")
print(f"SKU 1 Price: RM{SKU[0]:.2f}")
print(f"SKU 5 Price: RM{SKU[4]:.2f}")


