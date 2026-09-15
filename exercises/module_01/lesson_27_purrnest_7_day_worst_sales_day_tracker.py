"""
Module 1 - Lesson 27
PurrNest 7-Day Worst Sales Day Tracker

Learning objective:
Track a lowest value together with the label associated with that value.

Business scenario:
PurrNest wants to record exactly seven days of valid sales and determine which
day had the lowest sales and what that sales amount was.

Requirements:
1. Display exactly:
   PurrNest 7-Day Worst Sales Day Tracker
2. Use for + range() to process exactly Day 1 through Day 7.
3. For each day ask exactly:
   Enter Day X Sales:
4. Convert input using float().

Validation:
- Daily Sales >= 0 is valid.
- For negative input, display exactly:
  Invalid Daily Sales
- Ask again for the same day until the value is valid.
- Negative attempts must consume no day and change neither tracked state.
- Do not use break or continue.

Worst-day tracking:
- The first valid day establishes both Lowest Sales and Worst Day.
- For later valid days, compare Daily Sales with Lowest Sales.
- If the new value is strictly lower, update both tracked states together.
- If the new value is equal or higher, keep both states unchanged.

Tie rule:
- The earliest day wins.
- Equal sales must not replace the existing Worst Day.

After exactly seven valid days, display exactly:
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
- how Lowest Sales and Worst Day begin
- how the first valid day establishes both states
- where both states update together
- how equality preserves the earlier day
- where validation and final output belong
"""

# TODO: Write your implementation below this line.
print("PurrNest 7-Day Worst Sales Day Tracker")
daily_sales=0
lowest_sales=0
worst_day=0
for day in range(1,8):
    daily_sales=float(input(f"Enter Day {day} Sales:"))
    while daily_sales<0:
        print("Invalid Daily Sales")
        daily_sales=float(input(f"Enter Day {day} Sales:"))
    if daily_sales<lowest_sales or day==1:
        lowest_sales=daily_sales
        worst_day=day

print(f"Worst Sales Day: Day {worst_day}")
print(f"Lowest Daily Sales: RM{lowest_sales:.2f}")
