# Module 1: Python Foundations Assessment
#
# Scenario:
# Create a small checkout summary for a customer buying several copies
# of one product.
#
# Your program must:
# 1. Ask the user for their name and store it in a variable.
# 2. Ask for the product name and store it as a string.
# 3. Ask for the price of one item. Accept a decimal price and convert the
#    input to a float.
# 4. Ask how many items the customer wants. Accept a whole number and convert
#    the input to an integer.
# 5. Calculate the total cost by multiplying the price by the quantity.
# 6. Display a clear summary using print(). The summary must include the
#    customer's name, product name, quantity, and total cost.
#
# Run the program and test it with at least one set of sensible values.
# Be ready to explain which variables contain strings, floats, and integers,
# and why input used for the calculation must be converted.


# Write your implementation below this line.

customer_name=input("Please enter your name: ")
product_name=input("enter the product name:")
price=float(input("enter price amount:"))
quantity=int(input("how many quantity needed:"))
total_cost=(price*quantity)
print("customer name:",customer_name)
print("product name",product_name)
print("price amount:",price)
print("quantity:",quantity)
print("total cost:",total_cost)
