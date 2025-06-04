# Exercise 1: If Statements (Conditional Statements)
# Task: Write a Python program that asks the user to enter a number and checks if the number is:

# Positive
# Negative
# Zero
# Even or Odd
# Example Input/Output:
# Enter a number: 7
# The number is positive and odd.

# Enter a number: -4
# The number is negative and even.

x = int(input("Enter your number: "))

if x > 0 and x % 2 == 0:
  print("Your number is positive and even.")
elif x < 0 and x % 2 == 0:
     print("Your number is negative and even.")
elif x < 0 and x % 2 != 0:
     print("Your number is negative and odd.")
elif x > 0 and x % 2 != 0:
     print("Your number is positive and odd.")
else:
      print("Your number is zero.")


