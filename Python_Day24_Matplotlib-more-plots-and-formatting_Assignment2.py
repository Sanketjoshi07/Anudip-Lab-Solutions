#Q2.Suppose you're a sales manager for an e-commerce company, and you want to create a figure with subplots to compare the sales performance of different product categories over time.
#You have sales data for four product categories: Electronics, Clothing, Home & Garden, and Sports & Outdoors. Share your conclusion/analysis.
#Input: months = np.arange(1, 13) ,electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000]) ,clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000]) home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000]) sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])
#Solution=>>

import numpy as np  #Import NumPy for numerical operations
import matplotlib.pyplot as plt  #Import Matplotlib for creating plots

#nput data: Array of months from 1 to 12, representing the sales period (January to December)
months = np.arange(1, 13)

#Sales data for different product categories over the 12 months
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

#Create a 2x2 grid of subplots, with the overall figure size set to 10x8 inches
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

#Plot 1: Electronics Sales
#Electronics sales plot over the 12 months with diamond markers, blue color, and label, including title, X/Y-axis labels, and a legend
axs[0, 0].plot(months, electronics_sales, marker='D', color='blue', label='Electronics')
axs[0, 0].set_title('Electronics Sales')  
axs[0, 0].set_xlabel('Months')  
axs[0, 0].set_ylabel('Sales ($)')  
axs[0, 0].legend()
axs[0, 0].grid(True)

#Plot 2: Clothing Sales
#Clothing sales plot over the 12 months with diamond markers, green color, and label, including title, X/Y-axis labels, and a legend
axs[0, 1].plot(months, clothing_sales, marker='D', color='green', label='Clothing')
axs[0, 1].set_title('Clothing Sales')  
axs[0, 1].set_xlabel('Months')  
axs[0, 1].set_ylabel('Sales ($)')  
axs[0, 1].legend()
axs[0, 1].grid(True)

#Plot 3: Home & Garden Sales
#Home & Garden sales plot over the 12 months with diamond markers, red color, and label, including title, X/Y-axis labels, and a legend
axs[1, 0].plot(months, home_garden_sales, marker='D', color='red', label='Home & Garden')
axs[1, 0].set_title('Home & Garden Sales')  
axs[1, 0].set_xlabel('Months')  
axs[1, 0].set_ylabel('Sales ($)')  
axs[1, 0].legend()
axs[1, 0].grid(True)

#Plot 4: Sports & Outdoors Sales
#Sports & Outdoors sales plot over the 12 months with diamond markers, purple color, and label, including title, X/Y-axis labels, and a legend
axs[1, 1].plot(months, sports_outdoors_sales, marker='D', color='purple', label='Sports & Outdoors')
axs[1, 1].set_title('Sports & Outdoors Sales')  
axs[1, 1].set_xlabel('Months')  
axs[1, 1].set_ylabel('Sales ($)')  
axs[1, 1].legend()
axs[1, 1].grid(True)

#Adjust the layout to prevent overlap between subplots and ensure everything fits neatly
plt.tight_layout()

#Display the final figure with all subplots
plt.show()
