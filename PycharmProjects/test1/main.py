#1.Person who have above 18 in the given list
people = [
    {"name": "john", "age": 30},
    {"name": "Aishu", "age": 16},
    {"name": "meera", "age": 28},
    {"name": "Meena", "age": 14}
]
# Filter people who are 18 or older
adults = filter(lambda person: person["age"] >= 18, people)
# Map the remaining people's names to a list
adult_names = list(map(lambda person: person["name"], adults))
print(adult_names)

#2.product of numbers in the list
from functools import reduce
numbers = [11,22,33,44]
# Calculate product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)

#3.square of even numbers in the list
numbers = [1, 2, 3, 4, 5, 6]
squares_of_evens = [
    (lambda x: x * x)(n)
    for n in numbers
    if (lambda x: x % 2 == 0)(n)
]
print(squares_of_evens)

#4.Check if given string is number
is_number = lambda s: s.replace('.', '', 1).isdigit()
print(is_number("12.5"))
print(is_number("3.14"))
print(is_number("12.5.3"))

#5.to extract the day, year, month from a datetime object
from datetime import datetime
dates = [
    datetime(2023, 1, 10),
    datetime(2024, 6, 25),
    datetime(2025, 12, 5)
]
result = list(map(lambda d: (d.year, d.month, d.day), dates))
print(result)

#6.fibonacci series up to n terms
from functools import reduce
fibonacci = lambda n: reduce(
    lambda seq, _: seq + [seq[-1] + seq[-2]],
    range(n - 2),
    [0, 1]
)[:n]

print(fibonacci(10))