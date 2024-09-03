# 2. Write a Python program to remove duplicate characters of a given string.

 #Input = “String and String Function” Output: String and Function


# Function to remove duplicate characters from the string
def remove_duplicates(input_string):
    seen = set()  # Set to keep track of seen characters
    result = []   # List to build the result string without duplicates

    # Split the input string into words
    words = input_string.split()

    # Iterate over each word
    for word in words:
        new_word = []  # Temporary list to build a word without duplicates

        # Iterate over each character in the word
        for char in word:
            if char not in seen:
                seen.add(char)   # Mark the character as seen
                new_word.append(char)  # Add character to the new_word list

        # Append the word with unique characters to the result
        result.append(''.join(new_word))

    # Join the list of words into a single string
    return ' '.join(result)

# Input string
input_string = "String and String Function"

# Get the result string without duplicates
output_string = remove_duplicates(input_string)

# Print the result
print(f"Output: {output_string}")

#Output: Strng and Functio

