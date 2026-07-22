# Module 1 - Lesson 04: Shopee Seller Discount Eligibility Checker
#
# Business problem:
# Decide a seller's discount based on VIP status and order amount.
# The order amount should be requested only when the customer is a VIP.
#
# Inputs:
# 1. Ask whether the customer is a VIP: yes or no.
# 2. If the answer is yes, ask for the order amount in RM and convert it
#    to a suitable numeric type.
#
# Required decision:
# - If VIP is yes:
#     - If order amount is at least RM100, print: VIP Discount: 20%
#     - Otherwise, print: VIP Discount: 10%
# - Otherwise, print: No Discount
#
# Acceptance criteria:
# - You personally write the program's core logic.
# - The program uses an outer if/else and a nested if/else.
# - A non-VIP customer is not asked for an order amount.
# - The output text matches the required result exactly.
# - The boundary value RM100 is handled correctly.
# - The code is readable and contains no unnecessary duplicated decisions.
#
# Manual tests required:
# - VIP=no -> No Discount
# - VIP=yes, RM99 -> VIP Discount: 10%
# - VIP=yes, RM100 -> VIP Discount: 20%
# - VIP=yes, RM500 -> VIP Discount: 20%
# - One additional test chosen by you


# Write your implementation below this line.

VIP_confirmation=input("are you a VIP(yes/no): ")
if VIP_confirmation=="yes":
    order_amount=float(input("pls enter your order amount(RM): "))
    if order_amount>=100:
        print("VIP Discount: 20%")
    else:
        print("VIP Discount: 10%")
else:
    print("No Discount")
    