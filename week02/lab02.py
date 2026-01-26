"""Week 02 lab utilities.

Contains simple implementations for functions used in Lab 02.
These are intentionally small and documented so students can test
them interactively (e.g., `python -i week02/lab02.py`).
"""

from typing import Any


def factorial(n: int) -> int:
	"""Return the factorial of a non-negative integer n.

	Parameters
	----------
	n : int
		Non-negative integer.

	Returns
	-------
	int
		Factorial of n. By definition factorial(0) == 1.

	Raises
	------
	TypeError
		If n is not an int.
	ValueError
		If n is negative.
	"""
	if not isinstance(n, int):
		raise TypeError("n must be an integer")
	if n < 0:
		raise ValueError("n must be a non-negative integer")

	result = 1
	for i in range(2, n + 1):
		result *= i
	return result


def is_prime(number: int) -> bool:
	"""Return True if number is prime, otherwise False.

	A simple, efficient algorithm for moderate-sized integers.

	Parameters
	----------
	number : int
		Integer to test.

	Returns
	-------
	bool
		True if prime.
	"""
	if not isinstance(number, int):
		raise TypeError("number must be an integer")
	if number <= 1:
		return False
	if number <= 3:
		return True
	if number % 2 == 0 or number % 3 == 0:
		return False

	import math

	limit = int(math.isqrt(number))
	i = 5
	while i <= limit:
		if number % i == 0 or number % (i + 2) == 0:
			return False
		i += 6
	return True


def reverse_string(s: str) -> str:
	"""Return the reversed string of s.

	Parameters
	----------
	s : str
		Input string.

	Returns
	-------
	str
		Reversed string.
	"""
	if not isinstance(s, str):
		raise TypeError("s must be a string")
	return s[::-1]

