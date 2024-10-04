#Q1.Write a Pandas program to create a dataframe from a dictionary and display it.
#Solution=>>

import pandas as pd  #Import the Pandas library for data manipulation

#Sample data dictionary where subjects are keys and student scores are values
#Contains scores for three subjects: Math, English, and Hindi
score = {'Math': [78, 85, 96, 80, 86],'English': [84, 94, 89, 83, 86],'Hindi': [86, 97, 96, 72, 83]}

#Creating a DataFrame from the dictionary
#A DataFrame is like a table with rows and columns
df = pd.DataFrame(score)

#Displaying the created DataFrame
#This will print the DataFrame in a tabular format
print("DataFrame created from the dictionary:")
print(df)


"""Output:

DataFrame created from the dictionary:
   Math  English  Hindi
0    78       84     86
1    85       94     97
2    96       89     96
3    80       83     72
4    86       86     83

"""
