#Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce

def multiply(x, y):
    return x * y

numbers = [2, 3, 5, 7, 11]


product = reduce(multiply, numbers)

print(f"The product of the list {numbers} is {product}.")
