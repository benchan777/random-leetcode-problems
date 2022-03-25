def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def factorial_v2(n):
    return 1 if n == 1 else n * factorial_v2(n - 1)

def factorial_tail(n, i = 1):
    return i if n == 1 else factorial_tail(n - 1, i * n)

print(factorial(4))
print(factorial_v2(4))
print(factorial_tail(4))