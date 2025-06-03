# Create a simple banking system where a user can check their balance, deposit money, withdraw money, and exit the program.

# Features & Requirements
# The user starts with a balance of $100.

# Show a menu with options:

# Check balance
# Deposit money
# Withdraw money
# Exit
# Some help:
# Use a while loop to keep the program running until the user chooses to exit.

# Use if statements to handle menu choices.

# Use a for loop for a simple "loading" effect when processing deposits/withdrawals.

balance = 100

print("If you want to: ")
print("Check balance - insert '1'")
print("Deposit money - insert '2'")
print("Withdraw money - insert '3'")
print("Exit - insert '4'")

import time

while True:
  print()
  choice = int(input("Type in here what you want to do: "))
  if choice == 1:
    print("Your balance is: ", balance)
    if balance > 1000:
      print("DAMN! WHERE DID YOU GE ALL THAT MONEY")
    elif balance <= 0:
      print("Oh.. sorry mate")
    continue
  elif choice == 2:
    deposit = int(input("How much do you want to deposit? "))
    balance += deposit
    for i in ("....."):
      print(i, end = "")
      time.sleep(1)
    print()
    print("Your balance is now: ", balance)
    if balance > 1000:
      print()
      print("DAMN! WHERE DID YOU GE ALL THAT MONEY")
    elif balance <= 5:
      print()
      print("Oh.. sorry mate")
    continue
  elif choice == 3:
    withdrawal = int(input("How much do you want to withdraw? "))
    balance -= withdrawal
    if withdrawal > balance:
      print("You don't have that much :(")
    for i in ("....."):
      print(i, end = "")
      time.sleep(1)
    print()
    print("Your balance is now: ", balance)
    if balance > 1000:
      print()
      print("DAMN! WHERE DID YOU GE ALL THAT MONEY")
    elif balance <= 5:
      print()
      print("Oh.. sorry mate")
    continue
  elif choice == 4:
    print()
    print("You exited the bank.")
    break
  else:
    print()
    print("Do you want to rob the bank you stupid??? Please try again...")
    continue