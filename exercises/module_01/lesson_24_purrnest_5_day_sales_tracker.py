"""
Module 1 - Lesson 24
PurrNest 5-Day Sales Tracker

Learning objective:
Use a for loop with range() when the number of repetitions is known in
advance.

Business scenario:
PurrNest wants to enter sales totals for exactly five days and calculate
Total Sales and Average Daily Sales.

Requirements:
1. Display exactly:
   PurrNest 5-Day Sales Tracker
2. Create a Total Sales accumulator with an appropriate initial value.
3. Use for + range() to process exactly Day 1 through Day 5.
4. For each day, ask exactly:
   Enter Day X Sales:
5. Convert input using float().

Validation rule:
- Daily Sales >= 0 is valid.
- If a negative value is entered, display exactly:
  Invalid Daily Sales
- Ask for a new value for the same day until it is 0 or greater.
- A negative attempt must not move to the next day or affect Total Sales.
- Do not use break or continue.

After exactly five valid day values are processed:
- Calculate:
  Average Daily Sales = Total Sales / 5
- Display exactly:
  Total Sales: RMxx.xx
  Average Daily Sales: RMxx.xx
- Format both values to exactly two decimal places.

Allowed Python:
- print(), input(), float()
- variables and arithmetic
- comparisons
- if if needed
- while for same-day validation
- for and range()
- f-string two-decimal formatting

Do not use:
- lists, tuples, or dictionaries
- functions
- break or continue
- nested for loops
- enumerate()
- try / except

You must personally decide:
- how Total Sales begins
- which range() gives Day 1 through Day 5
- how the day variable appears in the prompt
- where same-day validation belongs
- where the valid value is accumulated
- where Average calculation and final output belong
"""

# TODO: Write your implementation below this line.
print("PurrNest 5-Day Sales Tracker")
total_sales=0.0
for day in range(1,6):
    daily_sales=float(input(f"Enter Day {day} Sales:"))
    while daily_sales<0:
        print("Invalid Daily Sales")
        daily_sales=float(input(f"Enter Day {day} Sales:"))
    
    total_sales+=daily_sales

average_daily_sales = total_sales / 5
print(f"Total Sales: RM{total_sales:.2f}")
print(f"Average Daily Sales: RM{average_daily_sales:.2f}")