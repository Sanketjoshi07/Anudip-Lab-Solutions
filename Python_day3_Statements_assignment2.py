#2. Using input function take two number and then swap the number 

# Taking input from the user
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Swapping the numbers
a, b = b, a

# Printing the swapped values
print(f"After swapping, the first number (a) is: {a}")
print(f"After swapping, the second number (b) is: {b}")

"""Ans: Enter the first number (a): 24
Enter the second number (b): 12
After swapping, the first number (a) is: 12
After swapping, the second number (b) is: 24"""
