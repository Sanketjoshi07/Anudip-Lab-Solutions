# Question 3: Write a Python program to reverse words in a string.
# Given string
string = "Deeptech Python Training"

# Split the string into words, reverse the list, and join them back into a string
reversed_string = " ".join(string.split()[::-1])

# Print the reversed string
print(reversed_string)

# Expected Output:
# Training Python Deeptech
