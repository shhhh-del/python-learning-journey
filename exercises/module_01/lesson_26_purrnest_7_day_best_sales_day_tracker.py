"""
Module 1 - Lesson 26
PurrNest 7-Day Best Sales Day Tracker

Learning objective:
Track a highest value together with the label associated with that value.

Business scenario:
PurrNest wants to record exactly seven days of sales and determine which day
had the highest sales and what that sales amount was.

Requirements:
1. Display exactly:
   PurrNest 7-Day Best Sales Day Tracker
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

Best-day tracking:
- The first valid day establishes both Highest Sales and Best Day.
- For later valid days, compare Daily Sales with Highest Sales.
- If the new value is strictly greater, update both tracked states together.
- If the new value is equal or lower, keep both states unchanged.

Tie rule:
- The earliest day wins.
- Equal sales must not replace the existing Best Day.

After exactly seven valid days, display exactly:
Best Sales Day: Day X
Highest Daily Sales: RMxx.xx

Format money to exactly two decimal places.

Allowed Python:
- print(), input(), float()
- variables and comparisons
- if / else if genuinely needed
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
- how Highest Sales and Best Day begin
- how the first valid day establishes both states
- where both states update together
- how equality preserves the earlier day
- where validation and final output belong
"""

# TODO: Write your implementation below this line.

print("PurrNest 7-Day Best Sales Day Tracker")
highest_sales=0.0
best_day=0
for day in range(1,8):
    daily_sales=float(input(f"Enter Day {day} Sales:"))
    while daily_sales<0:
        print("Invalid Daily Sales")
        daily_sales=float(input(f"Enter Day {day} Sales:"))
    if daily_sales>highest_sales or day ==1:
        highest_sales=daily_sales
        best_day=day

print(f"Best Sales Day: Day {best_day}")
print(f"Highest Daily Sales: RM{highest_sales:.2f}")