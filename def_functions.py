# Task 1: Sum of Digits

# Write a Python function called sum_of_digits that takes an integer as input and returns the sum of its digits. For example, if the input is 123, the function should return 6 (since 1 + 2 + 3 = 6). Use this function to find the sum of digits for the following numbers:

# 12345
# 9876
# 54321


def sum_of_digits(number):
  digits = str(number)
  sum = 0
  for num in digits:
    sum = sum + int(num)
  return sum

#CHECK
print(sum_of_digits(12345))
print(sum_of_digits(9876))
print(sum_of_digits(54321))

# Task 2: Palindrome Checker

# Write a Python function called is_palindrome that takes a string as input and returns True if the string is a palindrome (reads the same forwards and backwards), and False otherwise. Use this function to check if the following strings are palindromes:

# "radar"
# "python"
# "level"

def is_palindrome(text):
  return text == text[::-1]

#CHECK
print(is_palindrome('radar'))
print(is_palindrome('python'))
print(is_palindrome('level'))

# Task 3: Multiplication Table

# Write a Python function called multiplication_table that takes an integer n as input and prints the multiplication table from 1 to 10 for that number. For example, if n is 5, the function should print the multiplication table for 5 up to 10x5. Use this function to print multiplication tables for the following numbers:

# 3
# 7
# 9

def multiplication_table(n):
    for m in range(1, 11):
      print(m * n)
    return

#CHECK
print(multiplication_table(5))