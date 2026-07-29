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
- [x] Module 1 – Lesson 07: Shopee Inventory Action Checker

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

- [x] Module 1 – Lesson 07: Combining business rules with `if` / `elif` / `else`

## Latest Session Evidence

- Date: 2026-07-29
- Day of week: Wednesday
- Session type: Core Python Learning Day
- Lesson or business feature completed: Module 1 – Lesson 07: Shopee Inventory Action Checker
- Final status: Passed
- Verified skills: Integer input conversion, ordered business rules, narrower-before-wider condition ordering, comparison operators, mutually exclusive classification, exact output labels, consistent indentation, and boundary reasoning
- Code personally written: Yes; the student personally wrote the inventory checker's core logic
- Errors encountered: The `stock_quantity <= 5` branch initially printed an incomplete classification label
- Corrections understood: The required label was corrected; the student explained that placing `<= 20` before `<= 5` would capture values such as 5 too early because only the first true branch executes
- Tests performed: `-1` → Invalid Stock; `0` → Restock Immediately; `3` → Low Stock - Reorder Soon; `10` → Stock Level Normal; `50` → Stock Sufficient; student-selected `9999` → Stock Sufficient; boundary reasoning confirmed for `5` and `20`
- Codex review result: Passed through code inspection, reported manual-test evidence, and the student's explanation of overlapping conditions and boundary behavior
- Files created or modified: `exercises/module_01/lesson_07_shopee_inventory_action_checker.py`, `progress.md`, and `learning_log.md`
- Next confirmed task: Wait for the Daily Learning Supervisor to generate the Daily Learning Report

## Next Concept

- [x] Comparison operators
- [x] `if`
- [x] `elif`
- [x] `else`

## Next Saturday Business Application

- [ ] Shopee Profit Decision Calculator v0.1

Planned skills:

- Numeric input
- Basic calculation
- Comparison operators
- `if` / `elif` / `else`

This feature has not been completed yet.

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

## Review Approach

- Use a short explanation and one assessment exercise for familiar topics.
- Move forward without unnecessary repetition after an assessment is passed.
- Connect core modules to realistic Shopee or TikTok uses when appropriate.
- Begin practical business tools before completing the entire Python curriculum.
- Do not import or move old Python files.
