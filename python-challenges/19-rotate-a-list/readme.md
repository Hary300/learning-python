# Challenge 19 — Rotate a List

## Description

Create a Python program that rotates a list one position to the right.

The last element should move to the first position, while all other elements move one position to the right.

## Requirements

1. Create a list containing numbers.
2. Create an empty list named `rotated_numbers`.
3. Add the last element of the original list to the beginning of the new list.
4. Iterate through the original list, starting from the first element and ending before the last element.
5. Append each element to `rotated_numbers`.
6. Display the rotated list.

## Example 1

**Input:**

```python
numbers = [1, 2, 3, 4, 5]
```

**Output:**

```text
Rotated list: [5, 1, 2, 3, 4]
```

## Example 2

**Input:**

```python
numbers = [10, 20, 30]
```

**Output:**

```text
Rotated list: [30, 10, 20]
```

## Constraints

- Use a `for` loop.
- Use `range()` and `len()`.
- Use indexing.
- Use `append()`.
- Do not use slicing.
- Do not use built-in rotation methods.

## Concepts Practiced

- Lists
- Indexing
- For loops
- `range()`
- `len()`
- `append()`
