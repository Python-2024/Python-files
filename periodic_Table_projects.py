print("\tWelcome to our Periodic table searcher")
#main funtion
def periodic_table():
    # user input
    user_input = int(input("Enter the element's number (1-30, 0 to exit): "))
    #opening file
    f = open("periodic table list[elements]", "r")
    if user_input == 0: #conditional statements
        print("Try again :(\n")
        return periodic_table()
    elif user_input > 30:
        print("Try again :(\n")
        return periodic_table()
    else:
        lines = f.readlines()
        print(lines[user_input])
        f.close()
        return periodic_table()
periodic_table()