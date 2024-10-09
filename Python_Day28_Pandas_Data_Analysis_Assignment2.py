#Q2. Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school. Also generate a horizontal bar chart based on the result and explain the conclusion.
# Input: student_data = pd.DataFrame({ 'school_code': ['s001','s002','s003','s001','s002','s004'],
# 'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 
# 'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 
# 'age': [12, 12, 13, 13, 14, 12], 
# 'height': [173, 192, 186, 167, 151, 159], 
# 'weight': [35, 32, 33, 30, 31, 32], 
# 'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, )

# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame with the provided data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group the data by 'school_code' and calculate mean, min, and max age for each school
age_statistics = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Print the age statistics for each school
print("Age statistics for each school:\n", age_statistics)

# Plot the results as a horizontal bar chart
age_statistics.plot(kind='barh', figsize=(10, 6), color=['lightgreen', 'purple', 'yellow'])

# Add title and labels to the plot
plt.title("Age Statistics by School Code")
plt.xlabel("Age")
plt.ylabel("School Code")

# Display the plot
plt.show()


"""Output=>>
Age statistics for each school:
              mean  min  max
school_code
s001         12.5   12   13 
s002         13.0   12   14 
s003         13.0   13   13 
s004         12.0   12   12 """

"""Conclusion:

The horizontal bar chart displays the mean, minimum, and maximum ages for students in each school.

School s001 has a mean age of 12.5, with ages ranging from 12 to 13.
School s002 has a mean age of 13.0, with ages ranging from 12 to 14.
School s003 has a mean age of 13.0, with a consistent age of 13.
School s004 has a mean age of 12.0, consistent across all students.

"""
