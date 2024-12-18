#Write a Python program to apply the map() function to
#square a list of numbers.

def square(n):
    return n*n

numbers = [1, 2, 3, 4, 5]

result = map(square,numbers)
print(list(result))