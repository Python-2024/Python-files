"""
Q78. Write a recursive function to calculate the exponentiation of a number
base raised to an integer exponent.
"""

def function(x, y):
    """
    :param x: Base
    :param y: Exponent
    """
    if y == 0:
        return 1
    else:
        return x ** y

num1 = int(input("Enter the base: "))
num2 = int(input("Enter the exponent: "))
function(num1, num2)
print(function(num1, num2))