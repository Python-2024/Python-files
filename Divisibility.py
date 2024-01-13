test_cases = int(input("Enter the test cases: "))
user_number = 0
empty_list = []

for i in range(1, test_cases+1):
    user_number = int(input("Enter the number: "))
    empty_list.append(user_number)

for i in empty_list:
    end_digit = str(i)[-1]
    if int(end_digit) % 10 == 0:
        print(True)
    else:
        print(False)
