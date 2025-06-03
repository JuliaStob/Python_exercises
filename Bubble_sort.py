# Task 1: Bubble sort

# Write a function bubble_sort(list_of_numbers) that takes a list of numbers as input and sorts it using the Bubble Sort algorithm.

# Example:

# bubble_sort([64, 34, 25, 12, 22, 11, 90])
# Output: [11, 12, 22, 25, 34, 64, 90]

def bubble_sort(my_list):
  for n in range(len(my_list)-1):
    for i in range(len(my_list)-1):
      if my_list[i] > my_list[i+1]:
        my_list[i], my_list[i+1] = my_list[i+1], my_list[i]
  return my_list

#CHECK
print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))