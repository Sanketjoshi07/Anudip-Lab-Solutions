#Install matplotlib  & you can use plt.plot() to create a line plot of given data

#Import Matplot Library
import matplotlib.pyplot as plt
#Input Values for X & Y axis
x = [0, 5, 9, 10, 15, 20, 25]
y = [0, 1, 2, 3, 4, 5, 6]
#Creat a line plot
plt.plot(x,y,marker='o')
#Give Title to the line plot
plt.title("Line Plot Chart")
#Label X & Y Axis
plt.xlabel("X AXIS")
plt.ylabel("Y AXIS")
#Display the Plot
plt.show()
