"""
Module 1 - Lesson 30
PurrNest 7-Day Sales Analytics Capstone

Objective:
Integrate the major Module 1 processing patterns into one seven-day business
analytics program without introducing new Python concepts.

Business scenario:
PurrNest wants a seven-day report covering overall sales, target achievement,
best and worst sales days, and the difference between both extremes.

Requirements:
1. Display exactly:
   PurrNest 7-Day Sales Analytics Capstone
2. Process exactly Day 1 through Day 7 using for + range().
3. For every day ask exactly:
   Enter Day X Sales:
4. Convert input using float().

Validation:
- Daily Sales >= 0 is valid.
- If Daily Sales is negative, display exactly:
  Invalid Daily Sales
- Ask again for the same day until the value is valid.
- Invalid attempts consume no day and change no metric.
- Do not use break or continue.

Raw metrics maintained during processing:
- Total Sales: add every valid Daily Sales value.
- Target Days: add 1 only when Daily Sales >= RM20.00.
- Highest Daily Sales + Best Sales Day: update together for a strict maximum.
- Lowest Daily Sales + Worst Sales Day: update together for a strict minimum.
- The first valid day establishes both associated-state pairs.
- Maximum and minimum checks remain independent.
- Equal extremes preserve the earliest day.

Derived metrics calculated after seven valid days:
- Average Daily Sales = Total Sales / 7
- Target Hit Rate = (Target Days / 7) * 100
- Sales Spread = Highest Daily Sales - Lowest Daily Sales

Final output:
Total Sales: RMxx.xx
Average Daily Sales: RMxx.xx
Target Days: X
Target Hit Rate: xx.xx%
Best Sales Day: Day X
Highest Daily Sales: RMxx.xx
Worst Sales Day: Day X
Lowest Daily Sales: RMxx.xx
Sales Spread: RMxx.xx

Allowed Python:
- print(), input(), float()
- variables, arithmetic, and comparisons
- if / elif / else
- while, for, and range()
- f-string and .2f formatting

Do not use:
- lists, tuples, dictionaries, or sets
- functions or classes
- nested for loops
- enumerate()
- min(), max(), or abs()
- break or continue
- None
- try / except
- CSV, JSON, APIs, pandas, databases, or Streamlit

You must personally decide:
- accumulator and counter initialization
- the correct range()
- validation placement
- first-day initialization
- independent maximum and minimum comparisons
- synchronized associated-label updates
- target boundary handling
- which calculations and outputs belong after the loop
"""

# TODO: Write your implementation below this line.
print("PurrNest 7-Day Sales Analytics Capstone")
total_sales=0.0
target_days=0
worst_day=0
best_day=0
lowest_sales=0
highest_sales=0

for day in range(1,8):
    daily_sales=float(input(f"Enter Day {day} Sales:"))
    while daily_sales<0:
        print("Invalid Daily Sales")
        daily_sales=float(input(f"Enter Day {day} Sales:"))
    total_sales+=daily_sales
    if daily_sales>=20:
        target_days+=1
    if daily_sales<lowest_sales or day==1:
        lowest_sales=daily_sales
        worst_day=day
    if daily_sales>highest_sales or day==1:
        highest_sales=daily_sales
        best_day=day

average_daily_sales=total_sales/7
target_hit_rate=(target_days/7)*100
sales_spread=highest_sales-lowest_sales

print(f"Total Sales: RM{total_sales:.2f}")
print(f"Average Daily Sales: RM{average_daily_sales:.2f}")
print(f"Target Days: {target_days}")
print(f"Target Hit Rate: {target_hit_rate:.2f}%")
print(f"Best Sales Day: Day {best_day}")
print(f"Highest Daily Sales: RM{highest_sales:.2f}")
print(f"Worst Sales Day: Day {worst_day}")
print(f"Lowest Daily Sales: RM{lowest_sales:.2f}")
print(f"Sales Spread: RM{sales_spread:.2f}")
