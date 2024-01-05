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

my_list = [1, 2, 3]
my_tuple = (1, 2, 3)

iterator = map(lambda x: str(x), my_list)

print(list(iterator))

iterator = map(lambda x: str(x), my_tuple)

print(list(iterator))