import math

user_input = int(input("Enter the number: "))

sqrt1 = math.sqrt(user_input)
spliting = str(sqrt1).split(".")
print(int(spliting[0]))
