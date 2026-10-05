# Python Learning Log

## 2026-07-17 — Learning Plan Restart

### Decision

- Chose to restart Python learning with a structured accelerated foundations review.
- The review will begin with Module 1: Python Foundations.
- Familiar topics will receive a short explanation and one assessment exercise.
- Passing an assessment will allow progress without unnecessary repetition.
- Old Python code will not be imported or moved.
- Project 01 remains recorded as historical previous work.
- Project 02 is no longer the current starting point.

### Lessons Completed

- No new Python lessons were completed during this planning session.

### Next Task

- Complete the first foundations assessment lesson.

## 2026-07-17 — Module 1, Lesson 01: Foundations Assessment

### Result

- Lesson 01 successfully completed and passed.
- The student personally wrote and manually tested the program.

### Verified Skills

- `print()`
- Variables
- `input()`
- Strings
- Integers
- Floats
- Basic multiplication
- Converting input using `int()` and `float()`

### Exercise Completed

- Created a checkout summary that accepts customer and product details.
- Accepted a decimal price and a whole-number quantity.
- Calculated and displayed the total cost.

### Mistake Made

- `input()` originally returned strings.
- Multiplying two strings caused a `TypeError`.

### Correction Understood

- Changed the price to a float using `float()`.
- Changed the quantity to an integer using `int()`.
- Understood that numerical input must be converted before arithmetic.

### Topics Requiring Review

- None required from Lesson 01 at this time.

### Next Recommended Task

- Module 1 — Lesson 02: Comparison operators and `if`/`else` assessment.

## 2026-07-20 — Roadmap and Weekly Schedule Decision

### Session Evidence

- Date: 2026-07-20
- Day of week: Monday
- Session type: Learning-system planning update
- Lesson or business feature: Roadmap and weekly schedule revision
- Final status: Planning rules applied; no Python lesson completed
- Verified skills: No new skills verified
- Code personally written: No code written
- Errors encountered: None recorded
- Corrections understood: None required
- Tests performed: No Python tests performed
- Codex review result: No code review performed
- Files modified: `AGENTS.md`, `progress.md`, and `learning_log.md`
- Next confirmed task: Module 1 — Lesson 02: comparison operators and `if` / `elif` / `else` assessment

### Roadmap Decision

- Legacy Project 02: GitHub User Finder Pro was paused and archived.
- Legacy Project 03: GitHub Repo Explorer was paused and archived.
- Neither legacy project will restart automatically.
- The new roadmap prioritizes early Shopee and TikTok business applications alongside Python foundations.
- Practical command-line business tools will begin before the entire Python curriculum is completed.
- The roadmap will later progress through CSV and JSON automation, data analysis, Streamlit dashboards, FastAPI, databases, and SaaS architecture.

### Weekly Schedule Decision

- The weekly learning schedule was adopted.
- Monday through Thursday are Core Python Learning Days.
- Friday is a Review, Debugging, or Knowledge-Check Day.
- Saturday is the default Shopee or TikTok Business Application Day.
- Sunday is for weekly review, GitHub organization, catch-up, or rest.
- Missing a scheduled day does not mean the roadmap has failed; learning continues from the latest verified progress.

### Reporting Decision

- Daily learning records and business-feature reports will be generated only from verified session evidence.
- Lessons and business features will not be marked as passed without test results and demonstrated understanding.

### Lesson Progress

- No new Python lesson was completed during this planning update.

### Next Confirmed Task

- Module 1 — Lesson 02: comparison operators and `if` / `elif` / `else` assessment.

### Next Saturday Business Application

- Shopee Profit Decision Calculator v0.1.
- Planned skills: numeric input, basic calculation, comparison operators, and `if` / `elif` / `else`.
- Status: Not started.

## 2026-07-20 — Module 1, Lesson 02: TikTok Video Performance Classifier

### Session Evidence

- Date: 2026-07-20
- Day of week: Monday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: Module 1 — Lesson 02: TikTok Video Performance Classifier
- Final status: Passed
- Verified skills: Comparison operators, `if`, `elif`, `else`, integer conversion, ordered branches, and boundary-value testing
- Code personally written: Yes; the student personally wrote the classifier’s core logic
- Errors encountered: None recorded in the submitted implementation
- Corrections understood: The student explained that `else` handles 300–499 because earlier branches already handle values below 300 and values at or above 500
- Tests performed: `299` → Low Performance; `300` → Normal Performance; `499` → Normal Performance; `500` → High Performance; `9999` → High Performance
- Codex review result: Passed; conditions, indentation, branch reachability, and boundaries were correct
- Files created or modified: `exercises/module_01/lesson_02_tiktok_video_performance_classifier.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Shopee Profit Decision Calculator v0.1 on the next Saturday Business Application Day

### Concepts Demonstrated

- Comparisons produce `True` or `False`.
- Python checks `if`, `elif`, and `else` branches in order.
- Earlier conditions can exclude values so the final `else` safely handles the remaining range.
- Boundary values should be tested directly.

## 2026-07-21 — Module 1, Lesson 03: Shopee Free Shipping Eligibility Checker

### Session Evidence

- Date: 2026-07-21
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Available time: 60 minutes
- Lesson or business feature: Module 1 — Lesson 03: Shopee Free Shipping Eligibility Checker
- Final status: Passed
- Verified skills: `and`, `or`, `not`, comparisons, conditional branches, numeric conversion, combined business rules, and boundary testing
- Code personally written: Yes; the student personally wrote the core eligibility logic
- Errors encountered: The first version printed both the Part A result and the final VIP-aware result; an additional East-region test result was initially reported incorrectly
- Corrections understood: The earlier duplicate decision was removed; the student understood that `or` grants free shipping when VIP is `yes`, and that a non-VIP East-region order does not qualify regardless of amount
- Tests performed: RM39 West VIP=no → Standard Shipping; RM40 West VIP=no → Free Shipping; RM100 East VIP=no → Standard Shipping; RM20 West VIP=yes → Free Shipping; RM100 East VIP=yes → Free Shipping; RM9999 East VIP=no → Standard Shipping
- Codex review result: Passed; logical operators, comparisons, indentation, readability, boundary behavior, and branch reachability were verified
- Files created or modified: `exercises/module_01/lesson_03_shopee_free_shipping_eligibility_checker.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- `and` requires both connected conditions to be true.
- `or` requires at least one connected condition to be true.
- `not` reverses a Boolean value.
- Logical operators can combine multiple business rules into one decision.
- Boundary and exception cases must be tested directly.

## 2026-07-22 — Module 1, Lesson 04: Shopee Seller Discount Eligibility Checker

### Session Evidence

- Date: 2026-07-22
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Available time: 60 minutes
- Lesson or business feature: Module 1 — Lesson 04: Shopee Seller Discount Eligibility Checker
- Final status: Passed
- Verified skills: Nested `if` statements, indentation, conditional input placement, numeric conversion, and RM100 boundary handling
- Code personally written: Yes; the student personally wrote the nested discount decision logic
- Errors encountered: The order amount was initially requested before checking VIP status; its first move caused an indentation error; required output capitalization, colons, and spacing needed correction
- Corrections understood: The order amount belongs inside the outer VIP branch and before the nested amount comparison because only VIP customers require that input
- Tests performed: VIP=no → No Discount; VIP=yes and RM99 → VIP Discount: 10%; VIP=yes and RM100 → VIP Discount: 20%; VIP=yes and RM500 → VIP Discount: 20%; student-chosen VIP=yes and RM99999 → VIP Discount: 20%
- Codex review result: Passed; indentation, nested structure, input placement, absence of duplicated logic, readability, boundary behavior, and required manual tests were verified
- Files created or modified: `exercises/module_01/lesson_04_shopee_seller_discount_eligibility_checker.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- An inner `if` is evaluated only after its outer `if` branch is entered.
- Conditional input can prevent irrelevant questions from being asked.
- Indentation determines which statements belong to each conditional branch.
- `>= 100` correctly includes the RM100 boundary.

## 2026-07-23 — Module 1, Lesson 05: Shopee Product Stock Status Checker

### Session Evidence

- Date: 2026-07-23
- Day of week: Thursday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: Module 1 — Lesson 05: Multiple Conditions using `elif`
- Final status: Passed
- Verified skills: Ordered `if` / `elif` / `else` branches, integer conversion, comparisons, indentation, mutually exclusive classification, and boundary-value testing
- Code personally written: Yes; the student personally wrote the stock classification logic
- Errors encountered: In knowledge-check question 4, the student initially expected a later `elif` branch to execute after the first `if` condition was true
- Corrections understood: The student corrected the prediction to only `Positive`, demonstrating that Python skips later branches after the first true branch in one `if` / `elif` / `else` chain
- Tests performed: `0` → Out of Stock; `1` → Low Stock; `5` → Low Stock; `6` → Normal Stock; `20` → Normal Stock; `21` → High Stock; student-chosen `9999` → High Stock
- Codex review result: Passed; branch ordering, comparisons, indentation, readability, unnecessary conditions, and boundary values were correct
- Files created or modified: `exercises/module_01/lesson_05_shopee_product_stock_status_checker.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- Separate `if` statements are evaluated independently.
- An `if` / `elif` / `else` chain stops after its first true branch.
- Conditions must be ordered from the special or narrower case toward wider ranges.
- Earlier branches make repeated lower-bound conditions unnecessary.
- Boundary values should be tested directly.

## 2026-07-28 — Module 1, Lesson 06: Shopee Stock Input Validator

### Session Evidence

- Date: 2026-07-28
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: Module 1 — Lesson 06: Basic Input Validation using comparisons and `if` / `elif` / `else`
- Final status: Passed
- Verified skills: Integer input conversion, negative-value validation, comparison operators, ordered `if` / `elif` / `else` branches, mutually exclusive classification, consistent indentation, and boundary-value testing
- Code personally written: Yes; the student personally wrote the validator's core logic
- Errors encountered: The student initially expected two branches to run in one ordered conditional chain; the input prompt initially differed from the requirement; branch-body indentation was initially inconsistent
- Corrections understood: The student demonstrated that only the first true branch executes, corrected the required prompt, aligned branch indentation, and explained that `else` handles positive quantities because earlier branches already handle negative values and zero
- Tests performed: `-1` → Invalid Stock; `0` → Out of Stock; `1` → Valid Stock; `50` → Valid Stock; student-chosen `99999` → Valid Stock
- Codex review result: Passed by code inspection and reported manual-test evidence; all exercise requirements and required boundaries were satisfied. Independent automated execution was unavailable because no Python runtime was discoverable in the review shell
- Files created or modified: `exercises/module_01/lesson_06_shopee_stock_input_validator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- Input validation rejects impossible business data before it is accepted as valid.
- Negative inventory is invalid, while zero is a separate valid state meaning out of stock.
- An ordered conditional chain executes exactly one result branch.
- Earlier negative and zero checks allow the final `else` to represent every positive integer.

## 2026-07-29 – Module 1, Lesson 07: Shopee Inventory Action Checker

### Session Evidence

- Date: 2026-07-29
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: Module 1 – Lesson 07: Combining Business Rules with `if` / `elif` / `else`
- Final status: Passed
- Verified skills: Integer input conversion, ordered business rules, narrower-before-wider condition ordering, comparison operators, mutually exclusive classification, exact output labels, consistent indentation, and boundary reasoning
- Code personally written: Yes; the student personally wrote the inventory checker's core logic
- Errors encountered: The `stock_quantity <= 5` branch initially printed an incomplete classification label
- Corrections understood: The required label was corrected; the student explained that placing `<= 20` first would capture values such as 5 before the narrower rule could be checked because only the first true branch executes
- Tests performed: `-1` → Invalid Stock; `0` → Restock Immediately; `3` → Low Stock - Reorder Soon; `10` → Stock Level Normal; `50` → Stock Sufficient; student-selected `9999` → Stock Sufficient; boundary reasoning confirmed for `5` and `20`
- Codex review result: Passed through code inspection, reported manual-test evidence, and the student's explanation of condition ordering and boundaries
- Files created or modified: `exercises/module_01/lesson_07_shopee_inventory_action_checker.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- Business rules should be checked from special or narrower cases toward wider ranges.
- Overlapping conditions can misclassify a value when a broader rule appears too early.
- One `if` / `elif` / `else` chain produces exactly one classification.
- Earlier branches make repeated lower-bound comparisons unnecessary.
- Exact output labels and boundary values are part of the program requirements.

## 2026-07-30 — Module 1, Lesson 08: Business Rule Priority Review

### Session Evidence

- Date: 2026-07-30
- Day of week: Thursday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: Shopee Order Acceptance Checker
- Final status: Passed
- Verified skills: Business-rule priority, specific-before-general condition ordering, overlapping-condition reasoning, first-true-branch execution, integer input conversion, mutually exclusive output, indentation, readability, and boundary-value testing
- Code personally written: Yes; the student personally wrote the order acceptance checker's core logic
- Errors encountered: Knowledge-check Question 2 was initially omitted, and Question 5 initially predicted the later zero branch instead of the earlier matching branch
- Corrections understood: The student corrected both predictions and explained that zero satisfies `<= 3`, so placing that broader condition before `== 0` would capture zero and prevent the specific zero result
- Tests performed: `-1` → Invalid Stock Data; `0` → Reject Order; `1` → Accept Order - Low Stock Warning; `3` → Accept Order - Low Stock Warning; `4` → Accept Order; student-selected `-3` → Invalid Stock Data
- Codex review result: Passed through code inspection, six reported manual tests, boundary verification, and the student's explanation of overlapping conditions and execution order
- Files created or modified: `exercises/module_01/lesson_08_shopee_order_acceptance_checker.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- Specific business rules must be checked before broader overlapping rules.
- Python executes only the first true branch in one `if` / `elif` / `else` chain.
- Zero satisfies `<= 3`, making condition order essential for the correct business decision.
- A classification program should produce exactly one final result.
- Boundary values should be tested directly.

## 2026-07-31 — Friday Review: Shopee Inventory Decision System

### Session Evidence

- Date: 2026-07-31
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge Check Day
- Available time: 30 minutes
- Lesson or business feature: Shopee Inventory Decision System review exercise
- Final status: Passed
- Verified skills: Comparison operators, ordered `if` / `elif` / `else`, nested `if`, execution order, overlapping-condition priority, boundary testing, negative-stock validation, indentation, readability, and mutually exclusive output
- Code personally written: Yes; the student personally wrote the core inventory and VIP decision logic
- Errors encountered: Several knowledge-check answers needed correction; the first implementation did not apply the required fallback to every VIP value other than `yes`; the first understanding explanation used `< 3` instead of `<= 3` and initially omitted the first-true-branch execution rule
- Corrections understood: The student corrected the test boundaries, prioritized `stock == 0` before `stock <= 3`, replaced the incomplete nested VIP classification with the required fallback, and explained that later branches are skipped after the first true branch executes
- Tests performed: Stock `-1`, VIP `yes` → Invalid Stock Data; stock `0`, VIP `no` → Reject Order; stock `2`, VIP `yes` → Accept Order - Low Stock Warning; stock `4`, VIP `yes` → Priority Packing; stock `4`, VIP `no` → Normal Packing; student-selected stock `347`, VIP `maybe` → Normal Packing
- Codex review result: Passed through code inspection, six reported manual tests, boundary verification, and the student's explanation of nested execution order
- Files created or modified: `exercises/module_01/friday_review_shopee_inventory_decision_system.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- Specific stock rules must appear before broader overlapping ranges.
- A nested decision applies the VIP rule only after the outer stock rules reach it.
- Python skips later branches after the first true branch in one conditional chain.
- A final `else` provides the required fallback and preserves exactly one result.
- The values `-1`, `0`, `3`, and `4` verify the important stock boundaries.

## 2026-08-01 - PurrNest Shopee Order Profit Calculator, Stage 1A

### Session Evidence

- Date: 2026-08-01
- Day of week: Saturday
- Session type: Shopee Business Application Day
- Available time: Not specified
- Lesson or business feature: Single Order Net Profit Decision
- Final status: Passed
- Verified skills: Six decimal inputs using `float()`, non-negative input validation, total-cost and net-profit calculations, ordered profit classification, exactly one final status, and f-string money formatting with two decimal places
- Code personally written: Yes; the student personally wrote and corrected the complete Stage 1A core logic
- Errors encountered: Selling price was initially counted as a cost; valid-result logic initially escaped the validation branch; status labels were initially printed separately; output initially contained literal placeholders and incorrect punctuation; `packaging` was misspelled in one prompt
- Corrections understood: Total cost contains only costs; invalid data must stop financial calculation and output; `net_profit` must be calculated before it is compared; the first matching branch in `if` / `elif` / `else` executes and later branches are skipped; f-strings insert variable values and `.2f` displays two decimal places
- Tests performed: (1) profitable order produced RM7.40 and PROFITABLE; (2) break-even produced RM0.00 and BREAK-EVEN; (3) loss produced RM-2.50 and LOSS; (4) zero additional costs produced RM11.90 and PROFITABLE; (5) negative selling price produced only INVALID INPUT; (6) negative packaging cost produced only INVALID INPUT
- Codex review result: Passed through final static inspection, all six student-reported manual test results, understanding checks, scope review, and a secrets scan with no matches. Automated execution was unavailable because no Python runtime was discoverable in the Codex shell
- Files created or modified: `shopee_order_profit_calculator/profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Review changed files, then commit and push after student confirmation

### Concepts Demonstrated

- `float(input(...))` converts typed text into a decimal value suitable for prices and costs.
- Revenue is kept separate from the five costs when calculating net profit.
- Validation occurs before calculations so negative business data produces only `INVALID INPUT`.
- A nested `if` / `elif` / `else` decision assigns exactly one order status.
- An f-string inserts calculated values, while `.2f` displays money to two decimal places.

## 2026-08-03 - Module 1, Lesson 09: Using `float()` for Business Calculations

### Session Evidence

- Date: 2026-08-03
- Day of week: Monday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Product Profit Preview
- Final status: Passed
- Verified skills: Decimal input using `float()`, subtraction for profit calculation, positive/zero/negative comparison, exactly one final status, and two-decimal money formatting
- Code personally written: Yes; the student personally wrote the title, two decimal inputs, profit calculation, formatted profit output, and classification logic
- Errors encountered: The knowledge check initially treated `int("17.90")` as a value or Boolean result; the first implementation used a semicolon instead of a colon in the f-string format specifier and misspelled the Product Cost prompt
- Corrections understood: `int("17.90")` raises a conversion error because the text contains a decimal point; `float()` preserves decimal values; `.2f` displays money with exactly two decimal places; and the conditional chain divides profit into positive, zero, and negative groups while printing exactly one status
- Tests performed: `17.90 / 10.00` -> `Profit: RM7.90`, `PROFIT`; `20.00 / 20.00` -> `Profit: RM0.00`, `BREAK-EVEN`; `15.00 / 20.00` -> `Profit: RM-5.00`, `LOSS`; `0.00 / 0.00` -> `Profit: RM0.00`, `BREAK-EVEN`; student-selected `360 / 79` -> `Profit: RM281.00`, `PROFIT`
- Codex review result: Passed through static code inspection, all five student-reported manual tests, and the student's explanation of why decimal inputs use `float()` and why one conditional chain produces one status
- Files created or modified: `exercises/module_01/lesson_09_purrnest_product_profit_preview.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- `float()` converts decimal price and cost input into values that can be used in arithmetic.
- Subtracting product cost from selling price calculates profit.
- `.2f` formats positive, zero, and negative money results to exactly two decimal places.
- One `if` / `elif` / `else` chain classifies a result into exactly one of three profit groups.

## 2026-08-04 - Module 1, Lesson 10: Multiple Business Inputs and Combined Calculations

### Session Evidence

- Date: 2026-08-04
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Product Margin Calculator
- Final status: Passed
- Verified skills: Three decimal inputs using `float()`, addition for total cost, subtraction for profit, readable intermediate variables, two-decimal money formatting, and exactly one final status
- Code personally written: Yes; the student personally wrote the title, three money inputs, total-cost calculation, profit calculation, formatted outputs, and classification logic
- Errors encountered: Knowledge Check Question 4 initially contained an addition error; the first manual-test reports omitted the displayed two-decimal formatting and required several attempts to report the decimal values
- Corrections understood: Product cost and packaging cost are added into `total_cost`; selling price minus `total_cost` calculates profit; the intermediate total improves readability and can be reused; and `.2f` displays each money result with two decimal places
- Tests performed: `20.00 / 10.00 / 2.00` -> total cost `RM12.00`, profit `RM8.00`, `PROFIT`; `12.00 / 10.00 / 2.00` -> total cost `RM12.00`, profit `RM0.00`, `BREAK-EVEN`; `10.00 / 10.00 / 2.00` -> total cost `RM12.00`, profit `RM-2.00`, `LOSS`; `0.00 / 0.00 / 0.00` -> total cost `RM0.00`, profit `RM0.00`, `BREAK-EVEN`; student-selected `9.00 / 7.00 / 2.00` -> total cost `RM9.00`, profit `RM0.00`, `BREAK-EVEN`
- Codex review result: Passed through static code inspection, five student-reported manual tests, formatting verification against the submitted f-strings, and the student's explanation of both calculation steps
- Files created or modified: `exercises/module_01/lesson_10_purrnest_product_margin_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- Multiple business inputs can be combined into one clearly named intermediate value.
- `total_cost` is calculated before profit so the program follows the business calculation in small steps.
- Profit is calculated by subtracting total cost from selling price.
- Multiple f-strings can format business money outputs consistently with `.2f`.
- One conditional chain produces exactly one positive, zero, or negative profit status.

## 2026-08-05 - Module 1, Lesson 11: Multiple Business Outputs and Percentage Calculation

### Session Evidence

- Date: 2026-08-05
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Profit Margin Calculator
- Final status: Passed
- Verified skills: Three money inputs using `float()`, addition and subtraction, division and percentage calculation, zero-division protection, multiple formatted business outputs, and exactly one final profit status
- Code personally written: Yes; the student personally wrote the title, inputs, total-cost and profit calculations, protected profit-margin calculation, formatted outputs, and status classification
- Errors encountered: The knowledge check initially omitted the exact `float` type and gave the division result as a fraction; output labels initially missed required spaces; output indentation temporarily prevented total cost and profit from printing for a zero selling price; and one revision referenced `profit_margin` outside the branch where it was created
- Corrections understood: Float division produces a decimal result; zero cannot be used as a divisor; `Profit Margin: N/A` safely represents the zero-price case; margin calculation and output belong in the nonzero branch; total cost and profit belong outside that decision so they always display; and exact spaces and `.2f` formatting produce consistent output
- Tests performed: `20.00 / 10.00 / 2.00` -> `40.00%`, `RM12.00`, `RM8.00`, `PROFIT`; `12.00 / 10.00 / 2.00` -> `0.00%`, `RM12.00`, `RM0.00`, `BREAK-EVEN`; `10.00 / 10.00 / 2.00` -> `-20.00%`, `RM12.00`, `RM-2.00`, `LOSS`; `0.00 / 0.00 / 0.00` -> `N/A`, `RM0.00`, `RM0.00`, `BREAK-EVEN`; student-selected `36.00 / 27.00 / 2.00` -> `19.44%`, `RM29.00`, `RM7.00`, `PROFIT`. Every run displayed exactly one final status
- Codex review result: Passed through static inspection, five correct student-reported manual tests, exact output-format review, zero-division review, and a final understanding check
- Files created or modified: `exercises/module_01/lesson_11_purrnest_profit_margin_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- Profit margin expresses profit as a percentage of selling price.
- A selling price of zero must be handled before division to prevent an error.
- Branch placement controls whether outputs appear in both zero and nonzero cases.
- `.2f` formats money and percentage results to exactly two decimal places.
- One `if` / `elif` / `else` chain produces exactly one profit classification.

## 2026-08-06 - Module 1, Lesson 12: Business Input Validation with Multiple Money Fields

### Session Evidence

- Date: 2026-08-06
- Day of week: Thursday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Safe Profit Calculator
- Final status: Passed
- Verified skills: Three money inputs using `float()`, comparisons, multi-field validation using `or`, validation-before-calculation order, conditional execution, zero-division protection, arithmetic, two-decimal formatting, and exactly one final status for valid input
- Code personally written: Yes; the student personally wrote the complete validation condition and all valid-input calculation, output, margin, and classification logic
- Errors encountered: The knowledge check initially treated `float("-4.50")` as an error and predicted negative comparisons incorrectly; margin and status logic initially escaped the valid-input branch; the status chain required further indentation correction; and one profit-margin label initially missed a space
- Corrections understood: `float()` accepts a minus sign and decimal point; a negative value is less than zero; an `or` validation condition becomes true when any field is negative; negative prices or costs are invalid business data that could create misleading results; and nesting all result logic inside `else` ensures invalid input produces only `INVALID INPUT`
- Tests performed: `20.00 / 10.00 / 2.00` -> `RM12.00`, `RM8.00`, `40.00%`, `PROFIT`; `12.00 / 10.00 / 2.00` -> `RM12.00`, `RM0.00`, `0.00%`, `BREAK-EVEN`; `10.00 / 10.00 / 2.00` -> `RM12.00`, `RM-2.00`, `-20.00%`, `LOSS`; `0.00 / 0.00 / 0.00` -> `RM0.00`, `RM0.00`, `N/A`, `BREAK-EVEN`; `-1.00 / 10.00 / 2.00` -> only `INVALID INPUT`; student-selected `-20 / 10 / 2` -> only `INVALID INPUT`. Every valid run displayed exactly one final status
- Codex review result: Passed through static inspection, six correct student-reported manual tests, validation-order and invalid-path review, exact output-format verification, and a final understanding check
- Files created or modified: `exercises/module_01/lesson_12_purrnest_safe_profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- Business input validation should occur before calculations and result output.
- `or` can reject a record when any required money field is negative.
- Invalid input must not continue into calculations, margin output, or classification.
- A zero selling price is valid but requires an `N/A` margin to avoid division by zero.
- Valid input produces formatted business outputs and exactly one final status.

## 2026-08-07 - Friday Review #2: PurrNest Financial Decision System

### Session Evidence

- Date: 2026-08-07
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge-Check Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Financial Decision System
- Final status: Passed
- Verified skills: `float()`, comparisons, `if` / `elif` / `else`, `or`, validation order, arithmetic, profit-margin percentage calculation, zero-division protection, two-decimal formatting, business-rule execution, and exactly one status for valid input
- Code personally written: Yes; the student personally wrote the complete financial decision system core logic
- Errors encountered: Knowledge-check answers initially miscalculated a percentage, gave the wrong reason for protecting a zero selling price, and answered with a label instead of the requested status count; the first exercise implementation nested status classification inside the nonzero-margin branch; a revision temporarily rejected zero by using `<= 0`; and the status chain needed repeated indentation correction
- Corrections understood: Profit margin is calculated by division followed by multiplication by 100; zero cannot be a divisor; one `if` / `elif` / `else` chain prints one status; `< 0` rejects only negative values while allowing zero; the status chain must execute after either margin branch but only for validated input; and `or` makes the validation condition true when any field is negative
- Tests performed: `20 / 10 / 2` -> `RM12.00`, `RM8.00`, `40.00%`, `PROFIT`; `12 / 10 / 2` -> `RM12.00`, `RM0.00`, `0.00%`, `BREAK-EVEN`; `10 / 10 / 2` -> `RM12.00`, `RM-2.00`, `-20.00%`, `LOSS`; `0 / 0 / 0` -> `RM0.00`, `RM0.00`, `N/A`, `BREAK-EVEN`; `-1 / 10 / 2` and `10 / -5 / 2` -> only `INVALID INPUT`; student-designed `-3 / 9 / 2` -> only `INVALID INPUT`. Every valid run displayed exactly one final status
- Codex review result: Passed through the corrected ten-question knowledge check, final static inspection, seven correct student-reported manual tests, exact output and validation-path review, and an understanding check covering boundary choice, indentation, and `or` behavior
- Files created or modified: `exercises/module_01/friday_review_02_purrnest_financial_decision_system.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

### Concepts Demonstrated

- Validation must reject negative data before any calculations or business outputs.
- Zero is a valid boundary and requires separate protection only when used as a divisor.
- `or` combines field checks so one negative value invalidates the complete input set.
- Margin decisions and status decisions serve different purposes and require the correct indentation.
- Valid input produces one formatted financial result and exactly one classification.

## 2026-08-08 - PurrNest Shopee Order Profit Calculator, Stage 1B

### Session Evidence

- Date: 2026-08-08
- Day of week: Saturday
- Session type: Shopee / TikTok Business Application Day
- Available time: 30 minutes
- Lesson or business feature: Quantity and Multiple-Unit Order Calculation
- Final status: Passed
- Verified skills: Quantity input using `int()`, money inputs using `float()`, zero/negative quantity validation, negative money validation, validation-before-calculation order, total sales revenue, total product cost, total order cost, net profit, two-decimal formatting, and exactly one order status
- Code personally written: Yes; the student personally wrote the complete Stage 1B core implementation
- Errors encountered: The first student-designed Test 4 data produced `RM17.00` profit and `PROFITABLE` instead of the required loss; the first explanation called selling price multiplied by quantity total profit instead of total sales revenue
- Corrections understood: Total order cost must exceed total sales revenue to create a loss; selling price per unit multiplied by quantity calculates total sales revenue; product cost per unit multiplied by quantity calculates total product cost; packaging cost, Shopee fee, seller discount, and other cost apply once to the order in Stage 1B; and invalid quantity must be rejected before financial processing
- Tests performed: Test 1 -> `RM45.00`, `RM18.00`, `RM23.00`, `RM22.00`, `PROFITABLE`; Test 2 -> `RM10.00`, `RM6.00`, `RM8.00`, `RM2.00`, `PROFITABLE`; Test 3 -> `RM20.00`, `RM16.00`, `RM20.00`, `RM0.00`, `BREAK-EVEN`; corrected student-designed Test 4 using `25 / 2 / 18 / 6 / 5 / 0 / 5` -> `RM50.00`, `RM36.00`, `RM52.00`, `RM-2.00`, `LOSS`; Tests 5-7 for zero quantity, negative quantity, and negative packaging cost each produced only `INVALID INPUT`
- Codex review result: Passed through final static inspection, seven student-reported manual tests, validation-path and scope review, exact output-format verification, and an understanding check
- Files created or modified: `shopee_order_profit_calculator/stage_1b_quantity_profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start Stage 1C; wait for the Daily Learning Supervisor / SaaS Product Builder to generate the final progress report

### Concepts Demonstrated

- Whole-unit quantity is converted with `int()`, while monetary inputs use `float()`.
- Per-unit selling price and product cost are multiplied by quantity to produce order totals.
- Per-order costs are added once when calculating total order cost.
- Validation prevents impossible quantity and negative money data from reaching financial output.
- One conditional chain produces exactly one profitable, break-even, or loss status.

## 2026-08-10 - Module 1, Lesson 13: Introduction to `while` Loops

### Session Evidence

- Date: 2026-08-10
- Day of week: Monday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Low Stock Countdown
- Final status: Passed
- Verified skills: Basic `while` condition, condition checking before each repetition, stock decrement, loop-state change, loop termination, infinite-loop recognition, negative-stock validation, zero-stock handling, indentation, and required output order
- Code personally written: Yes; the student personally wrote the complete exercise implementation using only the allowed Python concepts
- Errors encountered: The first Test 3 report for input `1` listed only `Out of Stock`; the first explanation of removing the stock decrement did not explicitly identify that the repeated true condition creates an infinite loop
- Corrections understood: A positive stock is printed before being decreased; `stock_quantity -= 1` is equivalent to assigning the current stock minus one; reaching zero makes `stock_quantity > 0` false; and without a state change the same positive stock would be printed continuously in an infinite loop
- Tests performed: `-1` -> `Invalid Stock`; `0` -> `Out of Stock`; `1` -> `Stock Remaining: 1`, `Out of Stock`; `3` -> `Stock Remaining: 3`, `2`, `1`, `Out of Stock`; student-selected `5` -> `Stock Remaining: 5`, `4`, `3`, `2`, `1`, `Out of Stock`
- Codex review result: Passed through final static inspection, five correct student-reported manual tests, while-condition and decrement review, indentation and output-order verification, scope compliance review, and a two-question understanding check
- Files created or modified: `exercises/module_01/lesson_13_purrnest_low_stock_countdown.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start another lesson; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A `while` loop checks its condition before every repetition.
- Positive stock enters the countdown, while negative and zero stock follow separate paths.
- Changing the stock variable causes the condition to eventually become false.
- Code after the loop runs once after the countdown finishes.
- A condition that remains true forever creates an infinite loop.

## 2026-08-12 - Module 1, Lesson 14: Using `while` Loops for Input Validation

### Session Evidence

- Date: 2026-08-12
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Stock Input Retry
- Final status: Passed
- Verified skills: Input validation with `while`, invalid-state conditions, first input before the loop, new input inside the loop, controlling-variable update, repeated retries, loop termination, infinite-loop recognition, indentation, and final accepted-value output
- Code personally written: Yes; the student personally wrote the complete exercise implementation using only the allowed Python concepts
- Errors encountered: The initial knowledge-check answer described only the example-specific condition instead of the general while rule, and the initial false-condition answer confused repeating with leaving the loop; the submitted implementation required no correction
- Corrections understood: Python repeats the loop body while its condition is true; negative stock is invalid and keeps the loop active; `0` and positive stock make the condition false; reading into the same variable allows the next condition check to use fresh input; and omitting that new input would preserve the negative value and repeat forever
- Tests performed: `0` -> `Valid Stock: 0`; `5` -> `Valid Stock: 5`; `-1, 3` -> `Invalid Stock`, `Valid Stock: 3`; `-5, -2, -1, 10` -> three invalid messages followed by `Valid Stock: 10`; student-selected `-3, -5, 0` -> two invalid messages followed by `Valid Stock: 0`
- Codex review result: Passed through a corrected five-question knowledge check, final static code inspection, five correct student-reported manual tests, input-placement and variable-update review, loop-termination and scope checks, and a three-question understanding check
- Files created or modified: `exercises/module_01/lesson_14_purrnest_stock_input_retry.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 15; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A validation loop can describe the invalid state directly in its condition.
- The first value must exist before Python can check the loop condition.
- Requesting a new value inside the loop allows invalid input to be corrected.
- The loop stops naturally when the new value makes its condition false.
- Keeping the same invalid value would cause an infinite loop.

## 2026-08-14 - Friday Review #3: PurrNest Restock Quantity Validator

### Session Evidence

- Date: 2026-08-14
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge-Check Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Restock Quantity Validator
- Final status: Passed
- Verified skills: Translating a business validity rule into an invalid-state `while` condition, rejecting zero and negative quantities, updating the controlling input, repeated validation, natural loop termination, infinite-loop recognition, boundary-condition debugging, indentation, and output order
- Code personally written: Yes; the student personally wrote the complete validator implementation
- Errors encountered: Several initial knowledge-check answers needed correction; the first implementation placed the accepted output inside the loop
- Corrections understood: The loop repeats while its condition is true; the invalid restock range includes zero and negative quantities; replacing the controlling input prevents an infinite loop; and the final output must be outside the loop so it runs once after validation
- Tests performed: `1` -> accepted `1`; `0, 1` -> one invalid message then accepted `1`; `-1, 5` -> one invalid message then accepted `5`; `0, -2, 0, 10` -> three invalid messages then accepted `10`; student-designed `-1, -2, -3, 0, 5` -> four invalid messages then accepted `5`
- Debugging challenge: Passed; the student identified that `< 0` incorrectly accepts zero and explained the correction
- Understanding check: Passed; the student explained the business boundary, invalid repeat range, controlling-variable update, and false-condition termination
- Codex review result: Passed through knowledge check, static inspection, five student-reported manual tests, debugging challenge, understanding check, scope review, and secrets/private-data review
- Files created or modified: `exercises/module_01/friday_review_03_purrnest_restock_quantity_validator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start Lesson 15; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A business validity rule can be reversed to describe the invalid values that keep a validation loop running.
- Zero can be valid in one business context and invalid in another.
- Updating the controlling variable allows the loop condition to be checked against fresh input.
- A valid value makes the loop condition false, allowing execution to continue after the loop.

## 2026-08-15 - PurrNest Shopee Order Profit Calculator, Stage 1B.1

### Session Evidence

- Date: 2026-08-15
- Day of week: Saturday
- Session type: Shopee / TikTok Business Application Day
- Available time: 30 minutes
- Lesson or business feature: Repeated Input Until Valid
- Final status: Passed
- Verified skills: Separate `while` validation for each input, `int()` quantity validation, `float()` money validation, correct zero boundaries, controlling-variable updates, natural termination, preserving valid earlier fields, using corrected values in calculations, infinite-loop recognition, unchanged Stage 1B calculations, two-decimal formatting, and exactly one order status
- Code personally written: Yes; the student personally implemented the seven core retry loops. Codex modified only the version and scope documentation at the student's request
- Errors encountered: Selling Price initially used the wrong zero boundary; the first Packaging Cost test retried Product Cost instead; the first loss-test values produced profit; and the first infinite-loop explanation focused on the boundary rather than a missing variable update
- Corrections understood: Money values repeat only while negative, quantity repeats while zero or negative, every loop must replace its invalid controlling value, valid earlier input remains stored, and loss requires order cost greater than revenue
- Tests performed: Test 1 immediate valid input; Test 2 quantity `0, 2`; Test 3 quantity `-3, -1, 2`; Test 4 Packaging Cost `-2, 2`; Test 5 Packaging Cost `-5, -1, 0`; Test 6 four valid zero order-level money fields; Test 7 Packaging Cost `-2, 4` followed by a loss calculation
- Test results: All seven student-run manual tests passed. Test 7 produced `RM15.00` revenue, `RM8.00` product cost, `RM19.00` order cost, `RM-4.00` net profit, and `LOSS`
- Codex review result: Passed through static inspection, all required student-reported manual tests, boundary and retry-path review, formula and output review, understanding check, scope verification, and sensitive-information review
- Files created or modified: `shopee_order_profit_calculator/stage_1b_quantity_profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start another feature or Stage 1C; wait for the SaaS Product Builder

### Concepts Demonstrated

- Each input can have its own validation loop so one mistake does not restart the complete order entry.
- Quantity and money fields use different zero boundaries because their business rules differ.
- Updating the same variable inside its loop allows fresh input to replace an invalid value.
- Corrected inputs flow into the unchanged Stage 1B calculations and one final order status.

## 2026-08-17 - Module 1, Lesson 15: `while` Loop with an Accumulator

### Session Evidence

- Date: 2026-08-17
- Day of week: Monday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Daily Sales Accumulator
- Final status: Passed
- Verified skills: Initializing an accumulator before a loop, adding each positive order to an existing total, distinguishing replacement from accumulation, repeated input placement, zero-sentinel termination, negative-input exclusion, infinite-loop recognition, and two-decimal money formatting
- Code personally written: Yes; the student personally wrote the complete accumulator implementation. Codex created only the instruction scaffold
- Errors encountered: One knowledge-check answer incorrectly retained earlier values after resetting the accumulator; the first negative check was inside the loop and missed initially negative input; and the first answer about omitting new input said the loop would not execute
- Corrections understood: An accumulator reset inside the loop forgets prior values; zero makes the positive loop condition false; a negative check after positive accumulation covers both initial and later negative input; and an unchanged positive order amount causes an infinite loop that repeatedly adds the same value
- Tests performed: `10, 0` -> `RM10.00`; `10, 20, 5, 0` -> `RM35.00`; initial `0` -> `RM0.00`; `5.50, 4.50, 10, 0` -> `RM20.00`; initial `-5` -> invalid message and `RM0.00`; student-designed `5, 6, 7, 0` -> `RM18.00`
- Negative-input test: Passed; `-5` displayed `Invalid Order Amount`, was not added, and left Total Sales at `RM0.00`
- Understanding check: Passed after correction; the student explained initialization, accumulation versus replacement, reset behavior, zero termination, and missing-input infinite-loop risk
- Codex review result: Passed through knowledge check, static inspection, six student-reported manual tests, negative-input verification, understanding check, AGENTS.md and scope review, and sensitive-information review
- Files created or modified: `exercises/module_01/lesson_15_purrnest_daily_sales_accumulator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 16; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- An accumulator preserves a running total by adding each new value to what is already stored.
- Initializing before the loop prevents earlier accumulated values from being erased.
- Zero can stop a positive-value loop naturally without being added to the total.
- Updating the input inside the loop prevents an unchanged positive value from creating an infinite loop.

## 2026-08-18 - Module 1, Lesson 16: Counter Pattern with `while`

### Session Evidence

- Date: 2026-08-18
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Daily Order Counter
- Final status: Passed
- Verified skills: Initializing a counter at zero, adding exactly one per valid business event, distinguishing counts from accumulated money, using zero as the only sentinel, handling positive and negative paths inside one loop, excluding invalid events, repeated input updates, and preserving prior counts
- Code personally written: Yes; the student personally wrote the complete counter implementation. Codex created only the exercise scaffold and supplied progressive hints
- Errors encountered: One knowledge-check answer missed the valid event after an invalid event; several implementation attempts stopped at negative input or placed retry logic outside the continuing loop; one attempt used an invalid spaced variable name and another used `while ... else`; the student-designed sequence first omitted zero; and two understanding answers needed correction
- Corrections understood: The loop must remain active for every nonzero input; `!=` means not equal and allows zero to be the sole stopping value; only positive orders increment the counter; negative orders display an error and continue; resetting the counter loses previous counts; and failure to update input can cause an infinite loop
- Teaching adjustment: Codex explicitly taught `order_amount != 0` after the student pointed out that using `!=` as a sentinel condition had not been explained before the implementation request
- Tests performed: `0` -> `Total Orders: 0`; `10, 0` -> `1`; `10, 20, 5, 0` -> `3`; `5.50, 4.50, 10, 8, 0` -> `4`; `10, -5, 20, 0` -> invalid message and `2`; student-designed `1, 2, 3, 4, -5, 0` -> invalid message and `4`
- Negative-input test: Passed; negative amounts displayed `Invalid Order Amount`, did not increase the counter, and did not prevent later valid orders from being counted
- Understanding check: Passed after correction; the student explained zero initialization, increment-by-one behavior, invalid-event exclusion, count versus sales total, zero termination, and the effect of resetting inside the loop
- Codex review result: Passed through knowledge check, static inspection, six student-reported manual tests, negative-input verification, understanding check, AGENTS.md and scope review, and sensitive-information review
- Files created or modified: `exercises/module_01/lesson_16_purrnest_daily_order_counter.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 17; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A counter records how many valid events occurred rather than adding their monetary values.
- A nonzero loop condition can process positive and negative input while reserving zero as the sentinel.
- The counter increases only in the positive valid-event branch.
- Initializing the counter before the loop preserves counts from earlier iterations.

## 2026-08-20 - Module 1, Lesson 17: Combining Counter and Accumulator

### Session Evidence

- Date: 2026-08-20
- Day of week: Thursday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Daily Sales Summary
- Final status: Passed
- Verified skills: Maintaining a counter and accumulator in one loop, updating both for a valid order, keeping count and sales value separate, excluding negative input from both, using zero as a sentinel, repeated input updates, natural termination, final output placement, and two-decimal formatting
- Code personally written: Yes; the student personally wrote the complete combined implementation. Codex created only the exercise scaffold
- Errors encountered: Three knowledge-check responses needed completion; the first code attempt left positive `order_amount` unchanged, placed final output inside the loop, and misspelled `Summary`
- Corrections understood: A valid event contributes its monetary amount to `total_sales` and one to `order_count`; invalid input changes neither metric; both positive and negative paths need fresh input; zero ends the loop before updates; and resetting either variable inside the loop destroys prior history
- Tests performed: `0` -> `0` and `RM0.00`; `10, 0` -> `1` and `RM10.00`; `10, 20, 5, 0` -> `3` and `RM35.00`; `5.50, 4.50, 10, 8, 0` -> `4` and `RM28.00`; `10, -5, 20, 0` -> invalid message, `2`, and `RM30.00`; `-5, -10, 0` -> two invalid messages, `0`, and `RM0.00`; student-designed `1, 2, 3, 4, -1, -2, 0` -> two invalid messages, `4`, and `RM10.00`
- Student-designed test: Predicted `4` orders and `RM10.00` before running; actual output matched
- Negative-input verification: Passed; negative amounts displayed `Invalid Order Amount`, changed neither metric, and did not stop later processing
- Understanding check: Passed; the student explained the meaning and update behavior of both metrics, invalid and zero exclusion, termination, and reset consequences
- Codex review result: Passed through knowledge check, static inspection, all seven student-reported manual tests, negative-input verification, understanding check, AGENTS.md and scope review, and sensitive-information review
- Files created or modified: `exercises/module_01/lesson_17_purrnest_daily_sales_summary.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 18; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- One valid event can update both a total value and an event count.
- The accumulator and counter answer different business questions even when updated together.
- Negative input must change neither metric, while zero ends the session without being processed.
- Both variables must be initialized before the loop to preserve earlier results.

## 2026-08-21 - Friday Review #4: PurrNest Daily Order Processing Summary

### Session Evidence

- Date: 2026-08-21
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge-Check Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Daily Order Processing Summary
- Final status: Passed
- Verified skills: Maintaining one accumulator and two distinct counters in one `while` loop, assigning business events to the correct metrics, excluding zero, repeated input updates, natural termination, output placement, infinite-loop recognition, and formatted sales output
- Code personally written: Yes; the student personally wrote the complete core implementation. Codex created only the exercise scaffold
- Errors encountered: Three knowledge-check answers needed correction; two required output labels initially lacked colons; Test 6 initially omitted its invalid-message lines in the report; the debugging challenge first blamed the positive branch; and the understanding check required corrections about initialization and a nonzero condition remaining true
- Corrections understood: Valid positive input changes only Valid Order Count and Total Sales; invalid negative input changes only Invalid Entry Count; zero changes no metric; negative amounts cannot be subtracted from sales; metrics initialized outside the loop retain earlier results; final results print after processing; and missing repeated input can cause an infinite loop
- Tests performed: `0` -> `0 / 0 / RM0.00`; `10, 0` -> `1 / 0 / RM10.00`; `-5, 0` -> one invalid message and `0 / 1 / RM0.00`; `10, -5, 20, 0` -> `2 / 1 / RM30.00`; `10, -5, 20, -2, 5, 0` -> `3 / 2 / RM35.00`; `-1, -2, -3, 0` -> three invalid messages and `0 / 3 / RM0.00`; student-designed `1, 2, 3, 4, -5, -6, -7, 0` -> `4 / 3 / RM10.00`
- Student-designed test: Predicted all three metrics correctly before running; actual output matched
- Debugging challenge: Passed after correction; the student located the negative-sales update bug, calculated the incorrect `25`, and identified Invalid Entry Count as the only permitted update
- Understanding check: Passed after correction; the student explained separate metrics, valid and invalid updates, zero sentinel behavior, initialization, final output placement, and infinite-loop risk
- Codex review result: Passed through knowledge check, static inspection, all required manual tests, prediction verification, debugging challenge, understanding check, AGENTS.md and scope review, and sensitive-information review
- Files created or modified: `exercises/module_01/friday_review_04_purrnest_daily_order_processing_summary.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 18 or another exercise; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- Separate counters can classify valid and invalid events within one processing loop.
- Each business event must update only the metrics defined by its rule.
- The zero sentinel ends processing without affecting counts or totals.
- Fresh input on every nonzero path prevents repeated processing and infinite loops.

## 2026-08-22 - PurrNest Shopee Order Profit Calculator, Stage 1B.2

### Session Evidence

- Date: 2026-08-22
- Day of week: Saturday
- Session type: Shopee / TikTok Business Application Day
- Available time: 30 minutes
- Tool name: PurrNest Shopee Order Profit Calculator
- Previous version: Stage 1B.1 - Repeated Input Until Valid
- Current feature: Stage 1B.2 - Multi-Order Session Summary
- Final status: Passed
- Verified features: Multiple valid orders in one run, preserved per-order validation and formulas, per-order status output, session order counter, session revenue and net-profit accumulators, invalid-retry isolation, yes/no control, natural outer-loop termination, and final two-decimal Session Summary
- Code personally written: Yes; the student personally wrote the complete Stage 1B.2 core flow. Codex updated only documentation labels after the implementation passed
- Errors encountered: Session metrics were initially confused with per-order calculations; the count variable was singular; the first outer-loop attempt prompted before the first order and did not indent the order flow; yes/no placement required clarification; Session Summary was initially inside the loop and contained output-label and variable-expression errors
- Corrections understood: Per-order values and session totals serve different scopes; all session metrics initialize once before the outer loop; the complete existing calculator repeats; updates occur only after a valid order; yes/no must update after each order; and the summary prints once after processing ends
- Tests performed: One profitable order `1 / RM30.00 / RM14.00`; two profitable orders `2 / RM40.00 / RM16.00`; profitable-plus-loss scenario `2 / RM30.00 / RM7.00`; three-order session `3 / RM70.00 / RM30.00`; invalid Quantity retry counted once; invalid Packaging Cost retry counted once; student-designed three-order mixed-status scenario with invalid retry `3 / RM70.00 / RM30.00`
- Test 3 prediction note: The student ran the scenario before submitting predictions and explicitly requested that the repeat-prediction portion be waived due to time; the actual calculations and session totals were correct
- Student-designed test: Predicted and produced three processed orders, `RM70.00` Session Total Sales Revenue, and `RM30.00` Session Total Net Profit, with an invalid Quantity retry, two profitable orders, and one loss order
- Understanding check: Passed; the student explained counter versus accumulators, valid-order update timing, invalid-retry isolation, repeated calculation flow, preservation across orders, and final-summary placement
- Codex review result: Passed through static code inspection, all seven student-reported functional tests, formula and validation preservation checks, session control review, understanding check, AGENTS.md and scope verification, and sensitive-information review
- Files created or modified: `shopee_order_profit_calculator/stage_1b_quantity_profit_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not start another feature or Stage 1C; wait for the Daily Learning Supervisor / SaaS Product Builder

### Concepts Demonstrated

- An outer `while` loop can repeat a complete validated single-order workflow.
- Session counters and accumulators update once after each valid order is fully calculated.
- Invalid field retries remain inside one order and do not affect session-level metrics.
- A control string updated after each order allows natural session termination and one final summary.

## 2026-08-24 - Module 1, Lesson 18: Average from Counter and Accumulator

### Session Evidence

- Date: 2026-08-24
- Day of week: Monday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Average Order Value Calculator
- Final status: Passed
- Verified skills: Deriving Average Order Value from Total Sales and Total Orders, interpreting totals versus averages, protecting zero-count division, producing `N/A`, excluding negative input from both source metrics, calculating after the input loop, and formatting a numeric average to two decimal places
- Code personally written: Yes; the student personally wrote the complete implementation. Codex created only the exercise scaffold
- Errors encountered: Knowledge-check answers initially treated division by zero as zero and confused average sales with profit; average calculation was first inside the loop; the final no-order output initially omitted the Average Order Value line; and understanding answers required clarification about sentinel behavior, final-data timing, and average distortion
- Corrections understood: Average uses total divided by valid count; dividing by zero raises an error; no valid orders display `N/A`; final total and count are known after the loop; negative inputs affect neither input metric; and an incorrectly increased denominator lowers the calculated average
- Tests performed: `0` -> `0 / RM0.00 / N/A`; `10, 0` -> `1 / RM10.00 / RM10.00`; `10, 20, 30, 0` -> `3 / RM60.00 / RM20.00`; `5.50, 4.50, 10, 0` -> `3 / RM20.00 / RM6.67`; `10, -5, 20, 0` -> invalid message and `2 / RM30.00 / RM15.00`; `-5, -2, 10, 20, 0` -> two invalid messages and `2 / RM30.00 / RM15.00`; student-designed `1, 2, 3, 4, -5, -6, 0` -> two invalid messages and `4 / RM10.00 / RM2.50`
- Student-designed test: Predicted all three final metrics correctly before running; actual output matched
- Zero-order test: Passed; the program skipped division and displayed `Average Order Value: N/A`
- Negative-input verification: Passed; invalid negative values changed neither Total Sales nor Total Orders
- Understanding check: Passed after correction; the student explained the two average inputs, division, invalid exclusion, sentinel behavior, zero protection, post-loop timing, and denominator distortion
- Codex review result: Passed through knowledge check, static inspection, all seven student-reported manual tests, zero-order and negative-input checks, understanding check, AGENTS.md and scope review, and sensitive-information review
- Files created or modified: `exercises/module_01/lesson_18_purrnest_average_order_value_calculator.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 19; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A derived average requires both a completed accumulator and its valid-event count.
- Zero-count protection must occur before division.
- Invalid events must not alter either source metric used by the average.
- Calculating after the loop uses the complete session totals.

## 2026-08-25 - Module 1, Lesson 19: Tracking the Highest Value

### Session Evidence

- Date: 2026-08-25
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Highest Order Value Tracker
- Final status: Passed
- Verified skills: Initializing a running maximum, comparing new valid values, replacing only for a larger amount, retaining the previous maximum for smaller or equal input, excluding negatives, using zero as a sentinel, producing `N/A` when no valid order exists, and formatting the highest money value
- Code personally written: Yes; the student personally wrote the complete implementation. Codex created only the exercise scaffold
- Errors encountered: Two knowledge-check answers required correction for the intermediate maximum sequence and no-order behavior; the code contained a harmless unnecessary self-assignment; and the no-order understanding answer needed clarification
- Corrections understood: Highest value means the largest valid amount seen so far; only a greater positive amount replaces it; negative input and zero cannot participate; no valid order displays `N/A`; and unconditional replacement would incorrectly return the last valid amount
- Tests performed: `0` -> `N/A`; `10, 0` -> `RM10.00`; `10, 30, 20, 0` -> `RM30.00`; `5, 10, 25, 0` -> `RM25.00`; `5.50, 9.99, 7.25, 0` -> `RM9.99`; `10, -100, 20, 0` -> invalid message and `RM20.00`; `50, 10, 20, 0` -> `RM50.00`; student-designed `1, 2, 3, 4, 5, -6, -7, 0` -> two invalid messages and `RM5.00`
- Student-designed test: Predicted `RM5.00`; actual output matched
- No-order test: Passed; sentinel-only input displayed `Highest Order Value: N/A`
- Negative-input verification: Passed; negative values displayed errors and did not affect the maximum
- Understanding check: Passed after clarification; the student explained stored information, update conditions, smaller/equal preservation, invalid exclusion, sentinel behavior, no-order output, and the last-value bug
- Codex review result: Passed through knowledge check, static inspection, all eight student-reported manual tests, no-order and negative-input checks, understanding check, AGENTS.md and scope review, verification that `max()` was not used in implementation code, and sensitive-information review
- Files created or modified: `exercises/module_01/lesson_19_purrnest_highest_order_value_tracker.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Do not introduce Lesson 20; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A running maximum stores the largest valid value seen so far.
- A new value replaces the stored maximum only when it is greater.
- Invalid and sentinel values must not participate in maximum tracking.
- A no-valid-event check prevents the initial placeholder from being reported as real data.

## 2026-08-31 - Module 1, Lesson 20: Tracking the Lowest Value

### Session Evidence

- Date: 2026-08-31
- Day of week: Monday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson or business feature: PurrNest Lowest Order Value Tracker
- Final status: Passed
- Code personally written: Yes; the student personally wrote and corrected all core implementation logic. Codex created only the exercise scaffold
- Knowledge check: Passed all six prediction questions; for `30, 10, 20`, the student correctly predicted running lowest values `30, 10, 10`
- Verified skills: Running minimum, first-valid-value handling, comparison-based replacement using `<`, equal/larger preservation, negative-input exclusion, zero sentinel, no-valid-data handling with `N/A`, natural loop termination, and two-decimal money formatting
- Manual tests: All nine required tests passed based on student-run output
- Student-designed test: Input `1, 2, 3, 4, 5, -6, -7, 0`; predicted and produced two invalid messages and `Lowest Order Value: RM1.00`
- No-order test: Passed with `Lowest Order Value: N/A`
- Negative-input verification: Passed; `-100`, `-6`, and `-7` did not participate in minimum calculation
- Zero-sentinel verification: Passed; zero stopped input and was not stored as a real order
- Errors encountered: Repeated input was temporarily placed only under the non-update branch, creating an infinite-loop risk after a new minimum; indentation was initially inconsistent; and the comparison-direction answer initially lacked the actual operators
- Corrections understood: Every loop path must update the controlling input; nested blocks use consistent four-space indentation; a smaller positive value replaces the minimum; larger/equal values preserve it; Lesson 19 uses `>` and Lesson 20 uses `<`
- Understanding check: Passed all nine questions after the final operator clarification
- Codex review: Passed static logic, control-flow, formatting, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_20_purrnest_lowest_order_value_tracker.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Next confirmed task: Do not introduce Lesson 21; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A running minimum stores the smallest valid value seen so far.
- The first valid positive value must establish a real minimum before later comparisons.
- Only a smaller valid value replaces the stored minimum.
- Invalid values and the zero sentinel must not participate in minimum tracking.

## 2026-09-01 - Module 1, Lesson 21: Tracking Highest and Lowest Together

### Session Evidence

- Date: 2026-09-01
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 21
- Exercise: PurrNest Order Value Range Tracker
- Final status: Passed
- Code personally written: Yes; the student wrote and corrected all core implementation logic. Codex created only the exercise scaffold
- Knowledge check: Passed six prediction questions, including both running states after every value in `20, 5, 30, 10`
- Verified skills: Maintaining Highest and Lowest in one loop, first-valid-value establishment, independent comparison directions, middle/equal preservation, invalid exclusion, zero sentinel, two-output no-data handling, and money formatting
- Manual tests: All nine required tests passed based on student-run output
- Student-designed test: Input `1, 2, 3, 4, 5, -6, -7, 0`; predicted and produced two invalid messages, Highest `RM5.00`, and Lowest `RM1.00`
- First-valid-value verification: Passed; input `10, 0` produced `RM10.00` for both metrics
- No-order test: Passed; input `0` produced `Highest Order Value: N/A` and `Lowest Order Value: N/A`
- Negative-input verification: Passed; `-100`, `-50`, `-6`, and `-7` did not affect either state
- Zero-sentinel verification: Passed; zero naturally ended processing and affected neither result
- Errors encountered: Indentation initially used six spaces, then mixed three/six/twelve spaces; the first response about simultaneous updates discussed the first order rather than later established ranges
- Corrections understood: VS Code `Spaces: 4` plus Tab/Shift+Tab produces consistent levels; every valid input needs two independent comparisons; after the first value, a new input cannot simultaneously be greater than Highest and less than Lowest
- Understanding check: Passed all nine questions after the simultaneous-update clarification
- Codex review: Passed static logic, control-flow, indentation, output, scope, prohibited-method, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_21_purrnest_order_value_range_tracker.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 21 order value range tracker`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 22; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- One valid input can be evaluated independently against multiple stored states.
- The first valid input establishes both ends of an initially empty range.
- Later values may update one end or neither end, but cannot update both ends of an established valid range.
- Invalid values and the sentinel must not alter either stored extreme.

## 2026-09-02 - Module 1, Lesson 22: Calculating Order Value Spread

### Session Evidence

- Date: 2026-09-02
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 22
- Exercise: PurrNest Order Value Spread Analyzer
- Final status: Passed
- Code personally written: Yes; the student personally wrote all core Highest, Lowest, Spread, control-flow, and output logic. Codex created only the exercise scaffold
- Knowledge check: Passed six prediction questions covering endpoints, subtraction, equal endpoints, decimal values, no valid data, and invalid-negative exclusion
- Verified skills: Calculating a derived range after repeated processing, using `Highest - Lowest`, preserving Lesson 21 endpoint logic, zero Spread, no-data protection, invalid-input isolation, zero sentinel, and formatted output
- Manual tests: All eight required tests passed based on student-run output
- Student-designed test: Input `1, 2, 3, 4, 5, -6, -7, 0`; predicted and produced two invalid messages, Highest `RM5.00`, Lowest `RM1.00`, and Spread `RM4.00`
- One-order test: Passed; `10, 0` produced Highest and Lowest `RM10.00` and Spread `RM0.00`
- No-order test: Passed; initial `0` produced `N/A` for Highest, Lowest, and Spread
- Negative-input verification: Passed; negative values affected no endpoint or derived result
- Zero-sentinel verification: Passed; zero ended the session and did not affect any metric
- Errors encountered: The first understanding response claimed one value could not be subtracted and gave an incomplete reason for post-loop calculation
- Corrections understood: Equal endpoints can be subtracted and produce zero; final endpoints are known after the loop, so the final Spread belongs after repeated processing
- Understanding check: Passed all eight questions after correcting the one-value and calculation-timing explanations
- Codex review: Passed static logic, calculation placement, control flow, output, scope, prohibited-method, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_22_purrnest_order_value_spread_analyzer.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 22 order value spread analyzer`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 23; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A derived Spread depends on correctly maintained final Highest and Lowest endpoints.
- One valid value establishes equal endpoints, naturally producing a zero Spread.
- Final derived metrics should use the completed state after repeated input ends.
- No-data and invalid-data cases must not produce a fake numeric range.

## 2026-09-03 - Module 1, Lesson 23: Conditional Counter

### Session Evidence

- Date: 2026-09-03
- Day of week: Thursday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 23
- Exercise: PurrNest High-Value Order Rate Tracker
- Final status: Passed
- Code personally written: Yes; the student personally wrote all counter, threshold, loop, rate, and output logic. Codex created only the exercise scaffold
- Knowledge check: Passed seven questions after correcting the scope of Total Orders
- Verified skills: Counting a normal counter from a conditional counter, inclusive-boundary classification, percentage calculation two completed counters, preventing division by zero, invalid-input exclusion, zero sentinel, and formatted percentage output
- Manual tests: All nine required tests passed based on student-run output
- Student-designed test: Input `5, 15, 18, 20, 25, 30, -7, -8, 0`; predicted and produced two invalid messages, Total Orders `6`, High-Value Orders `3`, and High-Value Rate `50.00%`
- Boundary verification: Passed; RM20 was included by `>= 20.00`, while RM19.99 was excluded
- No-order test: Passed; input `0` produced both counters as zero and `High-Value Rate: N/A`
- Negative-input verification: Passed; negative values changed neither counter
- Zero-sentinel verification: Passed; zero naturally stopped processing without changing either counter
- Errors encountered: Total Orders was initially described as counting only valid values below RM20; the reason for checking Total Orders before rate calculation initially omitted division-by-zero protection
- Corrections understood: Total Orders includes all positive valid orders; qualifying orders form a subset; a zero denominator would fail with a division-by-zero error, so the program skips division and prints `N/A`
- Understanding check: Passed all ten questions after the zero-denominator clarification
- Codex review: Passed static logic, counter placement, boundary behavior, rate calculation, control flow, output, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_23_purrnest_high_value_order_rate_tracker.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 23 high-value order rate tracker`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 24; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A normal counter records every valid event, while a conditional counter records only a qualifying subset.
- An inclusive threshold requires careful boundary handling at exactly RM20.00.
- A rate can be calculated after both counters are complete and the denominator is confirmed nonzero.
- Invalid input and the sentinel must affect neither the total nor conditional count.

## 2026-09-04 to 2026-09-07 - Friday Review #5

### Session Evidence

- Date started: 2026-09-04
- Date completed: 2026-09-07
- Day: Friday review resumed and completed on Monday
- Session type: Review, Debugging, and Knowledge-Check Day
- Available time at start: 30 minutes
- Review: Friday Review #5
- Exercise: PurrNest Daily Order Analytics Summary
- Final status: Passed
- Code personally written: Yes; the student personally wrote and corrected the combined analytics implementation. Codex provided the exercise scaffold and progressive review hints only
- Knowledge check: Passed after correcting Counter/Accumulator meaning, the Lowest direction, and normal versus conditional counter behavior
- Verified skills: Five raw metrics and three derived metrics in one `while` flow, valid-event updates, conditional counting, Highest/Lowest tracking, Average, Rate, Spread, boundary handling, invalid exclusion, no-data protection, sentinel termination, and formatted reporting
- Manual tests: All seven required tests passed based on student-run outputs
- Student-designed test: `10, 10, 10, 20, 30, 40, -1, -2, 0`; after correcting the pre-run valid count and calculations, predicted and produced Total Orders `6`, Total Sales `RM120.00`, Average `RM20.00`, High-Value Orders `3`, Rate `50.00%`, Highest `RM40.00`, Lowest `RM10.00`, Spread `RM30.00`, and two invalid messages
- Boundary verification: Passed with `19.99`, `20.00`, and `20.01`; only the latter two were High-Value
- No-order test: Passed with zero counts/sales and `N/A` for Average, Rate, Highest, Lowest, and Spread
- Negative-input verification: Passed; invalid negatives changed no metric
- Debugging challenge: Passed; the student found a missing threshold guard around High-Value counter updates, predicted the overcount, and restored the RM20-inclusive rule
- Errors encountered: Invalid currency syntax in initialization, positive-path infinite-loop risk, amount states incremented as counters, mismatched variable naming, inaccurate output labels, missing prompt punctuation, and an initially incorrect student-test denominator
- Corrections understood: Keep currency symbols in display text; update loop control on all paths; assign order amounts to extreme-value states; use consistent names and exact labels; exclude invalid inputs from all metrics; calculate Average and Rate using only valid orders
- Understanding check: Passed all ten questions after adding Spread to the derived list and clarifying independent comparison conditions
- Codex review: Passed static logic, control flow, all required metrics, formulas, formatting, test evidence, debugging, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/friday_review_05_purrnest_daily_order_analytics_summary.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Friday Review 5 daily order analytics summary`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not start Lesson 24 or another exercise; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- Raw metrics update during valid-event processing; derived metrics use the completed raw state after the loop.
- Counters, accumulators, conditional counters, and running extremes can coexist in one controlled input flow.
- Invalid input and the sentinel must not contaminate any business metric.
- Correct denominators and endpoints determine the accuracy of every derived result.

## 2026-09-08 - Module 1, Lesson 24: Introduction to `for` and `range()`

### Session Evidence

- Date: 2026-09-08
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 24
- Exercise: PurrNest 5-Day Sales Tracker
- Final status: Passed
- Code personally written: Yes; the student personally built the implementation in small steps. Codex created the scaffold and provided progressive hints without inserting the solution
- Knowledge check: Passed seven questions after clarifying the loop variable and fixed-range versus condition-based termination
- Verified skills: Basic `for` loop, `range(1, 6)`, exclusive stop value, automatic loop-variable advancement, dynamic day prompt, same-day `while` validation, valid-value accumulation, fixed-denominator average, and two-decimal money formatting
- Manual tests: All seven required tests passed based on student-run output
- Student-designed test: The student predicted `RM21.00 / RM4.20` before a qualifying five-valid-day run with two negative retries, and the actual metrics matched. A later distinct sequence `1, 2, 3, -4, -5, 6, 7` produced the mathematically correct `RM19.00 / RM3.80`; Codex acknowledged its own earlier incorrect sum and did not require another rerun
- Fixed-iteration verification: Passed; exactly five valid day values were processed using Day 1 through Day 5
- Negative-retry verification: Passed; both one-retry and multiple-retry scenarios kept the same day and excluded invalid amounts
- Errors encountered: Missing initialization and colon, output used instead of input, hard-coded day number, misplaced loop variable, missing parentheses, missing f-string prefixes, and imprecise conceptual explanations
- Corrections understood: A known count fits `for`; `range()` excludes its stop value; the loop variable changes automatically; same-day retry uses `while`; accumulation happens once after validation; final calculation and output belong after the `for`
- Understanding check: Passed all eight questions after clarifying current-day representation and why invalid attempts cannot consume a fixed day
- Codex review: Passed static syntax, fixed iteration, validation nesting, accumulator placement, calculation, output, matching prediction evidence, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_24_purrnest_5_day_sales_tracker.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 24 five-day sales tracker`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 25; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A `for` loop is well suited to a known number of repetitions.
- `range(1, 6)` supplies the five day numbers while excluding the stop value.
- A nested validation `while` can repeat an unknown number of attempts without advancing the outer day.
- Accumulation after validation ensures exactly five valid values contribute to the result.

## 2026-09-09 - Module 1, Lesson 25: Conditional Counter inside `for`

### Session Evidence

- Date: 2026-09-09
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 25
- Exercise: PurrNest 7-Day Sales Target Tracker
- Final status: Passed
- Code personally written: Yes; the student personally wrote all core implementation logic. Codex created the scaffold and provided progressive review hints only
- Knowledge check: Passed seven questions after correcting threshold wording and same-day retry reasoning
- Verified skills: Seven fixed iterations, loop-variable prompts, nested validation, accumulator plus conditional counter, inclusive RM20 target, fixed-day rate, rounding, and formatted output
- Manual tests: All seven required tests passed based on student-run output
- Student-designed test: Day 1 inputs `-1, -2, 10`, followed by valid days `10, 30, 40, 50, 60, 70`; produced Total Sales `RM270.00`, Target Days `5`, and Target Hit Rate `71.43%`
- Fixed-iteration verification: Passed; invalid inputs did not reduce the seven valid days
- Boundary verification: Passed with `19.99`, `20.00`, and `20.01`
- Negative-retry verification: Passed with invalid attempts on the same day and across different days
- Errors encountered: Missing f-string prefixes in prompts, missing percentage formatting, truncated instead of rounded Rate prediction, and imprecise explanations of same-day retry and metric types
- Corrections understood: Use f-strings for the current day, `.2f` for Rate, standard rounding for `71.428...`, `while` to preserve the current `for` iteration, and distinct money versus count variables
- Understanding check: Passed all ten questions after two clarifications
- Codex review: Passed static syntax, seven-iteration behavior, validation, accumulator, conditional counter, boundary, rate, formatting, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_25_purrnest_7_day_sales_target_tracker.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 25 seven-day sales target tracker`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 26; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A fixed `for` loop can update both an accumulator and a conditional counter for each valid record.
- An inner validation `while` protects the current iteration from invalid attempts.
- Inclusive business thresholds require the boundary value to qualify.
- A fixed-period rate uses the known number of valid periods as its denominator.

## 2026-09-10 - Module 1, Lesson 26: Associated State Tracking

### Session Evidence

- Date: 2026-09-10
- Day of week: Thursday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 26
- Exercise: PurrNest 7-Day Best Sales Day Tracker
- Final status: Passed
- Code personally written: Yes; the student personally wrote and corrected all core implementation logic. Codex created the scaffold and provided progressive hints only
- Knowledge check: Passed seven questions plus a four-day state prediction
- Verified skills: Highest value plus associated label, synchronized updates, first-valid-day handling, strict comparison, earliest tie rule, all-zero behavior, same-day retry, and final stored-state output
- Manual tests: All seven required tests passed based on student-run output
- Student-designed test: Day 1–4 values `10, 20, 30, 40`; Day 5 retries `-10, -10, 40`; Day 6–7 values `40, 40`; predicted and produced Best Sales Day `Day 4` and Highest Daily Sales `RM40.00`
- Fixed-iteration verification: Passed; seven valid daily values were processed
- First-day initialization verification: Passed with seven zero values producing Day 1 and RM0.00
- Tie verification: Passed in required and student-designed tests; later equal values preserved the earliest maximum day
- Negative-retry verification: Passed on Day 1, Day 3, and Day 5 scenarios
- Errors encountered: Wrong `range` delimiters, leading title whitespace, mixed indentation, incorrect comparison placement and boundary, missing colon, reversed assignments, and output of `day` instead of `best_day`
- Corrections understood: Associated value and label must update together after validation; strict `>` preserves the earliest tie; Day 1 explicitly initializes zero-valued data; the stored label, not the ending loop variable, belongs in final output
- Understanding check: Passed all nine questions after clarifying synchronized association and first-day state establishment
- Codex review: Passed static syntax, validation, state synchronization, first-day and tie behavior, output, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_26_purrnest_7_day_best_sales_day_tracker.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 26 best sales day tracker`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 27; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A business metric may require both a value and the label identifying its source.
- Associated states must update in the same branch to remain synchronized.
- Strict comparison preserves the earliest source when maximum values tie.
- First-record initialization handles valid zero data without relying on a false maximum placeholder.

## 2026-09-11 - Friday Review #6

### Session Evidence

- Date: 2026-09-11
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge-Check Day
- Available time: 30 minutes
- Review: Friday Review #6
- Exercise: PurrNest 7-Day Sales Performance Summary
- Final status: Passed
- Code personally written: Yes; the student personally wrote the complete combined implementation. Codex created the scaffold and used progressive review hints only
- Knowledge check: Passed eight questions and the required seven-day prediction
- Verified skills: Fixed `for` processing, nested input validation, accumulator, conditional counter, Average, percentage, associated maximum tracking, first-day and tie rules, negative-input isolation, and final formatted summary
- Manual tests: All seven required tests passed based on student-run output
- Student-designed test: Final valid values `10, 15, 20, 25, 30, 35, 35` with two Day 5 negative retries; predicted and produced Total Sales `RM170.00`, Average `RM24.29`, Target Days `5`, Rate `71.43%`, Best Day `Day 6`, and Highest `RM35.00`
- Fixed-iteration verification: Passed; invalid attempts did not reduce the seven valid days
- Boundary verification: Passed with `19.99`, `20.00`, and `20.01`
- First-day initialization verification: Passed with all-zero data
- Tie verification: Passed in the required mixed test and student-designed test
- Negative-retry verification: Passed with three attempts across two days and two attempts on one day
- Debugging challenge: Passed; the student identified that `>=` violates earliest-tie behavior, corrected the predicted wrong day to Day 6, and restored strict `>`
- Errors encountered: Inconsistent indentation, an overly nested validation/metric block, missing tie in the first designed scenario, stale arithmetic after modifying that scenario, and initially incomplete debugging and understanding answers
- Corrections understood: Use consistent 4/8-space nesting; keep valid processing outside validation; recalculate dependent metrics after input changes; synchronize value and label; strict comparison preserves the earliest tie
- Understanding check: Passed all ten questions after clarifying associated states and the three metric-update categories
- Codex review: Passed static syntax, control flow, all raw/conditional/associated/derived metrics, all seven tests, debugging, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/friday_review_06_purrnest_7_day_sales_performance_summary.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Friday Review 6 sales performance summary`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not start Lesson 27 or another exercise; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- One fixed processing loop can maintain always-updated, conditionally updated, and associated states together.
- Derived metrics should use the complete raw state after all seven valid records.
- Same-day validation prevents invalid attempts from contaminating metrics or consuming iterations.
- Strict maximum comparison keeps the earliest label when the maximum value ties.

## 2026-09-14 - Module 1, Lesson 27: Associated Minimum State Tracking

### Session Evidence

- Date: 2026-09-14 (completed 2026-09-15)
- Day of week: Monday (continued Tuesday)
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 27
- Exercise: PurrNest 7-Day Worst Sales Day Tracker
- Final status: Passed
- Code personally written: Yes; the student personally wrote all core implementation logic. Codex created the scaffold and used progressive review hints only
- Knowledge check: Passed seven questions plus the required four-day running-state prediction
- Verified skills: Running minimum, synchronized lowest-value/associated-day tracking, first-day initialization, strict comparison, earliest tie preservation, all-zero behavior, same-day retry, fixed iteration, and formatted output
- Manual tests: All seven required tests passed based on student-run output
- Student-designed test: Final valid values `2, 1, 3, 4, 5, 1, 7`, with Day 7 retries `-1, -2, 7`; predicted and produced Worst Sales Day `Day 2` and Lowest Daily Sales `RM1.00`
- Fixed-iteration verification: Passed; invalid attempts did not reduce the seven valid days
- First-day initialization verification: Passed with seven zero values producing Day 1 and RM0.00
- Tie verification: Passed in required and student-designed tests; later equal values preserved the earliest minimum day
- Negative-retry verification: Passed in the required decimal test and student-designed test
- Errors encountered: Two knowledge-check answers initially referenced the wrong state; indentation first used 3/6 spaces and then Tab characters; the final comparison explanation initially lacked full variable order
- Corrections understood: Associated value and day carry different but connected information; both update together; four-space indentation contains no Tab characters; strict `<` tracks the minimum and preserves the earliest tie
- Understanding check: Passed all nine questions after clarifying the stale-day mismatch and exact comparison forms
- Codex review: Passed static control-flow, range, validation, synchronized updates, first-day/tie/all-zero behavior, output formatting, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_27_purrnest_7_day_worst_sales_day_tracker.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 27 worst sales day tracker`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 28; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A minimum business metric can be paired with the day that produced it.
- The minimum value and associated label must update in the same branch.
- Strict `<` comparison preserves the earliest day when minimum values tie.
- First-valid-day initialization correctly handles zero as valid sales data.

## 2026-09-16 - Module 1, Lesson 28: Combined Associated-State Tracking

### Session Evidence

- Date: 2026-09-16
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 28
- Exercise: PurrNest 7-Day Best & Worst Sales Tracker
- Final status: Passed
- Code personally written: Yes; the student personally wrote the combined four-state implementation. Codex created the scaffold and provided progressive review only
- Knowledge check: Passed eight questions and the required four-day state prediction
- Verified skills: Maximum and minimum associated pairs in one loop, independent comparisons, synchronized updates, first-day initialization of four states, earliest maximum/minimum tie handling, middle values, negative retry isolation, and two-decimal output
- Manual tests: All seven required tests passed based on student-run output
- Student-designed test: Final valid values `10, 10, 10, 20, 30, 5, 10`, with negative retries before Day 3 and Day 4; predicted and produced Best Day `Day 5`, Highest `RM30.00`, Worst Day `Day 6`, and Lowest `RM5.00`
- Fixed-iteration verification: Passed; two invalid attempts did not reduce seven valid days
- First-day initialization verification: Passed with all-equal values keeping both associated pairs at Day 1
- Maximum tie verification: Passed in required and student-designed tests
- Minimum tie verification: Passed in required and student-designed tests
- Negative-retry verification: Passed in required and student-designed tests
- Errors encountered: Four trailing spaces remained on the final blank line; the first custom test proposal had one negative retry instead of two
- Corrections understood: Remove whitespace-only trailing lines; distinguish attempts from final valid values; independently compare every valid value with both stored extremes
- Understanding check: Passed all ten questions, including both possible stale-label bugs
- Codex review: Passed static structure, range, validation, four-state initialization and synchronization, independent comparisons, both tie rules, decimals, output, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_28_purrnest_7_day_best_worst_sales_tracker.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 28 best and worst sales tracker`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 29; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- One valid record can be checked independently against both stored extremes.
- Maximum and minimum values each require their own synchronized source label.
- A middle value can leave all four states unchanged.
- Strict comparisons preserve the earliest day for both maximum and minimum ties.

## 2026-09-17 - Module 1, Lesson 29: Derived Sales Spread

### Session Evidence

- Date: 2026-09-17
- Day of week: Thursday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 29
- Exercise: PurrNest 7-Day Sales Range Summary
- Final status: Passed
- Code personally written: Yes; the student personally wrote the complete implementation, including the derived Spread calculation. Codex created the scaffold and used progressive review only
- Knowledge check: Passed seven questions and the required decimal Spread prediction
- Verified skills: Derived metrics from stored states, post-loop calculation, maximum/minimum associated tracking, strict tie rules, negative input isolation, decimal subtraction, and formatted reporting
- Manual tests: All seven required tests passed based on student-run output
- Student-designed test: Final valid values `10, 10, 30, 5, 5, 20, 20`, with two negative retries; predicted and produced Best Day `Day 3`, Highest `RM30.00`, Worst Day `Day 4`, Lowest `RM5.00`, and Spread `RM25.00`
- Fixed-iteration verification: Passed; invalid attempts did not reduce seven valid days
- First-day initialization verification: Passed with all-equal values keeping both labels at Day 1
- Maximum tie verification: Passed in the required tied-extremes test
- Minimum tie verification: Passed in required and student-designed tests
- Negative-retry verification: Passed in required and student-designed tests
- Spread verification: Passed for `RM60.00`, `RM35.00`, `RM0.00`, `RM24.85`, and `RM25.00` cases
- Errors encountered: Misspelled `lowest_sales`; extra spaces in both exact input prompts; initially incomplete definitions of a derived metric and why tie rules still matter
- Corrections understood: Exact variable spelling prevents `NameError`; exact output text includes whitespace; Spread is derived from finalized extremes; ties affect labels even when they do not affect numeric Spread
- Understanding check: Passed all nine questions after two focused corrections
- Codex review: Passed static control flow, exact prompts, range, validation, four-state tracking, post-loop Spread, ties, decimals, output, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_29_purrnest_7_day_sales_range_summary.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 29 seven-day sales range summary`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 30; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- A derived metric is calculated from finalized stored metrics rather than entered directly.
- Sales Spread uses the finalized highest and lowest values after fixed processing.
- Associated dates do not enter the subtraction but must still obey tie rules for accurate reporting.
- Incorrect maximum or minimum state makes every dependent metric inaccurate.

## 2026-09-18 - Friday Review #7

### Session Evidence

- Date: 2026-09-18
- Day of week: Friday
- Session type: Review, Debugging, and Knowledge-Check Day
- Available time: 30 minutes
- Review: Friday Review #7
- Exercise: PurrNest 7-Day Sales Extremes Report
- Final status: Passed
- Code personally written: Yes; the student personally wrote and corrected all core implementation logic. Codex created the scaffold and used progressive hints only
- Knowledge check: Passed eight questions and the required five-result prediction after correcting Spread to `RM35.00`
- Verified skills: Seven-day fixed processing, repeated same-day validation, combined maximum/minimum associated tracking, independent strict comparisons, earliest tie preservation, final Spread calculation, decimals, zero spread, and exact formatted output
- Manual tests: All seven required tests passed based on student-run output
- Student-designed test: Final valid values `10, 5, 20, 20, 5, 5, 30`, with two negative retries on Day 3; predicted and produced Best Day `Day 7`, Highest `RM30.00`, Worst Day `Day 2`, Lowest `RM5.00`, and Spread `RM25.00`
- Fixed-iteration verification: Passed; invalid attempts did not consume a day
- First-day initialization verification: Passed with all-equal values
- Maximum tie verification: Passed in required and student-designed tests
- Minimum tie verification: Passed in required and student-designed tests
- Negative-retry verification: Passed, including two consecutive invalid attempts on the same day
- Spread verification: Passed for integer, decimal, and zero differences
- Debugging challenge: Passed; the student found reversed subtraction, identified the negative business result, calculated `-35`, and restored the correct rule
- Errors encountered: One-time `if` validation, missing f-string prefixes, missing spaces in associated-day output, an incorrect initial Spread prediction, an incomplete debugging result, and uncertainty about the term derived metric
- Corrections understood: Use `while` for repeated retry; f-strings resolve loop variables; exact output spacing matters; Spread is `highest - lowest`; derived metrics use finalized stored values
- Understanding check: Passed all ten questions after one focused review
- Codex review: Passed static control flow, exact seven records, validation, four-state synchronization, independent comparisons, ties, post-loop Spread, formatting, all seven tests, debugging, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/friday_review_07_purrnest_7_day_sales_extremes_report.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Friday Review 7 sales extremes report`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not introduce Lesson 30 or another exercise; wait for the Daily Learning Supervisor

### Concepts Demonstrated

- Review implementation requires rebuilding known logic without receiving the finished structure.
- Repeated validation must use a loop, not a one-time condition.
- Associated values and labels must remain synchronized for both extremes.
- Finalized raw states support a reliable derived Sales Spread.

## 2026-09-19 - PurrNest Profit Calculator Stage 1B.3

### Session Evidence

- Date: 2026-09-19
- Day of week: Saturday
- Session type: Shopee / TikTok Business Application Day
- Available time: 30 minutes
- Tool: PurrNest Shopee Order Profit Calculator
- Previous version: Stage 1B.2 Multi-Order Session Summary
- Current feature: Stage 1B.3 Best & Worst Order Profit Tracking
- Final status: Passed
- Code personally written: Yes; the student personally implemented all new tracking logic and summary output. Codex reviewed and provided progressive guidance only
- Verified features: Highest Net Profit plus Order Number; Lowest Net Profit plus Order Number; first-valid-order initialization; independent later comparisons; earliest-wins ties; all-loss correctness; invalid retry isolation; preserved per-order and session calculations
- Skills applied: Running extrema, associated labels, session counters, accumulators, repeated validation, first-record branching, strict comparison, and formatted reporting
- Tests: Seven functional scenarios passed: one order; three distinct profits; highest tie; lowest tie; all losses; invalid Quantity retry; and a four-order mixed session with invalid Packaging retry
- Student-designed test: Mixed four-order session produced profits `RM4.00, RM10.00, RM-5.00, RM2.00`, Orders Processed `4`, Total Sales `RM47.00`, Total Net Profit `RM11.00`, Highest Order `2 / RM10.00`, and Lowest Order `3 / RM-5.00`
- Prediction note: The student explicitly requested that further pre-run prediction steps be removed; functional results and understanding were verified, and no unperformed prediction is claimed
- Errors encountered: Sales/day terminology carried into order-profit design; negative profit was confused with invalid input; all-loss maximum values were reversed; artificial zero initialization was used first; one output label was misspelled; one tie test was entered incorrectly; version documentation was initially stale
- Corrections understood: Losses are valid calculated orders; real first-order profit is the comparison baseline; `RM-5.00` is higher than `RM-10.00`; value/label pairs update together; strict comparisons preserve earliest orders; final summary follows session termination
- Understanding check: Passed all ten questions after focused corrections
- Codex review: Passed preservation, formulas, validation, session flow, initialization, extrema, labels, ties, all-loss case, invalid isolation, formatting, version documentation, scope, and sensitive-information checks
- Scope review: Passed; no Stage 1C, functions, collections, files, APIs, integrations, sorting, `max()`, `min()`, GUI, dashboard, or SaaS feature added
- Files changed: `shopee_order_profit_calculator/stage_1b_quantity_profit_calculator.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Add Stage 1B.3 order profit extremes tracking`
- Git commit status: Not yet committed
- Git push status: Not yet pushed
- Next confirmed task: Do not start Stage 1C or another feature; wait for the SaaS Product Builder

### Concepts Demonstrated

- The first real business record is a safer extrema baseline than an arbitrary zero.
- A negative Net Profit is a valid loss result, not an invalid input.
- Profit extrema and their Order Numbers are synchronized associated states.
- Session-level extrema are finalized only after repeated order processing ends.

## 2026-09-22 - Module 1, Lesson 30: Final Integration Capstone

### Session Evidence

- Date: 2026-09-22
- Day of week: Tuesday
- Session type: Core Python Learning Day
- Available time: 30 minutes
- Lesson: Module 1 Lesson 30
- Exercise: PurrNest 7-Day Sales Analytics Capstone
- Final status: Passed
- Code personally written: Yes; the student personally wrote the complete nine-metric integration. Codex created the scaffold and used progressive review guidance only
- Knowledge check: Passed ten questions and the required nine-output prediction after correcting Average rounding
- Verified skills: Seven-day `for + range()`, inner `while` validation, Total Sales accumulator, Target Days conditional counter, inclusive boundary, four synchronized associated states, independent extrema checks, first-day and tie rules, Average, Rate, Spread, and formatted final reporting
- Manual tests: All seven required tests passed based on student-run output
- Student-designed test: Valid values `10, 10, 20, 20, 5, 5, 5`, with three negative retries on Day 3; predicted and produced all nine outputs: Total `RM75.00`, Average `RM10.71`, Target Days `2`, Rate `28.57%`, Best `Day 3 / RM20.00`, Worst `Day 5 / RM5.00`, Spread `RM15.00`
- Fixed-iteration verification: Passed; invalid retries did not reduce seven valid records
- Boundary verification: Passed at RM19.99, RM20.00, and RM20.01
- First-day initialization verification: Passed with all-zero data
- Maximum tie verification: Passed in core, tied-extreme, and custom cases
- Minimum tie verification: Passed in core, tied-extreme, decimal, and custom cases
- Negative-retry verification: Passed with two and three retry scenarios
- Average verification: Passed, including standard rounding to `RM17.86`
- Rate verification: Passed, including `42.86%` and `28.57%`
- Spread verification: Passed, including `RM0.00` and `RM24.85`
- Debugging challenge: Passed; the student explained why assignment loses prior Total Sales and restored accumulation
- Errors encountered: Six raw states were initially uninitialized; one Average prediction was truncated; two target metrics were initially missing from a prediction; derived-metric explanation initially focused on timing
- Corrections understood: Initialize before use; distinguish accumulation from replacement; `.2f` rounds; complete analytics require all outputs; derived metrics are calculated from finalized raw metrics
- Understanding check: Passed all twelve questions after one focused correction
- Codex review: Passed static control flow, all raw/associated/derived states, validation, boundary, ties, formatting, seven tests, debugging, scope, prohibited-feature, and sensitive-information checks
- Files changed: `exercises/module_01/lesson_30_purrnest_7_day_sales_analytics_capstone.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Lesson 30 sales analytics capstone`
- Git commit/push status: Committed and pushed as `21e2ab8 Complete Lesson 30 sales analytics capstone`
- Next confirmed task: Do not introduce Lesson 31 or Module 2; wait for the 30-Lesson Technical + Full Portfolio Review and supervisor decision

### Concepts Demonstrated

- One fixed processing flow can maintain accumulated, conditional, and associated raw states together.
- Invalid retries must be isolated before every business metric update.
- Strict independent extrema checks preserve synchronized earliest labels.
- Finalized raw states support multiple reliable derived metrics.

## 2026-09-23 - Module 1 Final Technical and Portfolio Review

### Session Evidence

- Date: 2026-09-23
- Day of week: Wednesday
- Session type: 30-Lesson Technical + Full Portfolio Review
- Available time: 30 minutes
- Assessment: TikTok 6-Video Performance Analyzer
- Final status: MODULE 1 - FORMALLY COMPLETED
- Initial knowledge score: 7 / 12
- Knowledge corrections required: Counter definition, normal versus conditional counters, repeated invalid-input validation, running maximum, and running minimum
- Knowledge correction result: Passed; all five misunderstandings were corrected and explained accurately
- Code personally written: Yes; the student personally wrote the complete assessment logic. Codex created only the requirement file and used progressive hints during review
- Technical assessment result: Passed after student corrections to repeated validation, indentation, first-record initialization, comparison directions, and exact output labels
- Manual tests: 6 / 6 passed
- Student-designed prediction: Passed; all nine predicted outputs matched the execution results (`1850`, `308.33`, `2`, `33.33%`, Video 3 / `500`, Video 6 / `150`, spread `350`)
- Debugging result: Passed; the student identified that `>=` replaces the earliest tied maximum label and corrected the business rule to strict `>`
- Verified skills: Variables, `int()`, arithmetic, comparisons, `if`, repeated `while` validation, `for + range()`, accumulator, conditional counter, running maximum, running minimum, associated labels, first-valid-record initialization, strict comparisons, earliest-wins ties, post-loop derived calculations, average, percentage/rate, spread, and formatting
- Errors encountered: The first validation retried only once; metric updates were temporarily nested under the invalid branch; extrema comparisons were reversed; four output labels initially differed from the specification; the first student-designed dataset lacked a new minimum and its total was miscalculated
- Corrections understood: Validation repeats until valid and metrics follow validation; extrema values and labels update together; strict comparisons preserve earliest ties; output contracts require exact labels; transfer-test constraints and totals must be checked before execution
- Files created or modified: `exercises/module_01/module_01_final_technical_assessment_tiktok_6_video_performance_analyzer.py`, `progress.md`, and `learning_log.md`
- Portfolio audit: Passed for learning evidence; 30 lesson files and 7 Friday Review files are present, historical files are retained appropriately, and the assessment is separate from normal lessons
- Portfolio cleanliness: Non-critical issue noted; `progress.md` has legacy sections in a non-chronological order. The Module 1 summary index and formal status were updated without reorganizing old evidence
- progress.md consistency: Passed after adding Lessons 09-30 to the summary index and marking Module 1 formally completed
- learning_log.md consistency: Passed after reconciling the already-pushed Lesson 30 commit status
- Secrets/private-data check: Passed; no high-confidence secrets, API keys, passwords, tokens, or private keys were found in tracked files
- Git status at review decision: `main` matched `origin/main`; only today's new assessment and learning-record changes were uncommitted
- Evidence quality: Sufficient; includes student-written code, corrections, six manual tests, a nine-output transfer prediction, debugging explanation, repository records, and Git history
- Next confirmed task: Do not start Module 2; wait for the Daily Learning Supervisor / Roadmap Manager to schedule it

### Module Decision

- MODULE 1 - FORMALLY COMPLETED
- Suggested Git commit: `Complete Module 1 final technical and portfolio review`

## 2026-09-24 to 2026-09-25 - Module 2, Lesson 01: Introduction to Lists

### Standardized Lesson Summary

- Date: 2026-09-24 to 2026-09-25
- Day: Thursday to Friday; the Thursday Core Python Learning session was completed the following day
- Module: Module 2 - Structured Data & Reusable Python
- Lesson: Module 2 Lesson 01 - Introduction to Lists - Grouping Related Data
- Exercise: PurrNest 5-SKU Price Editor
- Final status: Passed
- Code personally written: Yes; the student personally created the List, selected indexes, read elements, validated input, replaced SKU 3, and formatted all outputs. Codex created only the instruction scaffold and used progressive hints
- New concepts: List literal syntax, elements, zero-based indexing, indexed reading, and indexed replacement
- Knowledge check: Passed after correcting that a List groups multiple related values in one variable and that `[]` represents the List while contained values are elements; all three index predictions were correct
- Manual tests: 6 / 6 passed
- Student-designed test: Input `20`; predicted and produced SKU 1 `RM12.90`, SKU 3 `RM20.00`, and SKU 5 `RM15.50`
- Index reading verification: Passed; indexes `0`, `2`, and `4` correctly displayed SKU 1, SKU 3, and SKU 5
- Index replacement verification: Passed; `SKU[2]` alone was replaced, while SKU 1 and SKU 5 remained unchanged
- Negative-retry verification: Passed; inputs `-5`, `-1`, and `13.25` produced two invalid messages and finally updated SKU 3 to `RM13.25`
- Index debugging check: Passed; the student explained that `cities[2]` changes the third element and that `cities[1]` is required for the second element
- Understanding check: Passed after distinguishing the whole List (`prices`) from one selected element (`prices[2]`)
- Carry-forward weakness observation: Exact output labels required one correction; conceptual vocabulary required clarification. Validation-loop recall was correct without reteaching. Maximum/minimum comparison direction did not arise naturally in this lesson
- Errors encountered: Non-Python brackets initially caused invalid List syntax; the first print began on the same line; the first version stopped before indexed replacement and final output; output labels initially omitted `Price`; the specified `19.99` test was first run with `19.90`
- Corrections understood: Use English square brackets for List literals; separate statements by line; assign to one indexed element after validation; preserve exact output contracts; run the specified test data exactly; distinguish a whole List from one element
- Codex review: Passed List syntax, five-value order, indexes, reads, SKU 3 replacement, preservation of other elements, repeated negative validation, two-decimal formatting, six manual tests, student prediction, debugging, understanding, student ownership, prohibited-concept scope, and AGENTS.md compliance
- Files changed: `exercises/module_02/lesson_01_purrnest_5_sku_price_editor.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Module 2 Lesson 01 list fundamentals`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not start Module 2 Lesson 02; wait for the Daily Learning Supervisor / Roadmap Manager

## 2026-09-26 - PurrNest Shopee Product Cost and Pricing Tracker Version 0.1

### Standardized Business Tool Session Summary

- Date: 2026-09-26
- Day: Saturday
- Session type: Shopee / TikTok Business Application Day
- Tool name: PurrNest Shopee Product Cost and Pricing Tracker
- Previous business tool status: PurrNest Shopee Order Profit Calculator Stages 1A, 1B, 1B.1, 1B.2, and 1B.3 remain Passed and were not modified; Stage 1C remains undefined
- Current version: Version 0.1
- Current feature: 5-SKU Selling Price Editor
- Final status: Passed
- Code personally written: Yes; the student personally wrote the five-price List, both validation loops, SKU-to-index conversion, indexed reading, indexed replacement, and formatted outputs. Codex created only the requirement scaffold and provided progressive review guidance
- Verified features: Select SKU 1-5, reject repeated out-of-range SKU numbers, display the selected SKU and current price, reject repeated negative prices, accept zero, update only the selected price, and display the updated price
- Skills applied: List literal, zero-based indexing, indexed reading, indexed replacement, `int()`, `float()`, comparisons, `while` validation, arithmetic mapping, f-strings, and `.2f`
- Tests performed: 7 / 7 passed; SKU 1 updated `12.90 -> 13.50`, SKU 3 updated `9.90 -> 11.50`, SKU 5 updated `22.90 -> 25.00`, SKU `0` rejected, SKU `6` rejected, price `-5` rejected before valid zero was accepted, and direct indexed checks confirmed all non-selected prices remained unchanged
- Understanding check: Passed after correcting that index `2` is the third element and therefore maps to SKU 3
- Corrections understood: Repeated SKU validation requires `while`, not one-time `if`; subtracting one maps user-facing SKU numbers to zero-based indexes; index `2` is the third element; assignment to one indexed position preserves every other element; test-only verification output should be removed from the final scoped feature
- Carry-forward observation: Validation-loop recall reappeared in the first SKU validation attempt and was corrected without reteaching Module 1; exact required output labels were correct in the final implementation
- Codex review: Passed List contents/order, zero-based mapping, indexed reading, indexed replacement, selected-only modification, both validation loops, zero-price behavior, money formatting, student ownership, prohibited-concept review, and AGENTS.md compliance
- Scope review: Passed; no List iteration or other unverified concept was used, no extra pricing feature was added, Version 0.2 was not started, and the existing Profit Calculator remained untouched
- Files created or modified: `shopee_product_cost_pricing_tracker/version_0_1_5_sku_selling_price_editor.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Start Shopee pricing tracker with indexed price editing`
- Git commit status: Not yet committed
- Git push status: Not yet pushed
- Next confirmed task: Do not start Version 0.2 or return to Profit Calculator Stage 1C; wait for the SaaS Product Builder to generate the final Business Tool Progress Report

## 2026-10-01 - Module 2, Lesson 02: Iterating Through a List with `for`

### Standardized Lesson Summary

- Date: 2026-10-01
- Day: Thursday
- Module: Module 2 - Structured Data & Reusable Python
- Lesson: Module 2 Lesson 02 - Iterating Through a List with `for`
- Exercise: PurrNest 5-SKU Price Summary
- Final status: Passed
- Code personally written: Yes; the student personally wrote the List, direct iteration loop, processing output, accumulator update, post-loop average, and formatted final outputs. Codex created only the instruction scaffold and provided progressive review guidance
- New concept: Direct List iteration using `for element in list`
- Knowledge check: Passed after clarifying that a List stores a complete collection, direct iteration advances through the List without `range()`, and a running total variable is an accumulator; all three loop-variable predictions were correct
- Manual tests: 6 / 6 passed
- Student-designed test: List `[5, 7, 8, 10, 12]`; predicted and produced processing order `5, 7, 8, 10, 12`, Total `RM42.00`, and Average `RM8.40`
- Direct List iteration verification: Passed; core processing used `for price in prices` without index-based iteration
- Processing order verification: Passed across all six tests; every element appeared once and in List order
- Accumulator verification: Passed; `total_price` was initialized once before the loop and updated from the current element inside the loop
- Average verification: Passed; Average was calculated after processing all five elements using the finalized Total divided by `5`
- Debugging check: Passed after clarifying that initializing an accumulator inside the loop resets it every iteration and leaves only the last element's value
- Understanding check: Passed after distinguishing one indexed read (`prices[2]`) from processing every element through direct iteration
- Carry-forward weakness observation: Conceptual vocabulary precision appeared naturally; the student initially attributed direct iteration to `range()` and described the accumulator without its name, then corrected both. Exact output labels were correct. Validation loops and maximum/minimum directions did not arise in this lesson
- Corrections understood: Python's `for` loop directly retrieves the next List element; an accumulator stores a running total; initialization belongs before the loop; indexed reading selects one position while direct iteration processes the complete List
- Codex review: Passed one-List storage, direct iteration, loop-variable use, five-element processing, order, accumulator placement/update, post-loop Average, two-decimal formatting, student ownership, prohibited-concept review, AGENTS.md compliance, and scope compliance
- Files changed: `exercises/module_02/lesson_02_purrnest_5_sku_price_summary.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Module 2 Lesson 02 list iteration`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not start Module 2 Lesson 03; wait for the Daily Learning Supervisor / Roadmap Manager

## 2026-10-05 - Module 2, Lesson 03: Building a List Dynamically with `append()`

### Standardized Lesson Summary

- Date: 2026-10-05
- Day: Monday
- Tracker ID: JR-19
- Module: Module 2 - Structured Data & Reusable Python
- Lesson: Module 2 Lesson 03 - Building a List Dynamically with `append()`
- Exercise: PurrNest 5-SKU Price Collector
- Final status: Passed
- Code personally written: Yes; the student personally wrote the empty List, fixed five-SKU input loop, repeated validation, append placement, direct processing loop, accumulator, Average, and formatted output. Codex created only the instruction scaffold and provided progressive review guidance
- New concept: Creating an empty List and adding one valid element to its end with `append()`
- Knowledge check: Passed after clarifying the precise meaning of an empty List and representing the post-append result as a complete List; final-order prediction `[5, 8, 12]` was correct
- Manual tests: 6 / 6 passed
- Student-designed test: Input sequence `1, 2, 3, -4, -5, 6, 0`; predicted and produced two invalid messages, stored order `1, 2, 3, 6, 0`, Total `RM12.00`, and Average `RM2.40`
- Append verification: Passed; one final valid price was appended for each SKU and all five elements were stored at the List end in collection order
- Invalid-data exclusion verification: Passed; negative attempts were rejected before append and never appeared in Stored Price output; zero was accepted
- Processing order verification: Passed across all tests; direct iteration reproduced append order exactly
- Accumulator verification: Passed after adding the initially omitted `total_price` initialization before direct iteration
- Average verification: Passed; Average used the finalized Total divided by five after processing
- Debugging check: Passed after tracing that append-before-validation stores the invalid `-5` and fails to append the later valid `10`
- Understanding check: Passed after clarifying that one append per SKU prevents missing or duplicate elements and yields exactly five valid prices
- Carry-forward weakness observation: Conceptual vocabulary precision appeared when `[]` was first described only as a List rather than an empty List. Validation structure was recalled, but the initial `<= 0` boundary incorrectly rejected valid zero and was self-corrected during the first code revision. Exact output labels were correct. Maximum/minimum direction did not arise
- Corrections understood: `[]` is an existing List with no elements; append adds one element to the end; initialize an accumulator before use; zero is valid under `>= 0`; append only once after validation; trace actual execution order rather than assuming control returns to an earlier statement
- Codex review: Passed empty-List creation, fixed five-record collection, repeated same-SKU validation, append placement, exact element count, invalid exclusion, order preservation, direct iteration, accumulator, post-loop Average, formatting, student ownership, prohibited-concept review, AGENTS.md compliance, and scope compliance
- Files changed: `exercises/module_02/lesson_03_purrnest_5_sku_price_collector.py`, `progress.md`, and `learning_log.md`
- Secrets/private-data check: No secrets or private data found
- Suggested Git commit: `Complete Module 2 Lesson 03 append fundamentals`
- Git commit/push status: Not yet committed or pushed
- Next confirmed task: Do not start Module 2 Lesson 04; wait for the Daily Learning Supervisor / Roadmap Manager
