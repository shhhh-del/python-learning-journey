"""
Friday Review #7
PurrNest 7-Day Sales Extremes Report

Objective:
Combine fixed seven-day processing, same-day negative validation, associated
maximum/minimum tracking, earliest-wins ties, and a post-loop Sales Spread.

Business scenario:
PurrNest wants a seven-day report showing the best and worst sales days, their
sales values, and the numerical spread between the two values.

Requirements:
1. Display exactly:
   PurrNest 7-Day Sales Extremes Report
2. Process exactly Day 1 through Day 7 using for + range().
3. For every day ask exactly:
   Enter Day X Sales:
4. Convert input using float().

Validation:
- Daily Sales >= 0 is valid.
- If Daily Sales is negative, display exactly:
  Invalid Daily Sales
- Ask again for the same day.
- Invalid attempts must consume no day and change no tracked state.
- Do not use break or continue.

State tracking:
- The first valid day establishes:
  highest_sales
  best_day
  lowest_sales
  worst_day
- A later strict maximum updates Highest Sales and Best Day together.
- A later strict minimum updates Lowest Sales and Worst Day together.
- Maximum and minimum checks must remain logically independent.

Tie rule:
- Earliest day wins for both extremes.
- Equal values must not replace Best Day or Worst Day.

Derived metric:
- After all seven valid days, calculate:
  sales_spread = highest_sales - lowest_sales

Final output:
Best Sales Day: Day X
Highest Daily Sales: RMxx.xx
Worst Sales Day: Day X
Lowest Daily Sales: RMxx.xx
Sales Spread: RMxx.xx

Allowed Python:
- print(), input(), float()
- variables, subtraction, and comparisons
- if / elif / else
- while, for, and range()
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
- first-day initialization
- maximum and minimum comparisons
- associated-state synchronization
- tie handling
- negative retry behavior
- where Sales Spread and final output belong
"""

# TODO: Write your implementation below this line.
print("PurrNest 7-Day Sales Extremes Report")
worst_day=0
best_day=0
highest_sales=0
lowest_sales=0
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
sales_spread=highest_sales-lowest_sales

print(f"Best Sales Day: Day {best_day}")
print(f"Highest Daily Sales: RM{highest_sales:.2f}")
print(f"Worst Sales Day: Day {worst_day}")
print(f"Lowest Daily Sales: RM{lowest_sales:.2f}")
print(f"Sales Spread: RM{sales_spread:.2f}")
