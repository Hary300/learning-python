# Challenge 18 — Check if a List Is Sorted

## Description

Create a Python program that checks whether a list of numbers is sorted in ascending order.

A list is sorted in ascending order when each number is less than or equal to the number after it.

## Requirements

1. Create a list of numbers.
2. Create a boolean variable named `is_sorted` with an initial value of `True`.
3. Iterate through the list using indexes.
4. Compare each number with the next number.
5. If the current number is greater than the next number, set `is_sorted` to `False` and stop the loop.
6. Display whether the list is sorted.

## Example 1

**Input:**

```python
numbers = [1, 2, 3, 4, 5]
```

**Output:**

```text
The list is sorted.
```

## Example 2

**Input:**

```python
numbers = [1, 3, 2, 4, 5]
```

**Output:**

```text
The list is not sorted.
```

## Constraints

- Use a `for` loop with `range()`.
- Use `len()` to determine the list length.
- Use conditional statements.
- Use `break` when the list is not sorted.
- Do not use `sorted()` or `.sort()`.

## Concepts Practiced

- Lists
- Indexing
- `range()`
- `len()`
- Conditional statements
- Boolean variables
- `break`
