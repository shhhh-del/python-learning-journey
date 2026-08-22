# Python Learning Progress

## Current Learning Status

- Accelerated Python Foundations combined with early Shopee and TikTok business applications

## Current Module

- [ ] Module 1: Python Foundations

## Completed Lessons

- [x] Module 1 — Lesson 01: Foundations Assessment
- [x] Module 1 — Lesson 02: TikTok Video Performance Classifier
- [x] Module 1 — Lesson 03: Shopee Free Shipping Eligibility Checker
- [x] Module 1 — Lesson 04: Shopee Seller Discount Eligibility Checker
- [x] Module 1 — Lesson 05: Shopee Product Stock Status Checker
- [x] Module 1 – Lesson 06: Shopee Stock Input Validator
- [x] Module 1 — Lesson 07: Shopee Inventory Action Checker
- [x] Module 1 — Lesson 08: Business Rule Priority Review

## Verified Skills

- [x] `print()`
- [x] Variables
- [x] `input()`
- [x] Strings
- [x] Integers
- [x] Floats
- [x] Basic multiplication
- [x] Converting input using `int()` and `float()`
- [x] Comparison operators
- [x] `if` / `elif` / `else`
- [x] Ordered conditional branches
- [x] Boundary-value testing
- [x] Logical operator `and`
- [x] Logical operator `or`
- [x] Logical operator `not`
- [x] Combining comparisons with logical operators
- [x] Nested `if` statements
- [x] Conditional input placement
- [x] Basic input validation using comparisons
- [x] Rejecting impossible negative inventory values
- [x] Combining ordered business rules in one `if` / `elif` / `else` chain
- [x] Prioritizing narrower conditions before overlapping wider conditions

The student personally wrote and manually tested the Lesson 01 program.

The student personally wrote and manually tested the Lesson 05 stock status checker.

The student personally wrote and manually tested the Lesson 06 stock input validator.

The student personally wrote and manually tested the Lesson 07 inventory action checker.

## Current Technical Milestone

- [x] Module 1 — Lesson 08: Business Rule Priority Review

## Completed Reviews

- [x] 2026-07-31 Friday Review: Shopee Inventory Decision System
- [x] 2026-08-07 Friday Review #2: PurrNest Financial Decision System

## Latest Session Evidence

- Date: 2026-07-31
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge Check Day
- Lesson or business feature completed: Shopee Inventory Decision System review exercise
- Final status: Passed
- Verified skills: Comparison operators, ordered `if` / `elif` / `else`, nested `if`, execution order, overlapping-condition priority, boundary testing, negative-stock validation, indentation, readability, and mutually exclusive output
- Code personally written: Yes; the student personally wrote the Shopee Inventory Decision System core logic and corrected its nested VIP decision
- Errors encountered: Several knowledge-check answers needed correction; the first implementation did not handle every non-`yes` VIP value according to the stated fallback rule; the first explanation used `< 3` instead of `<= 3` and initially omitted why later branches are skipped
- Corrections understood: The student corrected the boundary values to `-1`, `0`, `3`, and `4`; placed `stock == 0` before the overlapping `stock <= 3` rule; used a final nested `else` for every VIP value other than `yes`; and explained that later branches do not execute after the first true branch
- Tests performed: Stock `-1`, VIP `yes` → Invalid Stock Data; stock `0`, VIP `no` → Reject Order; stock `2`, VIP `yes` → Accept Order - Low Stock Warning; stock `4`, VIP `yes` → Priority Packing; stock `4`, VIP `no` → Normal Packing; student-selected stock `347`, VIP `maybe` → Normal Packing
- Codex review result: Passed through code inspection, six reported manual tests, boundary verification, and the student's explanation of nested execution order
- Files created or modified: `exercises/module_01/friday_review_shopee_inventory_decision_system.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

## Next Concept

- [x] Comparison operators
- [x] `if`
- [x] `elif`
- [x] `else`

## Next Saturday Business Application

- [x] PurrNest Shopee Order Profit Calculator Stage 1A: Single Order Net Profit Decision

Planned skills:

- Numeric input
- Basic calculation
- Comparison operators
- `if` / `elif` / `else`

This feature was completed and manually verified on 2026-08-01.

## Latest Saturday Business Application Evidence

- Date: 2026-08-01
- Day of week: Saturday
- Session type: Shopee Business Application Day
- Lesson or business feature completed: PurrNest Shopee Order Profit Calculator, Stage 1A - Single Order Net Profit Decision
- Final status: Passed
- Verified skills: Decimal input using `float()`, validation of six non-negative values, addition and subtraction for profit calculation, ordered `if` / `elif` / `else`, exactly one order status, and two-decimal f-string money formatting
- Code personally written: Yes; the student personally wrote the six inputs, validation, calculations, status logic, and output formatting
- Errors encountered: Selling price was initially included in total cost; the status decision and final outputs were initially outside the valid-input branch; statuses were initially printed directly; final output initially used literal placeholders and commas; the packaging prompt contained a spelling error
- Corrections understood: Revenue is not part of total cost; calculations and output must occur only after validation; net profit must exist before status comparison; an `if` / `elif` / `else` chain stops after its first matching branch and therefore produces one status; f-strings insert values and `.2f` formats money to two decimal places
- Tests performed: Six required manual tests covering profitable, break-even, loss, zero additional costs, negative selling price, and negative packaging cost; all produced the expected output
- Codex review result: Passed through static code inspection, six student-reported manual tests, scope review, secrets scan, and the student's explanation of calculation and condition order. Automated execution was unavailable because no Python runtime was discoverable in the Codex shell
- Files created or modified: `shopee_order_profit_calculator/profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Git commit and push after student confirmation

## Roadmap Milestones

1. [ ] Accelerated Python Foundations
2. [ ] Shopee Order and Profit Calculator
3. [ ] CSV and JSON Automation
4. [ ] TikTok Performance Analyzer
5. [ ] Streamlit Business Dashboard
6. [ ] FastAPI and Database Foundations
7. [ ] First Shopee or TikTok SaaS MVP
8. [ ] Portfolio Improvement and Job Preparation

## Historical and Archived Projects

- [x] Project 01: GitHub API Status Checker — completed historical work
- [ ] Legacy Project 02: GitHub User Finder Pro — paused and archived
- [ ] Legacy Project 03: GitHub Repo Explorer — paused and archived

Legacy Projects 02 and 03 are not part of the current main route and must not be restarted automatically.

## Module 1 Lesson 09 Status

- [x] Module 1 - Lesson 09: Using `float()` for Business Calculations

Verified skills:

- [x] Using `float()` for decimal price and cost input
- [x] Subtracting decimal business values to calculate profit
- [x] Comparing profit as positive, zero, or negative
- [x] Producing exactly one final status
- [x] Formatting money to exactly two decimal places

### Lesson 09 Evidence

- Date: 2026-08-03
- Day of week: Monday
- Session type: Core Python Learning Day
- Lesson or business feature completed: PurrNest Product Profit Preview
- Final status: Passed
- Verified skills: Decimal input using `float()`, subtraction for profit calculation, positive/zero/negative comparison, exactly one final status, and two-decimal money formatting
- Code personally written: Yes; the student personally wrote the complete product profit preview implementation and corrected its formatting syntax
- Errors encountered: The knowledge check initially treated `int("17.90")` as a value or Boolean result; the first implementation used invalid punctuation in the f-string format specifier and misspelled the Product Cost prompt
- Corrections understood: Text containing a decimal point cannot be converted directly with `int()`; `float()` preserves decimal price values; `.2f` formats money to two decimal places; and one `if` / `elif` / `else` chain separates positive, zero, and negative profit into exactly one status
- Tests performed: `17.90 / 10.00` -> `Profit: RM7.90`, `PROFIT`; `20.00 / 20.00` -> `Profit: RM0.00`, `BREAK-EVEN`; `15.00 / 20.00` -> `Profit: RM-5.00`, `LOSS`; `0.00 / 0.00` -> `Profit: RM0.00`, `BREAK-EVEN`; student-selected `360 / 79` -> `Profit: RM281.00`, `PROFIT`
- Codex review result: Passed through static code inspection, five student-reported manual tests, and the student's explanation of decimal input and mutually exclusive profit groups
- Files created or modified: `exercises/module_01/lesson_09_purrnest_product_profit_preview.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

## Module 1 Lesson 10 Status

- [x] Module 1 - Lesson 10: Multiple Business Inputs and Combined Calculations

Verified skills:

- [x] Converting multiple money inputs using `float()`
- [x] Adding product cost and packaging cost into an intermediate total
- [x] Using total cost in a second profit calculation
- [x] Formatting multiple money outputs to exactly two decimal places
- [x] Producing exactly one final profit status

### Lesson 10 Evidence

- Date: 2026-08-04
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Lesson or business feature completed: PurrNest Product Margin Calculator
- Final status: Passed
- Verified skills: Three decimal inputs using `float()`, addition for total cost, subtraction for profit, readable intermediate variables, two-decimal money formatting, and exactly one final status
- Code personally written: Yes; the student personally wrote the three inputs, combined calculations, formatted outputs, and profit classification
- Errors encountered: Knowledge Check Question 4 initially contained an addition error; the first manual-test reports omitted the displayed two-decimal formatting and required several attempts to report the decimal values
- Corrections understood: Product cost and packaging cost are added into `total_cost`; selling price minus `total_cost` calculates profit; storing total cost makes the second calculation clearer; and `.2f` displays every money result with two decimal places
- Tests performed: `20.00 / 10.00 / 2.00` -> total cost `RM12.00`, profit `RM8.00`, `PROFIT`; `12.00 / 10.00 / 2.00` -> total cost `RM12.00`, profit `RM0.00`, `BREAK-EVEN`; `10.00 / 10.00 / 2.00` -> total cost `RM12.00`, profit `RM-2.00`, `LOSS`; `0.00 / 0.00 / 0.00` -> total cost `RM0.00`, profit `RM0.00`, `BREAK-EVEN`; student-selected `9.00 / 7.00 / 2.00` -> total cost `RM9.00`, profit `RM0.00`, `BREAK-EVEN`
- Codex review result: Passed through static code inspection, five student-reported manual tests, formatting verification against the submitted f-strings, and the student's explanation of both calculation steps
- Files created or modified: `exercises/module_01/lesson_10_purrnest_product_margin_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

## Module 1 Lesson 11 Status

- [x] Module 1 - Lesson 11: Multiple Business Outputs and Percentage Calculation

Verified skills:

- [x] Converting multiple money inputs using `float()`
- [x] Adding costs and subtracting total cost from selling price
- [x] Calculating profit margin as a percentage
- [x] Protecting a percentage calculation from division by zero
- [x] Formatting money and percentages to exactly two decimal places
- [x] Producing exactly one final profit status

### Lesson 11 Evidence

- Date: 2026-08-05
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Lesson or business feature completed: PurrNest Profit Margin Calculator
- Final status: Passed
- Verified skills: Three money inputs using `float()`, total-cost and profit arithmetic, division and percentage calculation, zero-division protection, multiple formatted business outputs, and exactly one final status
- Code personally written: Yes; the student personally wrote the title, inputs, calculations, zero-price branch, formatted outputs, and profit classification
- Errors encountered: The knowledge check initially omitted the exact `float` type name and reported division as a fraction; output labels initially lacked required spaces; total-cost and profit outputs were temporarily placed inside the nonzero-price branch; and the calculated margin was temporarily printed outside its safe branch
- Corrections understood: `/` produces a decimal result for these float values; zero cannot be a divisor; the calculated margin belongs only in the nonzero-price branch; total cost and profit must print for both zero and nonzero selling prices; and exact label spacing is part of output formatting
- Tests performed: `20.00 / 10.00 / 2.00` -> margin `40.00%`, total cost `RM12.00`, profit `RM8.00`, `PROFIT`; `12.00 / 10.00 / 2.00` -> margin `0.00%`, total cost `RM12.00`, profit `RM0.00`, `BREAK-EVEN`; `10.00 / 10.00 / 2.00` -> margin `-20.00%`, total cost `RM12.00`, profit `RM-2.00`, `LOSS`; `0.00 / 0.00 / 0.00` -> margin `N/A`, total cost `RM0.00`, profit `RM0.00`, `BREAK-EVEN`; student-selected `36.00 / 27.00 / 2.00` -> margin `19.44%`, total cost `RM29.00`, profit `RM7.00`, `PROFIT`
- Codex review result: Passed through static code inspection, five student-reported manual tests, exact-format verification, zero-division review, and the student's explanation of the zero-price branch
- Files created or modified: `exercises/module_01/lesson_11_purrnest_profit_margin_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

## Module 1 Lesson 12 Status

- [x] Module 1 - Lesson 12: Business Input Validation with Multiple Money Fields

Verified skills:

- [x] Converting multiple money inputs using `float()`
- [x] Detecting any negative input using comparisons and `or`
- [x] Validating inputs before performing calculations
- [x] Stopping calculation and business-result output for invalid data
- [x] Protecting profit-margin calculation from division by zero
- [x] Formatting money and percentages to exactly two decimal places
- [x] Producing exactly one final status for valid input

### Lesson 12 Evidence

- Date: 2026-08-06
- Day of week: Thursday
- Session type: Core Python Learning Day
- Lesson or business feature completed: PurrNest Safe Profit Calculator
- Final status: Passed
- Verified skills: Three money inputs using `float()`, multi-field negative validation with comparisons and `or`, validation-before-calculation order, conditional execution, zero-division protection, arithmetic, two-decimal formatting, and exactly one status for valid input
- Code personally written: Yes; the student personally wrote the title, three inputs, combined validation condition, valid-input calculations, protected margin logic, formatted outputs, and profit classification
- Errors encountered: The knowledge check initially treated a negative decimal string as a conversion error and misclassified negative comparisons; the first implementation left margin and status logic outside the validation branch; a later revision moved margin logic but initially left the status chain outside; and the calculated margin initially lacked a required space after its label
- Corrections understood: `float()` accepts negative decimal text; negative values satisfy `< 0`; `or` makes validation true when any field is negative; invalid business data could create misleading results; and all calculation, output, and status logic must remain in the valid-input branch so invalid input prints only `INVALID INPUT`
- Tests performed: `20.00 / 10.00 / 2.00` -> total cost `RM12.00`, profit `RM8.00`, margin `40.00%`, `PROFIT`; `12.00 / 10.00 / 2.00` -> `RM12.00`, `RM0.00`, `0.00%`, `BREAK-EVEN`; `10.00 / 10.00 / 2.00` -> `RM12.00`, `RM-2.00`, `-20.00%`, `LOSS`; `0.00 / 0.00 / 0.00` -> `RM0.00`, `RM0.00`, `N/A`, `BREAK-EVEN`; `-1.00 / 10.00 / 2.00` -> only `INVALID INPUT`; student-selected `-20 / 10 / 2` -> only `INVALID INPUT`
- Codex review result: Passed through static code inspection, six student-reported manual tests, invalid-path verification, exact-format review, and the student's explanation of why invalid data must stop result processing
- Files created or modified: `exercises/module_01/lesson_12_purrnest_safe_profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

## Friday Review #2 Status

- [x] Friday Review #2: PurrNest Financial Decision System

Verified skills:

- [x] Converting multiple money inputs using `float()`
- [x] Validating multiple fields with comparisons and `or`
- [x] Performing validation before calculations and result output
- [x] Calculating total cost, profit, and profit margin
- [x] Protecting division from a zero selling price
- [x] Formatting money and percentages to exactly two decimal places
- [x] Producing exactly one final status for every valid input

### Friday Review #2 Evidence

- Date: 2026-08-07
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge-Check Day
- Lesson or business feature completed: PurrNest Financial Decision System
- Final status: Passed
- Verified skills: `float()`, comparison operators, `if` / `elif` / `else`, `or`, validation order, addition, subtraction, percentage calculation, zero-division protection, two-decimal formatting, and exactly one valid-input status
- Code personally written: Yes; the student personally wrote the inputs, multi-field validation, calculations, protected profit-margin logic, formatted outputs, and status classification
- Errors encountered: Knowledge-check Question 6 initially calculated the percentage incorrectly; Question 7 initially described a zero selling price as a business problem instead of identifying division by zero; Question 8 initially gave the status label rather than the number of statuses; the first implementation placed the status chain inside the nonzero-margin branch; one revision changed negative validation from `< 0` to `<= 0`; and the status chain required further indentation correction
- Corrections understood: Percentage calculation divides before multiplying by 100; dividing by zero causes an error; one conditional chain prints one status; validation uses `< 0` because zero is valid; the status chain must follow both margin paths while remaining inside the valid-input branch; and `or` rejects the record when any one money field is negative
- Tests performed: `20 / 10 / 2` -> `RM12.00`, `RM8.00`, `40.00%`, `PROFIT`; `12 / 10 / 2` -> `RM12.00`, `RM0.00`, `0.00%`, `BREAK-EVEN`; `10 / 10 / 2` -> `RM12.00`, `RM-2.00`, `-20.00%`, `LOSS`; `0 / 0 / 0` -> `RM0.00`, `RM0.00`, `N/A`, `BREAK-EVEN`; `-1 / 10 / 2` -> only `INVALID INPUT`; `10 / -5 / 2` -> only `INVALID INPUT`; student-designed `-3 / 9 / 2` -> only `INVALID INPUT`
- Codex review result: Passed through the corrected ten-question knowledge check, static code inspection, seven student-reported manual tests, invalid-path review, exact-format verification, and the student's explanation of validation boundaries, branch placement, and `or` logic
- Files created or modified: `exercises/module_01/friday_review_02_purrnest_financial_decision_system.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

## PurrNest Shopee Order Profit Calculator Stage 1B Status

- [x] Version 1 - Stage 1B: Quantity and Multiple-Unit Order Calculation

Verified skills:

- [x] Converting quantity with `int()` and money inputs with `float()`
- [x] Rejecting zero or negative quantity before calculations
- [x] Rejecting any negative money input before calculations
- [x] Calculating total sales revenue and total product cost using quantity
- [x] Combining per-order costs into total order cost
- [x] Calculating net profit for a multiple-unit order
- [x] Formatting four money outputs to exactly two decimal places
- [x] Producing exactly one order status for valid input

### Stage 1B Evidence

- Date: 2026-08-08
- Day of week: Saturday
- Session type: Shopee / TikTok Business Application Day
- Lesson or business feature completed: PurrNest Shopee Order Profit Calculator Version 1 - Stage 1B, Quantity and Multiple-Unit Order Calculation
- Final status: Passed
- Verified skills: `int()` quantity input, `float()` money inputs, quantity and money validation, validation-before-calculation order, multiple-unit revenue and product-cost calculations, total order cost, net profit, two-decimal formatting, and exactly one order status
- Code personally written: Yes; the student personally wrote all Stage 1B inputs, validation, calculations, formatted outputs, and status classification
- Errors encountered: The first student-designed loss test produced a profitable result; the first understanding answer referred to total profit instead of distinguishing total sales revenue from profit
- Corrections understood: A loss test requires total order cost to exceed total sales revenue; selling price per unit multiplied by quantity gives total sales revenue; product cost per unit multiplied by quantity gives total product cost; order-level costs are added once; and zero or negative quantity must be rejected before calculation
- Tests performed: Multiple-unit profitable order -> revenue `RM45.00`, product cost `RM18.00`, order cost `RM23.00`, net profit `RM22.00`, `PROFITABLE`; quantity-one order -> `RM10.00`, `RM6.00`, `RM8.00`, `RM2.00`, `PROFITABLE`; break-even order -> `RM20.00`, `RM16.00`, `RM20.00`, `RM0.00`, `BREAK-EVEN`; student-designed loss order using `25 / 2 / 18 / 6 / 5 / 0 / 5` -> `RM50.00`, `RM36.00`, `RM52.00`, `RM-2.00`, `LOSS`; quantity zero, quantity `-1`, and negative packaging cost each produced only `INVALID INPUT`
- Codex review result: Passed through static code inspection, seven student-reported manual tests, scope review, output-format verification, and the student's corrected explanation of quantity-based totals and order-level costs
- Files created or modified: `shopee_order_profit_calculator/stage_1b_quantity_profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start Stage 1C; wait for the Daily Learning Supervisor / SaaS Product Builder to generate the final progress report

## Module 1 Lesson 13 Status

- [x] Module 1 - Lesson 13: Introduction to `while` Loops

Verified skills:

- [x] Using a basic `while` loop with a comparison condition
- [x] Understanding that Python checks the condition before each repetition
- [x] Updating loop state with subtraction
- [x] Stopping a loop when its condition becomes false
- [x] Recognizing how a missing state update causes an infinite loop
- [x] Keeping negative and zero stock outside the countdown loop
- [x] Preserving the required countdown output order

### Lesson 13 Evidence

- Date: 2026-08-10
- Day of week: Monday
- Session type: Core Python Learning Day
- Lesson or business feature completed: PurrNest Low Stock Countdown
- Final status: Passed
- Verified skills: Basic `while` condition, pre-repetition condition checking, stock state update, countdown arithmetic, loop termination, infinite-loop understanding, negative-input handling, zero-stock handling, indentation, and output order
- Code personally written: Yes; the student personally wrote the stock input, conditional paths, `while` loop, stock decrement, and final output
- Errors encountered: The first report for input `1` omitted the `Stock Remaining: 1` line; the first answer about a missing decrement stated only that stock would not decrease and initially omitted the infinite-loop consequence
- Corrections understood: Input `1` must display its remaining stock before reaching zero; `stock_quantity -= 1` subtracts one on every repetition; the loop stops when `stock_quantity > 0` becomes false; and without the decrement a positive stock remains positive, repeatedly displays the same value, and creates an infinite loop
- Tests performed: Input `-1` -> `Invalid Stock`; input `0` -> `Out of Stock`; input `1` -> `Stock Remaining: 1`, then `Out of Stock`; input `3` -> remaining stock `3`, `2`, `1`, then `Out of Stock`; student-selected input `5` -> remaining stock `5`, `4`, `3`, `2`, `1`, then `Out of Stock`
- Codex review result: Passed through static inspection, five student-reported manual tests, loop-condition and termination review, scope review, output-order verification, and the student's explanation of condition failure and infinite-loop behavior
- Files created or modified: `exercises/module_01/lesson_13_purrnest_low_stock_countdown.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce another lesson; wait for the Daily Learning Supervisor

## Module 1 Lesson 14 Status

- [x] Module 1 - Lesson 14: Using `while` Loops for Input Validation

Verified skills:

- [x] Describing invalid input in a `while` condition
- [x] Reading the first value before the validation loop
- [x] Requesting and storing a new value inside the loop
- [x] Repeating after one or multiple invalid values
- [x] Stopping when the value becomes valid
- [x] Recognizing the infinite-loop risk when invalid state is not updated
- [x] Producing one final accepted-value output

### Lesson 14 Evidence

- Date: 2026-08-12
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Lesson or business feature completed: PurrNest Stock Input Retry
- Final status: Passed
- Verified skills: `while`-based input validation, invalid-state condition, input placement, controlling-variable update, repeated retry, loop termination, infinite-loop awareness, indentation, and final valid output
- Code personally written: Yes; the student personally wrote the title, initial integer input, validation loop, invalid message, repeated input update, and final output
- Errors encountered: In the knowledge check, the first answer used the age example instead of stating the general true-condition rule, and the first answer about a false condition mixed up repeating with exiting; no implementation errors were found
- Corrections understood: A `while` body runs while its condition is true; a false condition exits the loop and continues with the following code; a negative stock keeps the validation condition true; and failing to request a new value leaves the old negative value unchanged and causes an infinite loop
- Tests performed: Initial `0` -> `Valid Stock: 0`; initial `5` -> `Valid Stock: 5`; sequence `-1, 3` -> one `Invalid Stock`, then `Valid Stock: 3`; sequence `-5, -2, -1, 10` -> three `Invalid Stock` messages, then `Valid Stock: 10`; student-selected sequence `-3, -5, 0` -> two `Invalid Stock` messages, then `Valid Stock: 0`
- Codex review result: Passed through the corrected five-question knowledge check, static implementation inspection, five student-reported manual tests, loop-condition and input-update review, termination and scope verification, and a three-question understanding check
- Files created or modified: `exercises/module_01/lesson_14_purrnest_stock_input_retry.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start Lesson 15; wait for the Daily Learning Supervisor

## Friday Review #4 Status

- [x] Friday Review #4: PurrNest Daily Order Processing Summary

### Friday Review #4 Evidence

- Date: 2026-08-21
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge-Check Day
- Lesson or business feature completed: PurrNest Daily Order Processing Summary
- Final status: Passed
- Verified skills: One accumulator plus two event counters in a single `while` flow, metric separation, positive and negative branch updates, zero-sentinel behavior, repeated input, natural termination, infinite-loop recognition, final output placement, and two-decimal money formatting
- Code personally written: Yes; the student personally wrote the complete processing-summary implementation. Codex created only the exercise instructions
- Errors encountered: Knowledge-check answers initially needed more precise value-to-metric mapping; the first implementation omitted colons from two output labels; the first Test 6 report omitted the three invalid messages; the debugging challenge first identified the valid branch instead of the invalid branch; and several understanding-check answers needed clarification, including the truth value of `10 != 0`
- Corrections understood: Positive amounts update Valid Order Count and Total Sales; negative amounts update only Invalid Entry Count; zero updates nothing; negative values must not reduce Total Sales; all metrics must be initialized before the loop; final output belongs after the loop; and an unchanged nonzero input keeps the condition true and causes an infinite loop
- Tests performed: Initial `0` -> valid `0`, invalid `0`, `RM0.00`; `10, 0` -> `1`, `0`, `RM10.00`; `-5, 0` -> one invalid message, `0`, `1`, `RM0.00`; `10, -5, 20, 0` -> `2`, `1`, `RM30.00`; `10, -5, 20, -2, 5, 0` -> `3`, `2`, `RM35.00`; `-1, -2, -3, 0` -> three invalid messages, `0`, `3`, `RM0.00`; student-designed `1, 2, 3, 4, -5, -6, -7, 0` -> `4`, `3`, `RM10.00`
- Student-designed prediction: Correctly predicted Valid Orders `4`, Invalid Entries `3`, and Total Sales `RM10.00` before running
- Debugging challenge: Passed after correction; the student identified that a negative amount must not be added to Total Sales, predicted the incorrect change from `30` to `25`, and stated that only Invalid Entry Count should change
- Understanding check: Passed after corrections covering metric roles, branch-specific updates, sentinel behavior, initialization, output placement, and infinite-loop risk
- Codex review result: Passed through the corrected seven-question knowledge check, static code inspection, seven student-reported manual tests, student-designed prediction, debugging challenge, understanding check, AGENTS.md and scope review, and sensitive-information review
- Files created or modified: `exercises/module_01/friday_review_04_purrnest_daily_order_processing_summary.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 18 or another exercise; wait for the Daily Learning Supervisor

## Module 1 Lesson 15 Status

- [x] Module 1 - Lesson 15: `while` Loop with an Accumulator

Verified skills:

- [x] Initializing an accumulator before a loop
- [x] Adding each new value to an existing running total
- [x] Distinguishing replacement from accumulation
- [x] Updating repeated input inside a `while` loop
- [x] Using zero as a natural loop sentinel
- [x] Excluding negative values from the accumulator
- [x] Recognizing infinite-loop risk from missing input updates
- [x] Formatting an accumulated money total to two decimal places

### Lesson 15 Evidence

- Date: 2026-08-17
- Day of week: Monday
- Session type: Core Python Learning Day
- Lesson or business feature completed: PurrNest Daily Sales Accumulator
- Final status: Passed
- Verified skills: Accumulator initialization, running-total updates, replacement versus accumulation, positive-value loop condition, repeated input placement, zero sentinel behavior, negative-value rejection, natural termination, infinite-loop recognition, and two-decimal money formatting
- Code personally written: Yes; the student personally wrote the complete accumulator implementation. Codex created only the exercise instructions
- Errors encountered: The knowledge check initially predicted that a repeatedly reset accumulator would retain earlier values; the student initially asked how zero should stop the loop despite already having the correct condition; the first negative check did not handle an initially negative value; and the first infinite-loop explanation predicted that the loop would not execute
- Corrections understood: Resetting an accumulator erases earlier values; `order_amount > 0` naturally becomes false at zero; negative checking must also cover initial input; and failing to request a new amount leaves a positive condition true and repeatedly adds the same value forever
- Tests performed: `10, 0` -> `RM10.00`; `10, 20, 5, 0` -> `RM35.00`; initial `0` -> `RM0.00`; `5.50, 4.50, 10, 0` -> `RM20.00`; initial `-5` -> `Invalid Order Amount` and `RM0.00`; student-designed `5, 6, 7, 0` -> `RM18.00`
- Codex review result: Passed through the corrected five-question knowledge check, static code inspection, six student-reported manual tests, negative-input verification, understanding check, scope review, and sensitive-information review
- Files created or modified: `exercises/module_01/lesson_15_purrnest_daily_sales_accumulator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 16; wait for the Daily Learning Supervisor

## Module 1 Lesson 16 Status

- [x] Module 1 - Lesson 16: Counter Pattern with `while`

Verified skills:

- [x] Initializing a counter before a loop
- [x] Increasing a counter by exactly one per valid event
- [x] Distinguishing a counter from an accumulator
- [x] Using a zero sentinel with `!=`
- [x] Excluding invalid events from the count
- [x] Continuing input after a negative value
- [x] Preserving the counter across iterations
- [x] Recognizing reset and infinite-loop risks

### Lesson 16 Evidence

- Date: 2026-08-18
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Lesson or business feature completed: PurrNest Daily Order Counter
- Final status: Passed
- Verified skills: Counter initialization, increment-by-one behavior, valid-event counting, counter versus accumulator distinction, zero-sentinel termination, negative-input exclusion, continued input after invalid data, repeated input updates, and counter preservation across iterations
- Code personally written: Yes; the student personally wrote the complete counter implementation. Codex created only the exercise instructions and provided progressive guidance
- Errors encountered: Knowledge Check Question 3 initially excluded a later valid event; early implementations ended the loop at a negative value, retried a negative value only once, contained `order amount` with a space, and misused `while ... else`; the student-designed test initially omitted the final zero; the first understanding answers did not explain zero initialization and incorrectly connected resetting the counter with an infinite loop
- Corrections understood: `order_amount != 0` keeps both positive and negative inputs inside the session while reserving zero as the only sentinel; only the positive branch increments the counter; negative input displays an invalid message and continues; resetting the counter erases earlier counts but does not itself cause an infinite loop; and the input variable must keep updating
- Teaching adjustment: The sentinel use of `!=` was explicitly taught after the student correctly noted that this application had not been explained before implementation was requested
- Tests performed: Initial `0` -> `Total Orders: 0`; `10, 0` -> `1`; `10, 20, 5, 0` -> `3`; `5.50, 4.50, 10, 8, 0` -> `4`; `10, -5, 20, 0` -> invalid message and `2`; student-designed `1, 2, 3, 4, -5, 0` -> invalid message and `4`
- Codex review result: Passed through the corrected five-question knowledge check, static code inspection, six student-reported manual tests, negative-input verification, understanding check, AGENTS.md and scope review, and sensitive-information review
- Files created or modified: `exercises/module_01/lesson_16_purrnest_daily_order_counter.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 17; wait for the Daily Learning Supervisor

## Module 1 Lesson 17 Status

- [x] Module 1 - Lesson 17: Combining Counter and Accumulator in One `while` Loop

Verified skills:

- [x] Initializing a counter and accumulator before one loop
- [x] Updating both metrics for one valid event
- [x] Keeping count and total value as separate information
- [x] Excluding negative input from both metrics
- [x] Using zero as a sentinel without counting or accumulating it
- [x] Preserving both metrics across iterations
- [x] Producing final count and formatted sales output

### Lesson 17 Evidence

- Date: 2026-08-20
- Day of week: Thursday
- Session type: Core Python Learning Day
- Lesson or business feature completed: PurrNest Daily Sales Summary
- Final status: Passed
- Verified skills: Combined counter and accumulator initialization, simultaneous valid-event updates, separate count and total meanings, nonzero sentinel flow, negative-input exclusion, repeated input updates, natural zero termination, output placement, and two-decimal money formatting
- Code personally written: Yes; the student personally wrote the complete combined counter-and-accumulator implementation. Codex created only the exercise instructions
- Errors encountered: Several knowledge-check answers were initially incomplete; the first implementation did not update positive input and could loop forever, printed final results inside the loop, and misspelled the title
- Corrections understood: Every nonzero path must replace `order_amount`; positive input updates both metrics, negative input updates neither, zero exits before either update, final results belong after the loop, and resetting either metric inside the loop loses earlier information
- Tests performed: Initial `0` -> `0` orders and `RM0.00`; `10, 0` -> `1` and `RM10.00`; `10, 20, 5, 0` -> `3` and `RM35.00`; `5.50, 4.50, 10, 8, 0` -> `4` and `RM28.00`; `10, -5, 20, 0` -> one invalid message, `2`, and `RM30.00`; `-5, -10, 0` -> two invalid messages, `0`, and `RM0.00`; student-designed `1, 2, 3, 4, -1, -2, 0` -> two invalid messages, `4`, and `RM10.00`
- Student-designed prediction: Correctly predicted Total Orders `4` and Total Sales `RM10.00` before running
- Codex review result: Passed through the corrected six-question knowledge check, static code inspection, seven student-reported manual tests, negative-input verification, understanding check, AGENTS.md and scope review, and sensitive-information review
- Files created or modified: `exercises/module_01/lesson_17_purrnest_daily_sales_summary.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 18; wait for the Daily Learning Supervisor

## PurrNest Shopee Order Profit Calculator Version 1 - Stage 1B.1 Status

- [x] Stage 1B.1: Repeated Input Until Valid

### Stage 1B.1 Evidence

- Date: 2026-08-15
- Day of week: Saturday
- Session type: Shopee / TikTok Business Application Day
- Lesson or business feature completed: Repeated Input Until Valid for every Stage 1B input
- Final status: Passed
- Verified skills: Individual `while` validation loops, integer quantity validation, money-field validation, controlling-variable updates, natural loop termination, preserving earlier valid input, using corrected values in calculations, infinite-loop recognition, unchanged multi-unit profit formulas, two-decimal output, and exactly one order status
- Code personally written: Yes; the student personally wrote the seven core retry loops. Codex changed only two documentation lines after the student requested it
- Errors encountered: Selling Price initially rejected zero with `<= 0`; the first required Packaging Cost test used Product Cost instead; the first proposed loss test produced a profit; and the first understanding answer did not identify a missing controlling-variable update as an infinite-loop cause
- Corrections understood: Every money field accepts zero and repeats only for negative values; quantity repeats for zero or negative values; each loop must update its own variable; previous valid fields should not restart; and a loss requires total order cost to exceed total sales revenue
- Tests performed: Seven required student-run manual tests covering immediate valid input, zero quantity retry, repeated negative quantity retry, Packaging Cost retry, repeated negative money retry ending at zero, valid zero money fields, and a corrected-value loss order
- Test results: All seven passed. The final loss test used final valid values `15 / 1 / 8 / 4 / 4 / 0 / 3` after rejecting Packaging Cost `-2`, producing revenue `RM15.00`, product cost `RM8.00`, order cost `RM19.00`, net profit `RM-4.00`, and `LOSS`
- Codex review result: Passed through static code inspection, seven student-reported manual tests, loop-boundary and variable-update review, formula and status review, scope review, understanding check, and sensitive-information review
- Files created or modified: `shopee_order_profit_calculator/stage_1b_quantity_profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start another feature or Stage 1C; wait for the SaaS Product Builder

## PurrNest Shopee Order Profit Calculator Version 1 - Stage 1B.2 Status

- [x] Stage 1B.2: Multi-Order Session Summary

### Stage 1B.2 Evidence

- Date: 2026-08-22
- Day of week: Saturday
- Session type: Shopee / TikTok Business Application Day
- Lesson or business feature completed: Multi-Order Session Summary
- Final status: Passed
- Verified features: Preserved Stage 1B.1 validation and calculations, repeated complete order processing, lowercase `yes` continuation and `no` termination, Orders Processed counter, Session Total Sales Revenue accumulator, Session Total Net Profit accumulator, invalid-retry isolation, and one final formatted Session Summary
- Code personally written: Yes; the student personally wrote the session variables, session metric updates, outer order loop, yes/no control, and Session Summary. Codex changed only the version and scope documentation
- Errors encountered: The student initially confused per-order formulas with session variables; used singular `order_processed`; first asked yes/no before the first order; initially left the single-order flow outside the outer loop; first placed Session Summary inside repeated processing; and had summary label and variable-format errors
- Corrections understood: Session metrics begin before all orders, the complete Stage 1B.1 flow belongs inside the outer loop, each valid order updates session metrics once, yes/no is requested after a completed order, the control variable must update, and Session Summary belongs after the loop
- Tests performed: Test 1 one profitable order -> `1 / RM30.00 / RM14.00`; Test 2 two profitable orders -> `2 / RM40.00 / RM16.00`; Test 3 profit-plus-loss actual result -> `2 / RM30.00 / RM7.00`; Test 4 three orders -> `3 / RM70.00 / RM30.00`; Test 5 invalid Quantity retry -> one processed order and `RM30.00 / RM14.00`; Test 6 invalid Packaging Cost retry -> one processed order and `RM30.00 / RM14.00`; Test 7 student-designed three-order scenario with invalid Quantity retry and mixed `PROFITABLE` / `LOSS` statuses -> `3 / RM70.00 / RM30.00`
- Test 3 prediction note: Functional results were correct; the student explicitly waived repeating the pre-run prediction step due to time after running the scenario
- Student-designed test: Predicted Orders Processed `3`, Session Total Sales Revenue `RM70.00`, and Session Total Net Profit `RM30.00`; actual output matched
- Codex review result: Passed through static inspection, seven student-reported manual tests, preserved formula and validation review, session update and control-flow review, understanding check, AGENTS.md and scope review, and sensitive-information review
- Files created or modified: `shopee_order_profit_calculator/stage_1b_quantity_profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start another feature or Stage 1C; wait for the Daily Learning Supervisor / SaaS Product Builder

## Review Approach

- Use a short explanation and one assessment exercise for familiar topics.
- Move forward without unnecessary repetition after an assessment is passed.
- Connect core modules to realistic Shopee or TikTok uses when appropriate.
- Begin practical business tools before completing the entire Python curriculum.
- Do not import or move old Python files.

## Friday Review #3 Status

- [x] Friday Review #3: PurrNest Restock Quantity Validator

### Friday Review #3 Evidence

- Date: 2026-08-14
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge-Check Day
- Lesson or business feature completed: PurrNest Restock Quantity Validator
- Final status: Passed
- Verified skills: Translating a business validity rule into an invalid-state `while` condition, rejecting zero and negative quantities, updating the controlling input, repeated validation, natural loop termination, infinite-loop recognition, boundary-condition debugging, indentation, and output order
- Code personally written: Yes; the student personally wrote the title, integer input, validation loop, invalid message, repeated input update, and final accepted-value output
- Errors encountered: Initial knowledge-check answers confused the general loop condition and the invalid range; the first implementation indented the final accepted output inside the loop
- Corrections understood: A `while` loop repeats while its condition is true; quantities less than or equal to zero are invalid under the restock rule; the controlling value must be replaced to avoid an infinite loop; and the accepted output belongs after the loop so it runs once only for a valid value
- Tests performed: Initial `1` -> `Restock Quantity Accepted: 1`; `0, 1` -> one invalid message, then accepted `1`; `-1, 5` -> one invalid message, then accepted `5`; `0, -2, 0, 10` -> three invalid messages, then accepted `10`; student-designed `-1, -2, -3, 0, 5` -> four invalid messages, then accepted `5`
- Debugging challenge: Passed; the student identified that `< 0` incorrectly accepts zero and corrected the boundary to include zero
- Understanding check: Passed; the student explained the different business meaning of zero stock versus zero reorder quantity, the invalid repeat range, the need to update input, and false-condition termination
- Codex review result: Passed through the corrected six-question knowledge check, static code inspection, five student-reported manual tests, debugging challenge, understanding check, scope review, and secrets/private-data review
- Files created or modified: `exercises/module_01/friday_review_03_purrnest_restock_quantity_validator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start Lesson 15; wait for the Daily Learning Supervisor
