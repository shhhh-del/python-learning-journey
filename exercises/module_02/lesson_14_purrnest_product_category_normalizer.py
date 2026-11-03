"""
Module 2 - Lesson 14
PurrNest Product Category Normalizer
Date: 2026-11-04 | Tracker: JR-19

Write the implementation personally below.
Only major new concept: string normalization with strip() and lower().

Business problem:
Accept brush, bowl, or toy despite mixed case or surrounding whitespace.
Do not remove internal spaces or accept additional categories.

Function:
- Define normalize_category with exactly one parameter: category.
- Create a local variable containing category.strip().lower().
- Return the normalized string; do not print inside the function.
- Original raw text is not automatically changed by these operations.

Main program:
- Display exactly: PurrNest Product Category Normalizer
- Ask: Enter Product Category:
- Store raw input, pass it to the function and store returned normalized text.
- Compare normalized text, not raw input.
- Only brush, bowl, toy are valid.
- Use already learned comparisons/logical operators and while validation;
  do not introduce List membership or another new membership technique.
- For invalid normalized text display exactly: Invalid Category
- Ask for fresh input and normalize again on every retry.
- Continue until a valid category is supplied.
- After validation display exactly:
  Normalized Category: <normalized category>

FIRST STEP ONLY:
Write the function definition, local normalized variable and return.
Do not add input handling or the validation loop yet. Wait for review.

Allowed: input, variables, strings, if/elif/else, while validation,
previously learned logical comparisons, functions, one parameter, return,
local variables and f-strings.
Do not introduce split(), replace(), startswith(), endswith(), find(),
slicing, regular expressions, tuples, sets, files, CSV, JSON, exceptions,
modules, requests, HTTP, APIs, classes, pandas, databases, or Streamlit.

Seven manual tests after pre-run review:
1. brush -> Normalized Category: brush.
2. BRUSH -> Normalized Category: brush.
3. Leading/trailing spaces around bowl -> normalized bowl.
4. Surrounding spaces and mixed-case ToY -> normalized toy.
5. food rejected, then BOWL accepted -> final bowl.
6. cat brush rejected; explain why internal space remains, then enter a
   valid category to finish the retry loop.
7. Design an input sequence with at least one invalid entry followed by a
   valid category with mixed case or surrounding spaces. BEFORE running,
   predict each normalized value, rejected/accepted status and final output.
"""

# STUDENT CODE AREA
def normalize_category(category):
    normalized = category.strip().lower()
    return normalized
print("PurrNest Product Category Normalizer")
product_category = input("Enter Product Category: ")
normalized_category = normalize_category(product_category)
while normalized_category != "brush" and normalized_category != "bowl" and normalized_category != "toy":
    print("Invalid Category")
    product_category = input("Enter Product Category: ")
    normalized_category = normalize_category(product_category)
    
print(f"Normalized Category: {normalized_category}")

