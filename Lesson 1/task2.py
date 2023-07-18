'''
Problem:
You are given a list of integers. Your task is to find the sum of all the even numbers in the list.

Write a Python function called sum_even_numbers(numbers) that takes a list of integers as input and returns the sum of all the even numbers in the list.

'''

def sum_even_numbers(numbers):
    sum=0
    for element in numbers:
        if element % 2 ==0:
            sum+=element
    return sum        
numbers=[5, 2, 4 ,3, 6, 1]
result = sum_even_numbers(numbers)
print(result)