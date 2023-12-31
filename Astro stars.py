user_input = int(input("Enter a Integer: "))
for i in range(1, user_input+1):
    print(str(i).replace(str(i),"$")*i)