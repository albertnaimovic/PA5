def reverse(s):
    return s[::-1]


print(reverse("I am a string"))  # gnirts a ma I

animals = ["cat", "dog", "hedgehog", "gecko"]
iterator = map(reverse, animals)
print(iterator)  # <map object at 0x7fd3558cbef0>

for i in iterator:
    print(i)

print(list(iterator))  # ['tac', 'god', 'gohegdeh', 'okceg']
