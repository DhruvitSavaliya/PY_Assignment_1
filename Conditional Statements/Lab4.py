#Practical Example 8: Write a Python program to check if a person is eligible
#to donate blood using a nested if.

age = int(input("Enter your age: "))
weight = int(input("Enter your weight in kg: "))

if age >= 18:
    if weight >= 50:
        print( "You are eligible to donate blood.")
    else:
        print( "You are not eligible to donate blood because you do not weigh enough.")
else:
    print ( "You are not eligible to donate blood because you are too young.")

