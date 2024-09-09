# Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_integer_input():
    try:
        user_input = input("Please enter an integer: ")
        number = int(user_input)  # Try to convert the input to an integer
        print(f"You entered the integer: {number}")
    except ValueError:
        print(f"Error: '{user_input}' is not a valid integer!")

# Example usage
get_integer_input()

# ans
# Please enter an integer: 1.0
# Error: '1.0' is not a valid integer!

# Please enter an integer: 25
# You entered the integer: 25
