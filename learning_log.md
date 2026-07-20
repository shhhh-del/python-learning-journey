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
