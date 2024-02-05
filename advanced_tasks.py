# Task nr.1:
# Write a Python function that takes a list of integers as input,
# and returns a new list containing only the prime numbers in the original list, squared.


# def square_primes(my_list: list) -> list:
#     return list(map(lambda x: pow(x,2),filter(lambda x: all(x % y for y in range(2, x // 2)), my_list)))

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(square_primes(my_list))


# Task nr.2
# Create a function called `filter_and_map_books` that takes a list of such dictionaries as input and performs the following operations:
#  - Select books that were published after the year 2000.
#  - Transform the selected books into a new list containing tuples with the format `(Title, Author)`.
#  - The function should return the list of tuples with the titles and authors of the books published after the year 2000.

# Example:
# {
#     'title': 'Book Title',
#     'author': 'Author Name',
#     'published_year': 20XX,
#     'rating': X.X
# }
# P.S minimum 5 different titles


def filter_and_map_books(list_of_books: list) -> list:
    return list(map(lambda x: (x["title"], x["author"]),list(filter(lambda x: x["published_year"] > 2000, list_of_books))))



list_of_books = [
    {
        "title": "Harry Potter",
        "author": "J.K. Rowling",
        "published_year": 1997,
        "rating": 11,
    },
    {
        "title": "Don Quixote",
        "author": "Miguel de Cervantes",
        "published_year": 2015,
        "rating": 14,
    },
    {
        "title": "A Tale of Two Cities",
        "author": "Charles Dickens",
        "published_year": 1859,
        "rating": 7,
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "published_year": 2001,
        "rating": 10,
    },
    {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "published_year": 2020,
        "rating": 12,
    },
]
print(filter_and_map_books(list_of_books))
