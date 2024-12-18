#Write a generator function that generates the first 10 even numbers.

even_numbers = (i * 2 for i in range(1, 11))

for number in even_numbers:
    print(number)
