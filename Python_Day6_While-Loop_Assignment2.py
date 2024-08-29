#Q2.Write a python program finding the factorial of a given number using a while loop
#Solution=>>
# Define a function to calculate the factorial of a given number
def factorial(n):
    # Check if the input number is negative
    if n < 0:
        # Print a message indicating factorial is not defined for negative numbers
        print("Factorial is not defined for negative numbers.")
    else:
        # Initialize result to 1; factorial of 0 and 1 is 1
        result = 1
        
        # Calculate factorial using a while loop inside the else block
        while n > 0:
            # Multiply the current result by the current number
            result *= n
            # Decrement the number by 1 for the next iteration
            n -= 1
        
        # Print the final computed factorial
        print(f"The factorial of  {number} is {result}.")

# Prompt the user to enter a number
number = int(input("Enter a number: "))

# Calculate the factorial of the entered number
factorial(number)

"""ANS=>> Enter a number: -9
          Factorial is not defined for negative numbers.
          Enter a number: 7
          The factorial of  7 is 5040.
          """
