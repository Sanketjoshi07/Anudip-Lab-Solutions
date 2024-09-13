'''
1. Write a Python program to Get Only unique items from two sets. 

Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 

Output: {70, 40, 10, 50, 20, 60, 30} 

'''

# Define the sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Get unique items by combining the sets and removing common items
unique_items = set1.symmetric_difference(set2)

# Print the result
print(unique_items)

# Ans
#Output: {10, 20, 60, 70}
