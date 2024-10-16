"""
Exercise 1: Divide
"""
def divide(a, b):
  """Divides two numbers, handling potential division by zero.

  Args:
    a: The numerator.
    b: The denominator.

  Returns:
    The quotient, or None if b is zero.
  """

  if b == 0:
    return None
  else:
    return a / b

#check if divide 12&6 correctly
assert divide(12, 6) == 2
#check if divide 20&4 correctly
assert divide(20, 4) == 5
#check if return None when given 0
assert divide(8, 0) == None

"""
Exercise 2: Factorial
"""
def factorial(n):
  """Calculates the factorial of a non-negative integer.

  Args:
    n: A non-negative integer.

  Returns:
    The factorial of n.
  """

  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
  
#check if input 0 returns 1
assert factorial(0) == 1
#check if input 3 output correctly
assert factorial(3) == 6

"""
Exercise 3: String Reverse
"""
def reverse_string(string):
  """Reverses a given string.

  Args:
    string: A string to be reversed.

  Returns:
    The reversed string.
  """

  reversed_string = ""
  for char in string:
    reversed_string = char + reversed_string
  return reversed_string

#check if function reverse hi
assert reverse_string("hi") == "ih"
#check if function reverse "Hello World"
assert reverse_string("Hello World") == "dlroW olleH"

"""
Exercise 4: Fibonacci
"""
def fibonacci(n):
  """Generates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate.

  Returns:
    The nth Fibonacci number.
  """

  if n <= 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

#check if input 9 output 34
assert fibonacci(9) == 34
#check if input 3 output 2
assert fibonacci(3) == 2

"""
Exercise 5: Email Validation
"""

import re

def is_valid_email(email):
  """Determines whether email is valid or not

  Args:
    email: The email to validate

  Returns:
    Boolean value if email is valid
  """
  email_regex = r"^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,4})+"
  return re.match(email_regex, email) is not None

#check if output true when email vaild
assert is_valid_email("bwang@brooklynsteamcenter.org") == True
#check if output false when email invaild
assert is_valid_email("hi") == False