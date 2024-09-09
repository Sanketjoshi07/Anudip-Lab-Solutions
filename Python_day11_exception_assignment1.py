# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

# Function to handle division
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")

# Example usage
num1 = float(input("Enter the numerator: "))
num2 = float(input("Enter the denominator: "))

divide_numbers(num1, num2)

# ans
# Enter the numerator: 25
# Enter the denominator: 0
# Error: Division by zero is not allowed!

# Enter the numerator: 25
# Enter the denominator: 5
# The result of 25.0 divided by 5.0 is 5.0