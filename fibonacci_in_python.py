# Fn = F(n-1) + F(n-2)
def fibonacci_sequence(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

    else:
        return fibonacci_sequence(n - 1) + fibonacci_sequence(n - 2)


num = int(input("Enter the number for the Fibonacci sequence: "))
fibonacci_sequence(num)
print(fibonacci_sequence(num))
