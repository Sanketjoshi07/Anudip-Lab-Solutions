#Q2. Write a Pandas program to create and display a DataFrame from a specified dictionary data which has the index labels. 
#Solution=>>

import pandas as pd  #Import Pandas library for data manipulation
import numpy as np   #Import NumPy library to handle missing values (NaN)

#Sample dictionary data where each key represents a column (name, score, attempts, qualify)
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],  #Scores with some missing values (NaN)
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],  #Number of attempts by each student
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}  #Qualification status

#Defining custom index labels
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']  #Custom labels for rows

#Creating a DataFrame from the dictionary and applying custom index labels
df = pd.DataFrame(exam_data, index=labels)

#Displaying the created DataFrame
print("DataFrame created from the dictionary:")
print(df)

"""Output=>

 DataFrame created from the dictionary:
        name  score  attempts qualify
a  Anastasia   12.5         1     yes
b       Dima    9.0         3      no
c  Katherine   16.5         2     yes
d      James    NaN         3      no
e      Emily    9.0         2      no
f    Michael   20.0         3     yes
g    Matthew   14.5         1     yes
h      Laura    NaN         1      no
i      Kevin    8.0         2      no
j      Jonas   19.0         1     yes

"""
