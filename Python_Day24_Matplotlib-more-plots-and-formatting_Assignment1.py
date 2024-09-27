#Q1. Create a pie chart to visualize the distribution of your monthly income by source. You have collected data on the various sources of your income, such as salary, freelance work, investments, and rental income. Share your conclusion/analysis.
#Input: income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other'] ,monthly_income = [5000, 1500, 1000, 600, 400]
#Solution=>>

import matplotlib.pyplot as plt  #Import the matplotlib library for plotting

#Input data: List of income sources and corresponding monthly income values
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]

#Create a figure for the pie chart with a specified size (7x7 inches)
plt.figure(figsize=(7, 7))

#Create a pie chart displaying the percentage distribution of monthly_income for each income_sources, with slices rotated by 140 degrees and custom colors.
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=140, 
         colors= ['lightblue', 'lightcoral', 'lightgreen', 'lightpink', 'lightgrey'])  

#Add a title to the pie chart
plt.title('Distribution of Monthly Income by Source')

#Display the chart
plt.show()
