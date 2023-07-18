'''
Problem:
You are given a list of integers. Your task is to find the second largest number in the list.

Write a Python function called find_second_largest(numbers) that takes a list of integers as input and returns the second largest number in the list.
numbers = [5, 2, 7, 3, 9, 1]
result = find_second_largest(numbers)
print(result)  # Output: 7
'''
def find_second_largest(numbers):
    sorted_numbers = sorted(numbers,reverse=True)
    return sorted_numbers[1]

numbers=[5, 2, 7, 3, 9, 1]
result = find_second_largest(numbers)
print(result)