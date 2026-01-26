# Lab 02: Prompt Engineering Solutions

This file contains the prompts I used (CPTF framework) and the final code produced by the AI for each problem in Part 2 of the lab.

---

### Problem 1: Debugging

**Context:**
The following function is intended to calculate the sum of all even numbers in a list, but it currently returns the sum of odd numbers instead.

```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Parameters
    ----------
    numbers : list of int
        A list of integers.

    Returns
    -------
    int
        The sum of all even numbers in the list.
    """
    total = 0
    for num in numbers:
        if num % 2 == 1:  # This line has a bug!
            total += num
    return total
```

**Persona:**
You are a senior Python developer. Be concise and precise.

**Task:**
Identify the bug, explain why it happens, and provide a corrected, robust implementation. Also include a short test example showing expected output.

**Format:**
Return (1) a one-paragraph explanation, (2) corrected code in a Python code block, and (3) a short usage example.

**Exact prompt used:**
```text
Context: I have a function that should compute the sum of all even numbers in a list of integers. The function is shown above and currently returns the wrong result.
Persona: You are a senior Python developer.
Task: Explain the bug in one paragraph, give a corrected implementation that handles non-integer items gracefully (skip them), and provide a short usage example. Also mention edge cases to consider.
Format: Provide a short explanation, a Python code block with the corrected function, and a short usage example in code.
```

**AI's Corrected Code:**
```python
def sum_of_evens(numbers):
    """Calculate the sum of all even numbers in a list.

    Non-integer elements are ignored. Returns 0 for empty input.
    """
    total = 0
    for num in numbers:
        # Skip values that are not integers
        if not isinstance(num, int):
            continue
        if num % 2 == 0:
            total += num
    return total

# Short usage examples
print(sum_of_evens([1, 2, 3, 4, 5]))  # 6
print(sum_of_evens([2, 4, 6]))        # 12
print(sum_of_evens([]))               # 0
```

**What I learned:**
- The original bug was a wrong parity test (`% 2 == 1`) which selects odd numbers. The fix uses `% 2 == 0`.
- Adding a type check makes the function more robust when lists contain non-integers.

---

### Problem 2: Refactoring an unreadable function

**Context:**
This function returns the names of users who are 18 or older, but it's written in an unidiomatic way (indexing by range and repeated dictionary access).

```python
def get_names_of_adults(users):
    """Given a list of user dictionaries, returns a list of names of users
    who are 18 or older.

    Parameters
    ----------
    users : list of dict
        List of user dictionaries with 'name' and 'age' keys.

    Returns
    -------
    list of str
        Names of users who are 18 or older.
    """
    results = []
    for i in range(len(users)):
        if users[i]['age'] >= 18:
            results.append(users[i]['name'])
    return results
```

**Persona:**
You are a senior Python developer who focuses on readability and Pythonic idioms.

**Task:**
Refactor the function to be more Pythonic, handle missing keys gracefully, and include a brief explanation of the changes.

**Format:**
Provide the refactored function in a Python code block and a short paragraph describing improvements.

**Exact prompt used:**
```text
Context: The function above works but is non-idiomatic and brittle if some user dicts are missing keys.
Persona: You are a senior Python developer who values readability and robust code.
Task: Refactor the function to be Pythonic (prefer list comprehensions), handle missing 'age' or 'name' keys gracefully (skip the entry), and include a one-paragraph explanation of the changes and benefits.
Format: Provide the refactored function in a code block and a short explanation paragraph.
```

**AI's Refactored Code:**
```python
def get_names_of_adults(users):
    """Return a list of names for users aged 18 or older.

    Missing or malformed entries are ignored.
    """
    names = [
        user['name']
        for user in users
        if isinstance(user, dict) and user.get('age', 0) >= 18 and 'name' in user
    ]
    return names

# Example
users = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 17},
    {'age': 25},  # missing name
]
print(get_names_of_adults(users))  # ['Alice']
```

**What I learned:**
- List comprehensions make the function concise and expressive.
- Using `user.get('age', 0)` and checking `'name' in user` avoids KeyError and makes code robust against malformed input.

---

### Problem 3: Documenting a function

**Context:**
This function computes the area of a rectangle but has no docstring or documentation.

```python
def calculate_area(length, width):
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**Persona:**
You are a technical writer and senior Python developer who follows NumPy-style docstring conventions.

**Task:**
Write a professional NumPy-style docstring for the function that describes parameters, return value, and the raised error.

**Format:**
Provide the updated function with the docstring in a Python code block and a one-sentence rationale for the chosen wording.

**Exact prompt used:**
```text
Context: The function calculate_area(length, width) computes the rectangle area but lacks documentation.
Persona: You are a technical writer and senior Python developer.
Task: Produce a NumPy-style docstring that documents parameters, return type, and the ValueError raised for non-positive inputs. Keep it concise and clear.
Format: Provide the updated function in a Python code block and a one-sentence rationale.
```

**AI's Documented Code:**
```python
def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Parameters
    ----------
    length : float
        The length of the rectangle. Must be a positive number.
    width : float
        The width of the rectangle. Must be a positive number.

    Returns
    -------
    float
        The computed area (length * width).

    Raises
    ------
    ValueError
        If `length` or `width` is not a positive number.

    Examples
    --------
    >>> calculate_area(3, 4)
    12
    """
    if length <= 0 or width <= 0:
        raise ValueError("Length and width must be positive numbers.")
    return length * width
```

**Rationale:**
The docstring follows NumPy style, documents types, describes the error condition, and includes a short example to show expected usage.

---

## Final notes
- I created robust, idiomatic solutions for each problem and included small examples you can run interactively.
- If you want, I can run unit tests for these functions and add `week02/tests/test_prompts.py` with a few pytest cases and push them.
