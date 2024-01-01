import string

# index of lower case alphabet
indexing = [['a', 0], ['b', 1], ['c', 2], ['d', 3], ['e', 4], ['f', 5], ['g', 6], ['h', 7], ['i', 8], ['j', 9],
             ['k', 10], ['l', 11], ['m', 12], ['n', 13], ['o', 14], ['p', 15], ['q', 16], ['r', 17], ['s', 18],
             ['t', 19], ['u', 20], ['v', 21], ['w', 22], ['x', 23], ['y', 24], ['z', 25]]
# user inputs
user_input1 = input("The numerical value of firstWord is ")
spliting_up1 = user_input1.split(' ')
user_input2 = input("The numerical value of secondWord is ")
spliting_up2 = user_input2.split(' ')
targeted = input("The numerical value of targetWord is ")
target3 = targeted.split(' ')
# all lower case alphabets
lower_case = string.ascii_lowercase
# main function
def is_sum_is_equal():
    # part-1
    sum1 = 0
    for words in spliting_up1:
        for chars in words:
            for index in indexing:
                if chars == index[0]:
                    sum1 += index[1]
    # part-2
    sum2 = 0
    for words2 in spliting_up2:
        for chars2 in words2:
            for index2 in indexing:
                if chars2 == index2[0]:
                    sum2 += index2[1]
    # part-3
    sum3 = 0
    for words3 in target3:
        for chars3 in words3:
            for index3 in indexing:
                if chars3 == index3[0]:
                    sum3 += index3[1]
    # condition
    if sum1 + sum2 == sum3:
        print(True)
    else:
        print(False)
# calling the function
is_sum_is_equal()