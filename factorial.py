def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)

def printDigits(n):
    print(n * str(n))
    if n > 1:
        printDigits(n - 1)