# 1. Write a Python program to Count all letters, digits, and special symbols from the given string

#  Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3 

# Function to count letters, digits, and special symbols
def count_chars_digits_symbols(input_string):
    # Initialize counters
    letter_count = 0
    digit_count = 0
    symbol_count = 0

    # Iterate over each character in the string
    for char in input_string:
        if char.isalpha():  # Check if the character is a letter
            letter_count += 1
        elif char.isdigit():  # Check if the character is a digit
            digit_count += 1
        else:  # If it's neither a letter nor a digit, it's a symbol
            symbol_count += 1

    # Return counts
    return letter_count, digit_count, symbol_count

# Input string
input_string = "P@#yn26at^&i5ve"

# Get counts
letters, digits, symbols = count_chars_digits_symbols(input_string)

# Print results
print(f"Chars = {letters}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")


#Output
# Chars = 8
# Digits = 2
# Symbols = 3

