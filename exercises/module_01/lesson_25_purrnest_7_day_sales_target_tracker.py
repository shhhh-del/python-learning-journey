"""
Module 1 - Lesson 25
PurrNest 7-Day Sales Target Tracker

Learning objective:
Use a conditional counter and an accumulator while processing a known number
of records with for + range().

Business scenario:
PurrNest wants to record exactly seven days of sales and determine Total
Sales, Target Days, and Target Hit Rate.

Daily Sales Target:
Daily Sales >= RM20.00

Requirements:
1. Display exactly:
   PurrNest 7-Day Sales Target Tracker
2. Create appropriate starting variables for:
   - Total Sales
   - Target Days
3. Use for + range() to process exactly Day 1 through Day 7.
4. For each day ask exactly:
   Enter Day X Sales:
5. Convert input using float().

Validation:
- Daily Sales >= 0 is valid.
- For a negative value, display exactly:
  Invalid Daily Sales
- Ask again for the same day until the value is valid.
- A negative attempt must not consume a day or update either metric.
- Do not use break or continue.

Valid daily sales processing:
- Add every valid daily value to Total Sales.
- Independently check whether Daily Sales >= 20.00.
- If true, increase Target Days by exactly 1.
- Otherwise Target Days remains unchanged.

After exactly seven valid days:
- Calculate:
  Target Hit Rate = (Target Days / 7) * 100
- Display exactly:
  Total Sales: RMxx.xx
  Target Days: X
  Target Hit Rate: xx.xx%
- Format numeric output to exactly two decimal places.

Allowed Python:
- print(), input(), float()
- variables and arithmetic
- division and multiplication
- comparisons
- if if needed
- while for validation
- for and range()
- f-string two-decimal formatting

Do not use:
- lists, tuples, or dictionaries
- functions
- nested for loops
- break or continue
- enumerate()
- min() or max()
- try / except

You must personally decide:
- how Total Sales and Target Days begin
- which range() gives Day 1 through Day 7
- where same-day validation belongs
- where accumulation and conditional counting belong
- where rate calculation and final output belong
"""

# TODO: Write your implementation below this line.
print("PurrNest 7-Day Sales Target Tracker")
total_sales= 0.0
target_days= 0
for day in range (1,8):
    daily_sales=float(input(f"Enter Day {day} Sales:"))
    while daily_sales<0:
        print("Invalid Daily Sales")
        daily_sales=float(input(f"Enter Day {day} Sales:"))
    
    total_sales+=daily_sales
    if daily_sales>=20:
        target_days+=1

target_hit_rate=(target_days/7)*100
print(f"Total Sales: RM{total_sales:.2f}")
print(f"Target Days: {target_days}")
print(f"Target Hit Rate: {target_hit_rate:.2f}%")
