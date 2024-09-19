'''
1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12])
'''

import numpy as np

# Dataset of daily temperature readings
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, -4, -12])

# Finding the indices of the hot days (temperature > 35)
hot_days = np.where(temperatures > 35)

# Finding the indices of the cold days (temperature < 5)
cold_days = np.where(temperatures < 5)

# Printing the temperatures and the respective days for hot and cold
print("Hot Days (Temperature > 35°C):")
for day in hot_days[0]:
    print(f"Day {day + 1}: {temperatures[day]}°C")  # +1 to convert 0-based index to human-readable day number

print("\nCold Days (Temperature < 5°C):")
for day in cold_days[0]:
    print(f"Day {day + 1}: {temperatures[day]}°C")  # +1 for human-readable day number


# Output example:
# Hot Days (Temperature > 35°C):
# Day 3: 36.8°C
# Day 6: 38.7°C
# Day 10: 37.2°C

# Cold Days (Temperature < 5°C):
# Day 11: -4.0°C
# Day 12: -12.0°C
