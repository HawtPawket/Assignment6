# Objective:
# The aim of this assignment is to build a basic calculator that can perform addition, subtraction, multiplication, and division.



# Task 1: Create functions for each arithmetic operation.
def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):   # Task 3: Ensure your program can handle division by zero and other potential errors.
    try:
        return num1 / num2
    except ZeroDivisionError:
        return "you can't divide by zero"

# Task 2: Implement user input to receive numbers and an operation choice.

num1 = float(input('Enter your first number: '))
operation = input('Enter an operation(+,-,/,*): ')
num2 = float(input('Enter your second number: '))

if operation =='+':
    result = num1 + num2
    print(result)
elif operation == '-':
    result = num1 - num2
    print(result)
elif operation == '*':
    result = num1 * num2
    print(result)
elif operation == '/':
    if num2 != 0:        # Task 3: Ensure your program can handle division by zero and other potential errors.
        result = num1 / num2
        print(result)
    else:
        print("You can't divide by zero!")