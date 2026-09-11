"""
Friday Review #6
PurrNest 7-Day Sales Performance Summary

Objective:
Combine fixed for-loop processing, validation, an accumulator, a conditional
counter, associated maximum tracking, an average, and a percentage.

Display exactly:
PurrNest 7-Day Sales Performance Summary

Process exactly Day 1 through Day 7 with for + range().

For each day ask exactly:
Enter Day X Sales:

Convert input using float().

Validation:
- Daily Sales >= 0 is valid.
- If input is negative, display exactly:
  Invalid Daily Sales
- Ask again for the same day.
- Invalid attempts consume no day and change no metric.
- Do not use break or continue.

Raw metrics maintained during valid processing:
1. Total Sales
   Add every valid daily sales value.
2. Target Days
   Increase only when Daily Sales >= RM20.00.
3. Highest Daily Sales
   Track the highest valid daily value.
4. Best Sales Day
   Track the day associated with Highest Daily Sales.

First-day and tie rule:
- Day 1 establishes Highest Daily Sales and Best Sales Day.
- A later strictly greater value updates both states together.
- An equal or lower value changes neither state.
- Earliest day wins a tie.

After exactly seven valid days, calculate:
- Average Daily Sales = Total Sales / 7
- Target Hit Rate = (Target Days / 7) * 100

Display exactly:
Total Sales: RMxx.xx
Average Daily Sales: RMxx.xx
Target Days: X
Target Hit Rate: xx.xx%
Best Sales Day: Day X
Highest Daily Sales: RMxx.xx

Use exactly two decimal places for money and rate.

Allowed Python:
- print(), input(), float()
- variables and arithmetic
- division and multiplication
- comparisons
- if / elif / else
- while
- for and range()
- f-string and .2f formatting

Do not use:
- lists, tuples, or dictionaries
- functions
- nested for loops
- break or continue
- enumerate()
- min(), max(), or None
- try / except

You must personally decide:
- how all raw metrics begin
- where validation belongs
- which metrics every valid day changes
- which metrics change conditionally
- how associated states update together
- where derived calculations and final output belong
"""

# TODO: Write your implementation below this line.

print("PurrNest 7-Day Sales Performance Summary")
total_sales=0.0
target_days=0
highest_daily_sales=0.0
best_sales_day=1

for day in range(1,8):
    daily_sales=float(input(f"Enter Day {day} Sales:"))
    while daily_sales<0:
        print("Invalid Daily Sales")
        daily_sales=float(input(f"Enter Day {day} Sales:"))

    total_sales+=daily_sales
    if daily_sales>=20:
        target_days+=1
    if daily_sales>highest_daily_sales or day==1:
        highest_daily_sales=daily_sales
        best_sales_day=day

average_daily_sales = total_sales / 7
target_hit_rate=(target_days/7)*100
print(f"Total Sales: RM{total_sales:.2f}")
print(f"Average Daily Sales: RM{average_daily_sales:.2f}")
print(f"Target Days: {target_days}")
print(f"Target Hit Rate: {target_hit_rate:.2f}%")
print(f"Best Sales Day: Day {best_sales_day}")
print(f"Highest Daily Sales: RM{highest_daily_sales:.2f}")
