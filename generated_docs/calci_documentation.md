This document provides professional documentation for the given Python code, detailing its functionality, parameters, return values, and usage examples.

---

# Overview

This module provides fundamental arithmetic operations for basic numerical computations. It includes two core functions: `add` for summing two numbers and `subtract` for finding the difference between two numbers. Designed for simplicity, these functions handle both integer and floating-point numbers.

# Classes

No classes are defined within this module.

# Functions

## `add(a, b)`

Performs the addition of two numerical inputs.

## `subtract(a, b)`

Performs the subtraction operation, returning the difference between the first numerical input and the second.

# Parameters

### For `add(a, b)`:

*   **`a`** (`int` | `float`): The first operand for the addition.
*   **`b`** (`int` | `float`): The second operand for the addition.

### For `subtract(a, b)`:

*   **`a`** (`int` | `float`): The minuend; the number from which another is subtracted.
*   **`b`** (`int` | `float`): The subtrahend; the number to be subtracted from the minuend.

# Imports

This module does not require any external imports from the standard library or third-party packages.

# Returns

### For `add(a, b)`:

*   (`int` | `float`): The sum of `a` and `b`. The return type will match the input types (e.g., if both inputs are integers, an integer is returned; if any input is a float, a float is returned).

### For `subtract(a, b)`:

*   (`int` | `float`): The difference between `a` and `b` (`a - b`). The return type will match the input types.

# Example Usage

```python
# Define the functions (as they would be in your script)
def add(a, b):
    """Adds two numbers and returns their sum."""
    return a + b

def subtract(a, b):
    """Subtracts the second number from the first and returns the difference."""
    return a - b

# --- Example: Using add() ---
print("--- Demonstrating `add()` function ---")
# Example with integers
num1_add = 10
num2_add = 5
sum_result = add(num1_add, num2_add)
print(f"The sum of {num1_add} and {num2_add} is: {sum_result}") # Expected: 15

# Example with floats
float1_add = 3.5
float2_add = 2.1
float_sum_result = add(float1_add, float2_add)
print(f"The sum of {float1_add} and {float2_add} is: {float_sum_result}") # Expected: 5.6

# --- Example: Using subtract() ---
print("\n--- Demonstrating `subtract()` function ---")
# Example with positive difference
num1_sub = 100
num2_sub = 25
difference_result = subtract(num1_sub, num2_sub)
print(f"The difference between {num1_sub} and {num2_sub} is: {difference_result}") # Expected: 75

# Example with negative difference
neg_num1_sub = 5
neg_num2_sub = 10
neg_diff_result = subtract(neg_num1_sub, neg_num2_sub)
print(f"The difference between {neg_num1_sub} and {neg_num2_sub} is: {neg_diff_result}") # Expected: -5

# Example with floats
float1_sub = 10.0
float2_sub = 3.3
float_diff_result = subtract(float1_sub, float2_sub)
print(f"The difference between {float1_sub} and {float2_sub} is: {float_diff_result:.2f}") # Expected: 6.70 (approximately)
```