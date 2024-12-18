#Write a Python program that filters out even numbers using the filter() function.

def even(n):
    return n%2==0

number = [1,2,3,4,5,6,7,8,9,10]

result = filter(even,number)
print(list(result))
