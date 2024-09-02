# Question 2: Write a Python program to remove a newline in Python.
# Given string with newlines
string = "\nBest \nDeeptech \nPython \nTraining\n"

# Remove the newlines
cleaned_string = string.replace("\n", " ")

# Print the cleaned string
print(cleaned_string.strip())

# Expected Output:
# Best Deeptech Python Training
s