#4. Python program to find the area of a triangle whose sides are given

a = 6
b = 8
c = 7
# Calculate the semi-perimeter
s = (a + b + c) / 2 # Calculate the semi-perimeter

# Calculate the area using Heron's formula
area = ((s * (s - a) * (s - b) * (s - c)) ** 0.5)

print("The area of the triangle is:", area)

#The area of the triangle is: 20.33316256758894