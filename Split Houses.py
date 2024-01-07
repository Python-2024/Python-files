input_case = input("Enter the case: ")

wrong_grid = "HH"
c = wrong_grid in input_case

if c == True:
    print("NO")
else:
    print("YES")
    print(input_case.replace(".", "B"))