# Challenge 17 — Find Common Elements

## Description

Create a Python program that finds elements that exist in both lists.

## Requirements

1. Create two lists containing numbers.
2. Create an empty list named `common_elements`.
3. Iterate through the first list.
4. Check whether each element also exists in the second list.
5. If it exists and has not already been added, append it to `common_elements`.
6. Display the common elements.

## Example

**Input:**

```python
list_a = [1, 2, 3, 4, 5, 2]
list_b = [3, 4, 5, 6, 7, 4]
```

**Output:**

```text
Common elements: [3, 4, 5]
```

## Constraints

- Use a `for` loop.
- Use conditional statements.
- Use the `in` operator.
- Use `append()`.
- Do not use `set()`.
- Do not use list comprehensions.
- Do not use built-in intersection methods.

## Concepts Practiced

- Lists
- For loops
- Conditional statements
- Membership operators (`in`)
- Duplicate checking
- `append()`
