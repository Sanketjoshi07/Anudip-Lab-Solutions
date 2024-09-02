# Question 1: Write a Python program to count the occurrences of each word in a given sentence.
# Given string
string = "To change the overall look of your document. To change the look available in the gallery"

# Convert the string to lowercase and split it into words
words = string.lower().split()

# Count the occurrences of each word
from collections import Counter
word_count = Counter(words)

# Print the word count
for word, count in word_count.items():
    print(f"{word}: {count}")

# Expected Output:
# to: 2
# change: 2
# the: 2
# overall: 1
# look: 2
# of: 1
# your: 1
# document.: 1
# available: 1
# in: 1
# gallery: 1
