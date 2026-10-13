"""
Module 2 - Lesson 06
PurrNest Product Record Inspector

Write the program personally in the STUDENT CODE AREA below.

Requirements:
- Display: PurrNest Product Record Inspector
- Create exactly ONE Dictionary:
  sku: PN001
  name: Cat Brush
  price: 15.90
  stock: 20
- Use direct Dictionary key iteration.
- For every key, display:
  Field: <key>
  Value: <corresponding value>
- Retrieve the current value using product[key].
- If the current key is "price", display its value as RMxx.xx.
- Display all other values normally.
- Do not manually write separate Dictionary reads for each field.
- After inspection, use a second key iteration over the same Dictionary.
- Count the fields with a counter initialized before the second loop.
- Display: Total Fields: 4
- Do not use len(product) for the field count.

Do not use .items(), .keys(), .values(), get(), tuple unpacking,
tuples, sets, nested Dictionaries, Lists of Dictionaries, functions,
classes, CSV, JSON, file handling, exceptions, modules, requests,
APIs, pandas, databases, or Streamlit.
"""


# STUDENT CODE AREA
print("PurrNest Product Record Inspector")
product={
    "sku" : "PN004",
    "name" : "Dog Bowl",
    "price" : 20.50,
    "stock" : 15
}
for key in product:
    if key=="price":
        print(f"Field: {key}")
        print(f"Value: RM{product[key]:.2f}")
    else:
        print(f"Field: {key}")
        print(f"Value: {product[key]}")
counter=0
for key in product:
    counter+=1
print(f"Total Fields: {counter}")
        
