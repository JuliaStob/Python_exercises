# Exercise 2: For Loop
# Task: Write a Python program that calculates the sum of all multiples of 3 or 5 below a given number n.

# Example

# print(sum_multiples(10)) # Output: 23

n = int(input("What is your number? "))

sum = 0

for i in range(n):
  if i % 3 == 0 or i % 5 == 0:
    sum += i

print(sum)