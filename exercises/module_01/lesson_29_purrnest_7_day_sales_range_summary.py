"""
Module 1 - Lesson 29
PurrNest 7-Day Sales Range Summary

Learning objective:
Calculate a derived spread from tracked maximum and minimum associated states.

Business scenario:
PurrNest wants to record exactly seven valid daily sales values and report the
best day, highest sales, worst day, lowest sales, and sales spread.

Requirements:
1. Display exactly:
   PurrNest 7-Day Sales Range Summary
2. Use for + range() to process exactly Day 1 through Day 7.
3. For each day ask exactly:
   Enter Day X Sales:
4. Convert input using float().

Validation:
- Daily Sales >= 0 is valid.
- For negative input, display exactly:
  Invalid Daily Sales
- Ask again for the same day until the value is valid.
- Negative attempts must consume no day and change none of the tracked states.
- Do not use break or continue.

Tracked states:
- The first valid day establishes:
  highest_sales
  best_day
  lowest_sales
  worst_day
- Later strict maximums update Highest Sales and Best Day together.
- Later strict minimums update Lowest Sales and Worst Day together.
- Equal values preserve the earliest associated day.

Derived metric:
- After exactly seven valid days, calculate:
  Sales Spread = Highest Daily Sales - Lowest Daily Sales

Final output:
Best Sales Day: Day X
Highest Daily Sales: RMxx.xx
Worst Sales Day: Day X
Lowest Daily Sales: RMxx.xx
Sales Spread: RMxx.xx

Format every money value to exactly two decimal places.

Allowed Python:
- print(), input(), float()
- variables, arithmetic, and comparison operators
- if / elif / else if genuinely needed
- while for validation
- for and range()
- f-string and .2f formatting

Do not use:
- lists, tuples, or dictionaries
- functions
- nested for loops
- enumerate()
- min(), max(), or abs()
- break or continue
- None
- try / except

You must personally decide:
- the correct range()
- how the first valid day establishes all four states
- how and where both associated pairs update
- how strict comparisons preserve the earliest days
- where Sales Spread should be calculated
- where final output belongs
"""

# TODO: Write your implementation below this line.
print("PurrNest 7-Day Sales Range Summary")
daily_sales=0
worst_day=0
best_day=0
lowest_sales=0
highest_sales=0
for day in range(1,8):
    daily_sales=float(input(f"Enter Day {day} Sales:"))
    while daily_sales<0:
        print("Invalid Daily Sales")
        daily_sales=float(input(f"Enter Day {day} Sales:"))
    if daily_sales<lowest_sales or day==1:
        lowest_sales=daily_sales
        worst_day=day
    if daily_sales>highest_sales or day==1:
        highest_sales=daily_sales
        best_day=day

sales_spread = highest_sales - lowest_sales

print(f"Best Sales Day: Day {best_day}")
print(f"Highest Daily Sales: RM{highest_sales:.2f}")
print(f"Worst Sales Day: Day {worst_day}")
print(f"Lowest Daily Sales: RM{lowest_sales:.2f}")
print(f"Sales Spread: RM{sales_spread:.2f}")
