"""
Module 2 - Lesson 04
PurrNest Dynamic SKU Price Summary

Write the program personally in the STUDENT CODE AREA below.

Requirements:
- Display: PurrNest Dynamic SKU Price Summary
- Ask: How Many SKUs:
- Convert the input with int().
- Valid SKU count is 1 through 5 inclusive.
- For every invalid count, display: Invalid SKU Count
- Keep asking until the count is valid.
- Start with ONE empty List.
- Use for + range() to collect exactly the requested number of prices.
- For each SKU ask: Enter SKU X Price:
- Convert the input with float().
- For every negative price, display: Invalid Price
- Keep asking for the SAME SKU until the price is valid.
- Append only the final valid price for each SKU.
- After collection, display the actual List size using:
  Stored SKU Count: X
- Stored SKU Count must come from len(the_list), not the input variable.
- Use direct List iteration to display each stored price and accumulate Total.
- Display each element as: Stored Price: RMxx.xx
- Calculate Average after iteration using Total / len(the_list).
- Display:
  Total Product Prices: RMxx.xx
  Average Product Price: RMxx.xx
- Use two decimal places for money.

Do not use range(len(...)), insert(), remove(), pop(), slicing,
negative indexing, enumerate(), dictionaries, tuples, sets, functions,
classes, CSV, JSON, files, exceptions, requests, pandas, databases,
or Streamlit.
"""


# STUDENT CODE AREA

print("PurrNest Dynamic SKU Price Summary")
prices=[]

SKU_count=int(input("How Many SKUs:"))
while SKU_count<1 or SKU_count>5:
    print("Invalid SKU Count")
    SKU_count=int(input("How Many SKUs:"))
for sku in range(1,SKU_count+1):
    price_input=float(input(f"Enter SKU {sku} Price:"))
    while price_input<0:
        print("Invalid Price")
        price_input=float(input(f"Enter SKU {sku} Price:"))
    prices.append(price_input)
total_price=0.0

for price in prices:
    print(f"Stored Price: RM{price:.2f}")
    total_price+=price
average_price=total_price/len(prices)
print(f"Stored SKU Count: {len(prices)}")
print(f"Total Product Prices: RM{total_price:.2f}")
print(f"Average Product Price: RM{average_price:.2f}")        