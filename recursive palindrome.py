"""
Q5. Write a recursive function to check if a string is a palindrome.
A string is considered a palindrome if it reads the same forwards and backwards.
For example, "racecar" and "level" are palindromes.
"""


def function(x):
    if x.isnumeric():
        return None
    else:
        return str(x)[::-1] == x


text = input("Enter the Text: ")
function(text)
print(function(text))


