# Module 1 - Lesson 05: Shopee Product Stock Status Checker
#
# Business problem:
# Help a Shopee seller quickly classify a product's current stock level.
#
# Input:
# - Ask for the current stock quantity.
# - Convert the input into an integer.
#
# Required classification:
# - Stock equal to 0 -> Out of Stock
# - Stock at most 5 -> Low Stock
# - Stock at most 20 -> Normal Stock
# - Any other value -> High Stock
#
# Required output text:
# - Out of Stock
# - Low Stock
# - Normal Stock
# - High Stock
#
# Acceptance criteria:
# - You personally write the program's core logic.
# - Use one ordered if / elif / elif / else decision chain.
# - Check the special zero case before the wider ranges.
# - Convert the entered quantity using int().
# - Use correct indentation and readable variable naming.
# - Avoid unnecessary or duplicated conditions.
# - Each input prints exactly one stock status.
#
# Manual tests required:
# - 0 -> Out of Stock
# - 1 -> Low Stock
# - 5 -> Low Stock
# - 6 -> Normal Stock
# - 20 -> Normal Stock
# - 21 -> High Stock
# - One additional value chosen by you


# Write your implementation below this line.

stock_amount=int(input("please enter your stock amount:"))
if stock_amount==0:
    print("Out of Stock")
elif stock_amount<=5:
    print("Low Stock")
elif stock_amount<=20:
    print("Normal Stock")
else:
    print("High Stock")