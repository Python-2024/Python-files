"""Iterative function"""
def factorial():
    n = 5
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac
factorial()
print(factorial())

"""Recursion Funtion"""
def factorial_recursive(n):
    if n ==1:
        return 1
    else:
        return n * factorial_recursive(n-1)
n = 5
print(factorial_recursive(n))