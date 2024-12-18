#Practical Example 3: Write a Python program to find a specific string in
#the list using a simple for loop and if condition.

list1 = ["apple", "banana", "cherry",'mango']

ch = input("Enter search string : ")

for i in list1:
    if i==ch:
        print(ch," String Found")
        break
else:
    print(ch," String Not Found")
