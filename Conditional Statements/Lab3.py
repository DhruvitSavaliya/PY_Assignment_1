#Practical Example 7: Write a Python program to calculate grades based
#on percentage using if-else ladder.

m1 = int(input("Enter mark1 : "))
m2 = int(input("Enter mark2 : "))
m3 = int(input("Enter mark3 : "))
m4 = int(input("Enter mark4 : "))
m5 = int(input("Enter mark5 : "))

sum = m1+m2+m3+m4+m5
pre = sum/5

print("Your Percentage : ",pre)

if(pre>90):
    print("Grade - A")
elif(pre>80):
    print("Grade - B")
elif(pre>60):
    print("Grade - C")
elif(pre>30):
    print("Grade - D")
else:
    print("Fail")
