#Q2. Calculate the profit made by a company ,Input: revenue = np.array([10000, 12000, 11000, 10500]) ,expenses = np.array([4000, 5000, 4500, 4800])
#Solution=>>

import numpy as np

#Define the revenue array (represents revenue for different periods)
revenue = np.array([10000, 12000, 11000, 10500])

#Define the expenses array (represents expenses for the same periods)
expenses = np.array([4000, 5000, 4500, 4800])

#Calculate profit by subtracting expenses from revenue element-wise
#Profit is the difference between revenue and expenses for each period
profit = revenue - expenses

#Print the calculated profit
print("Profit made by a company is :", profit)

"""ANS=>>
 Profit made by a company is : [6000 7000 6500 5700]
 
"""
