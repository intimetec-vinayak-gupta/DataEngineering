# 1. Write a function that takes two functions and a value as arguments. 
# The function should apply the two functions to the value and return a tuple with the results.

def apply_functions(func1, func2, value):
    """Apply two functions to a value and return results as tuple"""
    result1 = func1(value)
    result2 = func2(value)
    return (result1, result2)

def square(x):
    return x * x

def double(x):
    return x * 2

result = apply_functions(square, double, 5)
print(f"square and double of given no are: {result}")  # (25, 10)


# 2. Implement a simple iterator that iterates over a list of numbers.

class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration
        value = self.numbers[self.index]
        self.index += 1
        return value

numbers = [1, 2, 3, 4, 5]
iterator = NumberIterator(numbers)
for num in iterator:
    print(f"Iterated: {num}")


# 3. Create a generator function that yields squares of numbers up to a given limit.

def squares_generator(limit):
    num = 1
    while num * num <= limit:
        yield num * num
        num += 1

for square in squares_generator(50):
    print(f"Square: {square}")


# 4. Create a closure function that generates a series of numbers starting from a given base.

def number_series_closure(base):
    def get_next():
        nonlocal base
        current = base
        base += 1
        return current
    return get_next

series_from_10 = number_series_closure(10)
for i in range(5):
    print(f"Next in series: {series_from_10()}")
