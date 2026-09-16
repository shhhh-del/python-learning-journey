"""
Module 1 - Lesson 28
PurrNest 7-Day Best & Worst Sales Tracker

Learning objective:
Track maximum and minimum associated-state pairs together in one fixed loop.

Business scenario:
PurrNest wants to record exactly seven days of valid sales and identify the
best sales day, highest daily sales, worst sales day, and lowest daily sales.

Requirements:
1. Display exactly:
   PurrNest 7-Day Best & Worst Sales Tracker
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

First valid day:
- Establish all four states:
  highest_sales
  best_day
  lowest_sales
  worst_day

Later valid days:
- If Daily Sales is strictly greater than Highest Sales, update both the
  maximum value and its associated day.
- Independently, if Daily Sales is strictly lower than Lowest Sales, update
  both the minimum value and its associated day.
- A middle value updates neither pair.

Tie rule:
- The earliest day wins for both maximum and minimum.
- Equal values must not replace either associated day.

After exactly seven valid days, display exactly:
Best Sales Day: Day X
Highest Daily Sales: RMxx.xx
Worst Sales Day: Day X
Lowest Daily Sales: RMxx.xx

Format money to exactly two decimal places.

Allowed Python:
- print(), input(), float()
- variables and comparison operators
- if / elif / else if genuinely needed
- while for validation
- for and range()
- f-string and .2f formatting

Do not use:
- lists, tuples, or dictionaries
- functions
- nested for loops
- enumerate()
- min() or max()
- break or continue
- None
- try / except

You must personally decide:
- the correct range()
- how the first valid day establishes all four states
- the maximum and minimum comparisons
- why the two comparisons are independent
- where each associated pair updates together
- how equality preserves the earlier days
- where validation and final output belong
"""

# TODO: Write your implementation below this line.
print("PurrNest 7-Day Best & Worst Sales Tracker")
daily_sales=0
worst_day=0
lowest_sales=0
best_day=0
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


print(f"Best Sales Day: Day {best_day}")
print(f"Highest Daily Sales: RM{highest_sales:.2f}")
print(f"Worst Sales Day: Day {worst_day}")
print(f"Lowest Daily Sales: RM{lowest_sales:.2f}")