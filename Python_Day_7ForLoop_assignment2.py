#2. Python program to check if a given number is an Armstrong number 

# Function to check if a given number is an Armstrong number
# An Armstrong number (also known as a narcissistic number) is equal to the sum of its own digits raised to the power of the number of digits.
def is_armstrong_number(num):  
    # Convert the number to a string to easily iterate through each digit
    digits = str(num)  
    # Calculate the number of digits
    num_digits = len(digits)  
    # Calculate the Armstrong sum
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)  
    # Check if the sum is equal to the original number
    return armstrong_sum == num  

# Example usage
input_number = 153  
# Check if the input number is an Armstrong number
is_armstrong_result = is_armstrong_number(input_number)  
# Print the result
print(is_armstrong_result)  # This should print True as 153 is an Armstrong number.