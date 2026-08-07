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
