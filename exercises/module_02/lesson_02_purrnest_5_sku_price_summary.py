"""
Module 2 - Lesson 02
PurrNest 5-SKU Price Summary

Write the program personally in the STUDENT CODE AREA below.

Requirements:
- Display: PurrNest 5-SKU Price Summary
- Store these prices in ONE List, in this order:
  12.90, 18.50, 9.90, 22.00, 15.50
- Create a total_price accumulator with an appropriate starting value.
- Use direct List iteration in the form: for element in list
- During every iteration:
  1. Display: Processing Price: RMxx.xx
  2. Add the current price to total_price.
- After all five elements have been processed, calculate:
  Average Product Price = Total Product Prices / 5
- Display:
  Total Product Prices: RMxx.xx
  Average Product Price: RMxx.xx
- Use two decimal places for all displayed prices.

Do not manually process prices[0], prices[1], and so on.
Do not use an index-based loop for the core processing.
Do not use len(), append(), insert(), remove(), pop(), negative indexing,
slicing, enumerate(), range(len(...)), dictionaries, tuples, sets,
nested Lists, functions, classes, CSV, JSON, file handling, try/except,
pandas, databases, or Streamlit.
"""


# STUDENT CODE AREA
print("PurrNest 5-SKU Price Summary")
prices=[12.90, 18.50, 9.90, 22.00, 15.50]
total_price=0.0
for price in prices:
    print(f"Processing Price: RM{price:.2f}")
    total_price+=price

average_price=total_price/5
print(f"Total Product Prices: RM{total_price:.2f}")
print(f"Average Product Price: RM{average_price:.2f}")
