print('Lesson 8: Log and UnitTest')

import logging
import unittest

logging.basicConfig(level=logging.ERROR, filename='calculation.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Calculation:
    def __call__(self, a, b, operation):
        try:
            a, b = self.convert_to_number(a), self.convert_to_number(b)
            if operation == '+':
                return a + b
            elif operation == '-':
                return a - b
            elif operation == '*':
                return a * b
            elif operation == '/':
                if b == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                return a / b
            else:
                raise ValueError(f"Unsupported operation: {operation}")
        except Exception as e:
            logging.error(f"Calculation error: {e}")
            raise

    def convert_to_number(self, value):
        try:
            if isinstance(value, (int, float)):
                return value
            return float(value)
        except ValueError as e:
            logging.error(f"Conversion error for value {value}: {e}")
            raise

calc = Calculation()

class CalculationTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calc(2, 3, '+'), 5)

    def test_subtraction(self):
        self.assertEqual(calc(10, 4, '-'), 6)

    def test_multiplication(self):
        self.assertEqual(calc(3, 7, '*'), 21)

    def test_division(self):
        self.assertEqual(calc(8, 2, '/'), 4)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            calc(5, 0, '/')

    def test_invalid_operation(self):
        with self.assertRaises(ValueError):
            calc(5, 3, '%')

    def test_invalid_conversion(self):
        with self.assertRaises(ValueError):
            calc('abc', 5, '+')

unittest.main()
