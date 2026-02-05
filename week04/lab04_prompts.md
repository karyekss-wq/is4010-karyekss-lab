# Lab 04 AI Prompts and Responses

## Problem 1: Finding common items

**Prompt**
I have two very large lists of product IDs from two suppliers. I need to find which IDs appear in both lists. The output order does not matter. Which Python data structure or approach should I use and why?

**AI recommendation and reasoning**
Use sets and set intersection. Converting lists to sets removes duplicates and enables fast membership checks; intersecting the sets gives the common IDs efficiently. Since order doesn’t matter, returning a list built from the intersection is fine.

## Problem 2: User profile lookup

**Prompt**
I have a list of user profiles, each with unique `name`, plus `age` and `email`. I need to look up users by name frequently and quickly. What data structure should I use and why?

**AI recommendation and reasoning**
Use a dictionary keyed by username. Building a dict like `{user['name']: user}` enables average O(1) lookup by name. This is faster than scanning the list each time and returns the full profile when found.

## Problem 3: Listing even numbers in order

**Prompt**
I have a list of integers from sensor readings. I need to return only the even numbers while preserving the original order. What Python data structure or technique is best?

**AI recommendation and reasoning**
Use a list (or list comprehension) to filter the numbers. A list preserves order, and a comprehension like `[n for n in numbers if n % 2 == 0]` keeps only evens while maintaining the original sequence.
