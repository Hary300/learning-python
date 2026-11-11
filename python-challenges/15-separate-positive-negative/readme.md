# Challenge 15 — Separate Positive and Negative Numbers

**Difficulty:** Easy

**Language:** Python

## Description

Create a Python program that separates positive and negative numbers from a given list into two different lists.

Zero should not be included in either list.

## Requirements

1. Create a list containing positive numbers, negative numbers, and zero.
2. Create two empty lists:
   - `positive_numbers`
   - `negative_numbers`
3. Iterate through the original list.
4. If a number is greater than zero, add it to `positive_numbers`.
5. If a number is less than zero, add it to `negative_numbers`.
6. Display both lists.

## Example

**Input:**

```python
numbers = [10, -5, 0, 8, -2, 3, -1]
```

**Expected Output:**

```text
Positive numbers: [10, 8, 3]
Negative numbers: [-5, -2, -1]
```

## Constraints

- Use a `for` loop.
- Use `if` and `elif`.
- Use the `append()` method.
- Do not use list comprehensions.
- Do not use built-in filtering functions.

## Concepts Practiced

- Lists
- Empty lists
- For loops
- Conditional statements
- append() method
- Comparison operators
