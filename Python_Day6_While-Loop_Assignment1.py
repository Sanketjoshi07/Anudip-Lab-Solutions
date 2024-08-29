#Q1.Write a python program to check whether a number is palindrome or not? 
#Solution=>>
#Define a function to check if a number is a palindrome
def is_palindrome(num):
    # Store the original number
    original_num = num
    # Initialize a variable to build the reversed number
    reversed_num = 0

    # Reverse the number using a while loop
    while num > 0:
        # Get the last digit of the number
        last_digit = num % 10
        # Append the last digit to the reversed number
        reversed_num = reversed_num * 10 + last_digit
        # Remove the last digit from the number
        num = num // 10

    # Check if the reversed number is the same as the original number
    return reversed_num == original_num

# Take input from user.
number = int(input("Enter a number: "))

# Determine if the number is a palindrome and print the result
if is_palindrome(number):
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")
"""ANS=>> Enter a number: 4237
          4237 is not a palindrome.
          Enter a number: 989
          989 is a palindrome.
 """

