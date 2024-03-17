"""Q3. Write a recursive and Iterative function to find the sum of digits of a positive integer."""


def digits(n):
    """This function work on Iterative"""
    a = 0
    str_ = str(n)
    for i in str_:
        x = int(i)
        a += x
    f = a
    print(f)


num = int(input("Enter the number: "))
digits(num)


def sum_of_digits(n):
    """This is work on Recursion"""
    if n < 10:
        return n
    else:
        last_digit = n % 10
        remaining_digit = n // 10
        return last_digit + sum_of_digits(remaining_digit)


num = int(input("Enter the number: "))
sum_of_digits(num)
print(sum_of_digits(num))