'''
Problem:
You are given a list of integers. Your task is to find the maximum difference between any two numbers in the list.

Write a Python function called max_difference(numbers) that takes a list of integers as input and returns the maximum difference between any two numbers in the list.
'''
def max_difference(numbers):
    sorted_numbers = sorted(numbers)
    difference = (sorted_numbers[-1]-sorted_numbers[0])
    return difference
numbers=[5, 2, 4 ,3, 6, 1]
result =(max_difference(numbers))
print(result)