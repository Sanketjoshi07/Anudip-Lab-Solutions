""" Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

 Input: my_list = [1, 2, 3, 4, 5]"""

import numpy as np

# Input list
my_list = [1, 2, 3, 4, 5]

# Convert list to numpy array
array = np.array(my_list)

# Display the array
print("Array:", array)

# Display the first element
print("First element:", array[0])

# Display the last element
print("Last element:", array[-1])

# Multiply each element by 2
multiplied_array = array * 2

# Display the multiplied array
print("Multiplied array:", multiplied_array)


"""Output:
          Array: [1 2 3 4 5]
          First element: 1
          Last element: 5
          Multiplied array: [ 2  4  6  8 10]"""
