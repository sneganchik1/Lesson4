
# n! = n*f(n-1)
# 5!=5⋅4⋅3⋅2⋅1=120

def factorial(n):
    if n in (0, 1):
        return 1
    return n*factorial(n-1)
# print(factorial(50))




