#Practical Example 6: Write a Python program to check if a number is
#prime using if_else.

n = int(input("Enter Any Number: "))

if n > 1:
    for i in range(2,n):
        if n%i == 0:
            print(n, "Is Not Prime Number")
            break
    else:
            print(n, "Is prime Number")
