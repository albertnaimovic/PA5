# def reverse(s):
#     return s[::-1]


# print(reverse("I am a string"))  # gnirts a ma I

# animals = ["cat", "dog", "hedgehog", "gecko"]
# iterator = map(reverse, animals)
# print(iterator)  # <map object at 0x7fd3558cbef0>

# for i in iterator:
#     print(i)

# print(list(iterator))  # ['tac', 'god', 'gohegdeh', 'okceg']


### part 2


# def greater_than_100(x):
#     return x > 100


# print(list(filter(lambda x: x > 100, [1, 111, 2, 222, 3, 333])))
# # [111, 222, 333]
####

# list(range(10))


# # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# def is_even(x):
#     return x % 2 == 0


# print(list(filter(is_even, range(10))))

# # [0, 2, 4, 6, 8]

# print(list(filter(lambda x: x % 2 == 0, range(10))))
# # [0, 2, 4, 6, 8]


####

# animals = ["cat", "Cat", "CAT", "dog", "Dog", "DOG", "emu", "Emu", "EMU"]


# def all_caps(s):
#     return s.isupper()


# print(list(filter(all_caps, animals)))
# # ['CAT', 'DOG', 'EMU']

# print(list(filter(lambda s: s.isupper(), animals)))
# # ['CAT', 'DOG', 'EMU']

###### REDUCE ######

from functools import reduce


def f(x, y):
    return x + y


from functools import reduce

print(reduce(f, [1, 2, 3, 4, 5]))
# 15
# tas pats bybis
print(sum([1, 2, 3, 4, 5]))
