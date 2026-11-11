# Challenge 13 — Remove Duplicates

**Difficulty:** Easy

**Language:** Python

## Description

Create a Python program that removes duplicate numbers from a list.

The program should return a new list containing only unique numbers while preserving their original order.

## Requirements

1. Create a list containing some duplicate integers.
2. Create a new empty list to store unique numbers.
3. Iterate through the original list.
4. Check whether each number already exists in the new list.
5. Add the number only if it has not appeared before.
6. Display the new list.

## Example

**Input:**

```python
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
```

**Expected Output:**

```text
Unique numbers: [1, 2, 3, 4, 5]
```

## Constraints

- Use a `for` loop.
- Use an `if` statement.
- Use a new list to store unique numbers.
- Do not use `set()`.
- Preserve the original order.
- Do not modify the original list.

## Concepts Practiced

- Lists
- For loops
- Conditional statements
- Membership operator (`in`)
- List methods (`append()`)
- Creating new lists
- Duplicate detection
