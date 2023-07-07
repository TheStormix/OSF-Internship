'''
Challenge
Given a list of distinct integers between 1 and 100 with length 99, 
how do you find out the number not present in the array as efficiently as possible (array is not sorted)
'''
import random
def find_missing_number(numbers_list):
    result = 0
    for num in numbers_list:
        result ^= num
    for num in range(1, 101):
        result ^= num
    return result
numbers = list(range(1, 101))
numbers_list = random.sample(numbers, 99)
result = find_missing_number(numbers_list)
print(numbers_list)
print(result)
