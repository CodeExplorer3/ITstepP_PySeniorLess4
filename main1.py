print('Lesson 7: Iterators, Closure function')

class Counter:
    limit: int
    index: int
    step_iteration: int

    def __init__(self, limit: int, step_iteration: int):
        self.index = 0
        self.limit = limit
        self.step_iteration = step_iteration

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        self.index += self.step_iteration
        if self.index > self.limit:
            raise StopIteration
        return self.index


numbers = ['one', 'two', 3, 4, 'five', 'c++', 'c#']
counter = Counter(len(numbers), 2)

try:
    for i in counter:
        print(numbers[i])
except Exception as e:
    print('catch next error: ', e.__str__())


def arithmetic_operations():
    def check_type(value):
        try:
            if isinstance(value, (int, float)):
                return value
            return float(value)
        except ValueError:
            raise ValueError(f"Cannot convert {value} to a number")

    def safe_division(a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return a / b

    def calculate(a, b):
        a, b = check_type(a), check_type(b)
        addition = a + b
        subtraction = a - b
        multiplication = a * b
        division = safe_division(a, b)
        return addition, subtraction, multiplication, division

    return calculate


operations = arithmetic_operations()
try:
    result = operations(10, 2)
    print(f"Addition: {result[0]}, Subtraction: {result[1]}, Multiplication: {result[2]}, Division: {result[3]}")
except Exception as e:
    print('Error: ', e)
