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
