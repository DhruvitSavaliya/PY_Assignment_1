#Write a Python program that manipulates and prints
#strings using various string methods. 

str1 = " Hello, Python World! "

print("Original String: \n",str1)

print()
stripped_string = str1.strip()
print("Stripped String: ",stripped_string)

print()
upper_string = str1.upper()
print(f"Uppercase: ",upper_string)

print()
lower_string = str1.lower()
print(f"Lowercase: ",lower_string)

print()
replaced_string = str1.replace("Python", "Programming")
print(f"Replaced String: ",replaced_string)

print()
split_list = str1.split()
print(f"Split into List: ",split_list)

print()
joined_string = "-".join(split_list)
print(f"Joined with Hyphen: ",joined_string)

print()
starts_with_hello = str1.startswith("Hello")
print(f"Starts with 'Hello': ",starts_with_hello)

print()
ends_with_world = str1.endswith("World!")
print(f"Ends with 'World!': ",ends_with_world)

print()
position_of_python = str1.find("Python")
print(f"Position of 'Python': ",position_of_python)

print()
count_of_o = str1.count("o")
print(f"Count of 'o': ",count_of_o)

print()
reversed_string = stripped_string[::-1]
print(f"Reversed String: '",reversed_string)
