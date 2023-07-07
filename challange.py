'''
Challenge
Given a list of distinct integers between 1 and 100 with length 99, 
how do you find out the number not present in the array as efficiently as possible (array is not sorted)
'''
import random

def find_missing_number(numbers):
    result = 0
    for num in numbers:
        result ^= num
    for num in range(1, 101):
        result ^= num
    return result

exclude_number = random.randint(1, 100)
numbers =[x for x in range(1, 101) if x != exclude_number]
result = find_missing_number(numbers)
print(numbers)
print(result)
