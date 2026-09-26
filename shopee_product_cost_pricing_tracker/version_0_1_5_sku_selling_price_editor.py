"""
PurrNest Shopee Product Cost and Pricing Tracker
Version 0.1 - 5-SKU Selling Price Editor

All prices in this exercise are simulated test data.

Write the program personally in the STUDENT CODE AREA below.

Requirements:
- Store exactly these five prices in ONE List:
  12.90, 15.90, 9.90, 18.90, 22.90
- Ask: Select SKU Number (1-5):
- Convert the input with int().
- If the number is outside 1-5, display an invalid message and ask again.
- Convert the valid SKU number to its zero-based List index.
- Display:
  Selected SKU: SKU X
  Current Price: RMxx.xx
- Ask: Enter New Selling Price:
- Convert the input with float().
- If the price is negative, display an invalid message and ask again.
- Zero is valid.
- Replace only the selected List element.
- Display: Updated Price: RMxx.xx
- Format money to two decimal places.

Do not use List iteration, enumerate(), dictionaries, tuples, sets,
functions, CSV, JSON, file handling, databases, APIs, Streamlit, GUI,
classes, product-cost calculations, margin calculations, automatic
recommendations, price history, or persistent storage.
"""


# STUDENT CODE AREA
prices=[12.90,15.90,9.90,18.90,22.90]
sku_numbers=int(input("Select SKU Number (1-5):"))
while sku_numbers<1 or sku_numbers>5:
    print("Invalid SKU Number")
    sku_numbers=int(input("Select SKU Number (1-5):"))
index=sku_numbers-1
print(f"Selected SKU: SKU {sku_numbers}")
print(f"Current Price: RM{prices[index]:.2f}")

new_price=float(input("Enter New Selling Price:"))
while new_price<0:
    print("Invalid Selling Price")
    new_price=float(input("Enter New Selling Price:"))
prices[index]=new_price
print(f"Updated Price: RM{prices[index]:.2f}")

