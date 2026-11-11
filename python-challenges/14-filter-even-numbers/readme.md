# Challenge 14 — Filter Even Numbers

## Description

Create a program that filters even numbers from a list and stores them in a new list.

## Requirements

1. Use a `for` loop to iterate through the list.
2. Use an `if` statement to check whether a number is even.
3. Use `append()` to add even numbers to a new list.
4. Do not use list comprehension or `filter()`.

## Example

**Input:**

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
```

**Expected Output:**

```text
Even numbers: [2, 4, 6, 8]
```

## Additional Test Cases

- `[1, 3, 5, 7]` → `[]`
- `[2, 4, 6, 8]` → `[2, 4, 6, 8]`
- `[-3, -2, -1, 0, 1, 2]` → `[-2, 0, 2]`

## Concepts Practiced

- `for` loop
- `if` statement
- Modulo operator (`%`)
- Lists
- `append()`
