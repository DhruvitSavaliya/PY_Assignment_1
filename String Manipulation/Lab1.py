#Write a Python program to demonstrate string slicing.

str1 = "hello world"

print("Substring from index 2 to 5:",str1[2:6])
 
print("Every alternate character: ",str1[::2])

print("String in reverse order: ",str1[::-1])

print("Characters from index 3 to the end: ",str1[3:])

print("Characters from the beginning to index 4:",str1[:5])

print("Characters from index 7 to 2 in reverse order: ",str1[7:1:-1])
