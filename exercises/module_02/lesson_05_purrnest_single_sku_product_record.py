"""
Module 2 - Lesson 05
PurrNest Single SKU Product Record

Write the program personally in the STUDENT CODE AREA below.

Requirements:
- Create exactly ONE Dictionary representing one product.
- Store exactly these four fields and values:
  sku: PN001
  name: Cat Brush
  price: 15.90
  stock: 20
- Read every value from the Dictionary using its key.
- Display exactly:
  SKU: PN001
  Product Name: Cat Brush
  Price: RM15.90
  Stock: 20
- Ask: Enter New Price:
- Convert input with float().
- For every negative price, display: Invalid Price
- Retry until the price is valid; zero is valid.
- Replace only the Dictionary's price value using its key.
- Display: Updated Price: RMxx.xx
- Ask: Enter New Stock:
- Convert input with int().
- For every negative stock value, display: Invalid Stock
- Retry until stock is valid; zero is valid.
- Replace only the Dictionary's stock value using its key.
- Display: Updated Stock: X
- Display the final four fields again using Dictionary keys.
- SKU and name must remain unchanged.

Do not hard-code the displayed business values separately.
Do not use Dictionary iteration, .keys(), .values(), .items(), get(),
nested Dictionaries, Lists of Dictionaries, tuples, sets, functions,
classes, CSV, JSON, file handling, exceptions, modules, requests, APIs,
pandas, databases, or Streamlit.
"""


# STUDENT CODE AREA
product = {
    "sku" : "PN001",
    "name" : "Cat Brush",
    "price" : 15.90,
    "stock" : 20
}

print(f"SKU: {product['sku']}")
print(f"Product Name: {product['name']}")
print(f"Price: RM{product['price']:.2f}") 
print(f"Stock: {product['stock']}")

new_price=float(input(f"Enter New Price:"))
while new_price<0:
    print("Invalid Price")
    new_price=float(input(f"Enter New Price:"))
product["price"]=new_price
print(f"Updated Price: RM{product['price']:.2f}")

new_stock=int(input(f"Enter New Stock: "))
while new_stock<0:
    print("Invalid Stock")
    new_stock=int(input(f"Enter New Stock: "))
product["stock"]=new_stock
print(f"Updated Stock: {product['stock']}")

print(f"SKU: {product['sku']}")
print(f"Product Name: {product['name']}")
print(f"Price: RM{product['price']:.2f}")
print(f"Stock: {product['stock']}")