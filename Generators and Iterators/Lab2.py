#Write a Python program that uses a custom iterator to iterate over a list of integers.

class IntegerListIterator:
    # Initialize with a list of integers
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    # Make the object iterable
    def __iter__(self):
        return self

    # Define how to get the next element
    def __next__(self):
        if self.index < len(self.numbers):
            result = self.numbers[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# List of integers
numbers = [1, 2, 3, 4, 5]

# Custom iterator
iterator = IntegerListIterator(numbers)

# Iterate through the integers
for number in iterator:
    print(number)
