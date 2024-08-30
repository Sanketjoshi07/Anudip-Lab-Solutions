#1.Python program to check if the given string is a palindrome 

# Function to check if a given string is a palindrome
# A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
def is_palindrome(s):  
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()  
    # Remove non-alphanumeric characters to ignore spaces, punctuation, and symbols
    s = ''.join(char for char in s if char.isalnum())  
    # Check if the string is equal to its reverse
    return s == s[::-1]  

# Example usage
input_string = 'A man, a plan, a canal, Panama'
# Check if the input string is a palindrome
is_palindrome_result = is_palindrome(input_string)  
# Print the result
print(is_palindrome_result)  # This should print True as it is a palindrome.