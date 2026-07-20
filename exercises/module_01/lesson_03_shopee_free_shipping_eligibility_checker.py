# Module 1 — Lesson 03: Shopee Free Shipping Eligibility Checker
#
# Business problem:
# Decide whether an order receives free shipping based on its amount,
# delivery region, and VIP status.
#
# Part A — Basic eligibility
#
# Your program must:
# 1. Display this title:
#    Shopee Free Shipping Eligibility Checker
# 2. Ask for the order amount in RM and convert it to a suitable numeric type.
# 3. Ask for the region: West or East.
# 4. Use a comparison and the `and` operator to apply this rule:
#    - Free Shipping when the order amount is at least RM40 AND the region is West.
#    - Otherwise, Standard Shipping.
# 5. Print the shipping result clearly.
#
# Part B — VIP extension
#
# After Part A works:
# 1. Ask whether the customer is a VIP: yes or no.
# 2. Extend the decision using `or` so that VIP customers always receive
#    Free Shipping.
# 3. The complete business rule is:
#    - Free Shipping when (order amount is at least RM40 AND region is West)
#      OR the customer is a VIP.
#    - Otherwise, Standard Shipping.
#
# Acceptance criteria:
# - The title, inputs, and shipping result are displayed clearly.
# - The program uses comparisons and logical operators.
# - Both Free Shipping and Standard Shipping branches are reachable.
# - Boundary value RM40 is handled correctly.
# - You personally write and understand the core logic.
#
# Manual tests required after completing Part B:
# - RM39, West, VIP=no -> Standard Shipping
# - RM40, West, VIP=no -> Free Shipping
# - RM100, East, VIP=no -> Standard Shipping
# - RM20, West, VIP=yes -> Free Shipping
# - RM100, East, VIP=yes -> Free Shipping
# - Test one additional case of your own choice.


# Write your implementation below this line.

print("Shopee Free Shipping Eligibility Checker")
order_amount=(float(input("please enter your order amount(RM):")))
region=input("enter your region(west/east):")

vip_confirmation=input("are you vip(yes/no):")
if order_amount >=40 and region=="west" or vip_confirmation=="yes":
    print("free shipping")
else:
    print("standard shipping")