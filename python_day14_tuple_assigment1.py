
#1.Write a python program and iterate the given tuples Input: employee1 = ("John Doe", 101, "Human Resources", 60000) employee2 = ("Alice Smith", 102, "Marketing", 55000) employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# Given employee tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# List of employees
employees = [employee1, employee2, employee3]

# Iterate through the employee tuples
for employee in employees:
    name, emp_id, department, salary = employee  # Unpack the tuple
    print(f"Name: {name}, ID: {emp_id}, Department: {department}, Salary: {salary}")

#Output:
#Name: John Doe, ID: 101, Department: Human Resources, Salary: 60000
#Name: Alice Smith, ID: 102, Department: Marketing, Salary: 55000
#Name: Bob Johnson, ID: 103, Department: Engineering, Salary: 75000
