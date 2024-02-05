# 1.Write a Python program to triple all numbers of a given list of integers. Use Python map

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# iterator = map(lambda x: x * 3, my_list)

# print(list(iterator))

# 2.Write a Python program to square the elements of a list using map() function.

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# iterator = map(lambda x: pow(x, 2), my_list)

# print(list(iterator))

# 3.Write a Python program to add three given lists using Python map and lambda

# list_one = [1, 2, 3]
# list_two = [4, 5, 6]
# list_three = [7, 8, 9]


# iterator = map(lambda a, b, c,: a + b + c, list_one, list_two, list_three)

# print(list(iterator))

# 4.Write a Python program to add two given lists and find the difference between lists. Use map() function.


# 5.Write a Python program to convert a given list of integers and a tuple of integers in a list of strings.

# my_list = [1, 2, 3]
# my_tuple = (1, 2, 3)

# iterator = map(lambda x: str(x), my_list)

# print(list(iterator))

# iterator = map(lambda x: str(x), my_tuple)

# print(list(iterator))


# 6.Write a Python program to filter a list of integers using Lambda
# Original list of integers:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
# # Even numbers from the said list:
# # [2, 4, 6, 8, 10]

# print(list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
# # Odd numbers from the said list:
# # [1, 3, 5, 7, 9]


# 7.Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.
# Orginal list:
# [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

# print(list(filter(lambda x: x % 19 == 0 or x % 13 == 0, [19, 65, 57, 39, 152, 639, 121, 44, 90, 190])))

# Numbers of the above list divisible by nineteen or thirteen:
# [19, 65, 57, 39, 152, 190]


# 8.Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
# Original arrays:
# [1, 2, 3, 5, 7, 8, 9, 10]

# print(len(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 5, 7, 8, 9, 10]))))
# print(len(list(filter(lambda x: x % 2 != 0, [1, 2, 3, 5, 7, 8, 9, 10]))))
# Number of even numbers in the above array: 3
# Number of odd numbers in the above array: 5


# # Use reduce for following tasks
# from functools import reduce

# # 9.Write a python program that multiplies all the values in a given list of integers.

# print(reduce(lambda x, y: x * y, [1, 2, 5, 4, 3]))

# # 10.Write a python program that finds the maximum value within the given list.

# print(reduce(lambda x, y: x if x > y else y, [1, 2, 5, 4, 3]))

# # 11.Write a python function that given list of strings concatenates all of them together.

# print(reduce(lambda x, y: x + y, ["obuolys", "kriause", "citrina"]))
