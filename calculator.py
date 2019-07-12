class CalculatorError(Exception):
    """an exception class for calculator"""
import sys

class Calculator:
    def add(self, a, b):
        self._check_operand(a)
        self._check_operand(b)
        try:
            return a + b
        except TypeError:
            raise CalculatorError('hi dad')
        except ValueError:
            raise CalculatorError('hi mom')

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise CalculatorError("cant divide by zero")

if __name__ == "__main__":
    print("Lets calculate!")
    calculator = Calculator()
    operations = [
        calculator.add,
        calculator.subtract,
        calculator.multiply,
        calculator.divide,
    ]
    while True:
        for i, operation in enumerate(operations, start=1):
            print(f"{i}: {operation.__name__}")
        operation = input("Pick an operation: ")
        if operation == "q":
            sys.exit()
        op = int(operation)
        a = float(input("what is a ?"))
        b = float(input("what is b ?"))
        print(operations[op - 1](a,b))