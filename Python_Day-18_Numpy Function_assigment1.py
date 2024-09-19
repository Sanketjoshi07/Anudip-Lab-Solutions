'''
1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])
'''

import numpy as np

# Define the temperature readings for a city
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Find days with temperatures higher than 35 degrees Celsius (hot days)
hot_days = temperatures > 35

# Find days with temperatures lower than 5 degrees Celsius (cold days)
cold_days = temperatures < 5

# Combine hot and cold days to find extreme temperature days
extreme_days = hot_days | cold_days  # Logical OR operation to combine the two conditions

# Output the result
print("Temperature readings:", temperatures)
print("Days with extreme temperatures (True means extreme):", extreme_days)

# Output example:
# Temperature readings: [32.5 34.2 36.8 29.3 31.  38.7 23.1 18.5 22.8 37.2]
# Days with extreme temperatures (True means extreme): [False False  True False False  True False False False  True]
