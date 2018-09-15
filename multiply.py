def multiply(n):
    if n==1:
        return 1
    else:
        return 4*multiply(n-1)
