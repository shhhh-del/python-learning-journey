"""
Module 2 - Lesson 07
PurrNest Required Product Field Checker

Business problem:
Check whether one product record contains every required field.
Membership checks keys; read a value only after confirming its key exists.

Write the program personally in the STUDENT CODE AREA.

Requirements:
1. Display exactly: PurrNest Required Product Field Checker
2. Create one required_fields List in this order:
   sku, name, price, stock
3. Create exactly one product Dictionary with initial data:
   sku: PN001
   name: Cat Brush
   price: 15.90
   stock: 20
4. Initialize present_count and missing_count before processing.
5. Iterate directly through required_fields; do not write four separate checks.
6. Use field in product to check each expected key.
7. For a present field, display exactly:
   Field <field>: PRESENT
   Value: <stored value>
   Retrieve its value using product[field].
   For price only, display Value: RMxx.xx with two decimal places.
   Increase only the present counter.
8. For a missing field, display exactly:
   Field <field>: MISSING
   Increase only the missing counter; do not read product[field].
9. After all processing, display exactly:
   Required Fields: <number of required fields>
   Present Fields: <present count>
   Missing Fields: <missing count>
   You may use len(required_fields).

You determine counter initial values, indentation, safe value-read placement,
price-formatting placement, counter updates, and summary placement.

Allowed: Lists, direct List iteration, Dictionary literals, keys/values,
key-based reading, for, if/else, counters, +=, print, f-strings, .2f, len.
New concept: Dictionary key membership using in.
Do not use not in for the main solution, get(), keys(), values(), items(),
tuple unpacking, tuples, sets, nested Dictionaries, Lists of Dictionaries,
functions, classes, CSV, JSON, file handling, exceptions, modules, requests,
HTTP, APIs, pandas, databases, or Streamlit.

Manual tests (after Codex reviews your implementation):
1. Complete original record: required 4, present 4, missing 0.
2. Remove stock only: stock MISSING, present 3, missing 1.
3. Restore stock and remove price only: price MISSING, present 3, missing 1;
   no attempt to read the missing price value.
4. Keep only sku and name: present 2, missing 2.
5. Use sku value 'price', name 'Cat Brush', stock 20, with no price key.
   Predict membership before running, then verify price is MISSING.
6. Design one record with 1-4 required keys. Before running, predict each
   field's status and both counts, then compare with actual output.
Change only product data during tests; keep required_fields and logic unchanged.
"""

# STUDENT CODE AREA
print("PurrNest Required Product Field Checker")
required_fields= ["sku","name","price","stock"]
product={
    "sku" : "PN005",
    "name" : "Cat Bowl",
    "price" : 12.90,
    "stock" : 2
}
required_count=len(required_fields)
present_count=0
missing_count=0
for field in required_fields:
    if field in product:
        print(f"Field {field}: PRESENT")
        if field=="price":
            print(f"Value: RM{product[field]:.2f}")
        else:
            print(f"Value: {product[field]}")
        present_count += 1
    else:
        print(f"Field {field}: MISSING")
        missing_count += 1

print(f"Required Fields: {required_count}")
print(f"Present Fields: {present_count}")
print(f"Missing Fields: {missing_count}")