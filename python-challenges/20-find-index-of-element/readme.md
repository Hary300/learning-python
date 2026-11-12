# Challenge 20 — Find the Index of an Element

## Description

Create a Python program that finds the index of a target number in a list without using the built-in `index()` method.

If the target number does not exist, display a message indicating that it was not found.

## Requirements

1. Create a list of numbers.
2. Create a variable named `target` containing the number to search for.
3. Create a variable named `found_index` with an initial value of `-1`.
4. Iterate through the list using indexes.
5. Compare each element with the target.
6. If a match is found:
   - Store its index in `found_index`.
   - Stop the loop using `break`.
7. Display the result:
   - If `found_index` is not `-1`, display its index.
   - Otherwise, display that the element was not found.

## Example 1

**Input:**

```python
numbers = [10, 20, 30, 40, 50]
target = 30
```

**Output:**

```text
Element found at index: 2
```

## Example 2

**Input:**

```python
numbers = [10, 20, 30, 40, 50]
target = 99
```

**Output:**

```text
Element not found.
```

## Constraints

- Use a `for` loop with `range()`.
- Use `len()` and indexing.
- Use `break` when a match is found.
- Do not use `index()`.
- Do not use `in` to search for the target.

## Concepts Practiced

- Lists
- Indexing
- `range()`
- `len()`
- Conditional statements
- Boolean and integer variables
- `break`
