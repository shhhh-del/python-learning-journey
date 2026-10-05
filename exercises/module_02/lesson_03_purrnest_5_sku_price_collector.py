"""
Module 2 - Lesson 03
PurrNest 5-SKU Price Collector

Write the program personally in the STUDENT CODE AREA below.

Requirements:
- Display: PurrNest 5-SKU Price Collector
- Start with ONE empty List for prices.
- Use for + range() to process SKU 1 through SKU 5.
- For each SKU ask: Enter SKU X Price:
- Convert input with float().
- Prices greater than or equal to zero are valid.
- For every negative price, display: Invalid Price
- Keep asking for the SAME SKU until the price is valid.
- Append only the final valid price for each SKU.
- Exactly five valid prices must be stored after collection.
- After collection, use direct List iteration.
- During iteration display: Stored Price: RMxx.xx
- Use an accumulator to calculate Total Product Prices.
- After iteration calculate Average Product Price = Total / 5.
- Display:
  Total Product Prices: RMxx.xx
  Average Product Price: RMxx.xx
- Use two decimal places for money.

Do not hard-code the final List or assign prices by index.
Do not use len(), insert(), remove(), pop(), slicing, negative indexing,
enumerate(), range(len(...)), dictionaries, tuples, sets, functions,
classes, CSV, JSON, file handling, exceptions, APIs, pandas, or Streamlit.
"""


# STUDENT CODE AREA

print("PurrNest 5-SKU Price Collector")
prices=[]
for sku in range(1,6):
    price=float(input(f"Enter SKU {sku} Price:"))
    while price<0:
        print("Invalid Price")
        price=float(input(f"Enter SKU {sku} Price:"))
    prices.append(price)

total_price=0.0

for price in prices:
    print(f"Stored Price: RM{price:.2f}")
    total_price+=price
average_price=total_price/5
print(f"Total Product Prices: RM{total_price:.2f}")
print(f"Average Product Price: RM{average_price:.2f}")
