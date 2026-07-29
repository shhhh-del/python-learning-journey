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

## Latest Session Evidence

- Date: 2026-07-30
- Day of week: Thursday
- Session type: Core Python Learning Day
- Lesson or business feature completed: Module 1 — Lesson 08: Business Rule Priority Review — Shopee Order Acceptance Checker
- Final status: Passed
- Verified skills: Business-rule priority, specific-before-general condition ordering, overlapping-condition reasoning, first-true-branch execution, integer input conversion, mutually exclusive output, indentation, readability, and boundary-value testing
- Code personally written: Yes; the student personally wrote the order acceptance checker's core logic
- Errors encountered: Knowledge-check Question 2 was initially omitted, and Question 5 initially predicted the later zero branch instead of the earlier matching branch
- Corrections understood: The student corrected both predictions and explained that zero satisfies `<= 3`, so placing that broader condition before `== 0` would capture zero and prevent the specific zero result
- Tests performed: `-1` → Invalid Stock Data; `0` → Reject Order; `1` → Accept Order - Low Stock Warning; `3` → Accept Order - Low Stock Warning; `4` → Accept Order; student-selected `-3` → Invalid Stock Data
- Codex review result: Passed through code inspection, six reported manual tests, boundary verification, and the student's explanation of overlapping conditions and execution order
- Files created or modified: `exercises/module_01/lesson_08_shopee_order_acceptance_checker.py`, `progress.md`, and `learning_log.md`
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
