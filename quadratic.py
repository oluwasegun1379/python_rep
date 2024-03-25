#!/usr/bin/env python3
def square(x):
    return x * x
def sqrt(x):
    return x ** 0.5
def divided(x, y):
    return x / y

a = 1
b = -5
c = 6
result = divided(-b + sqrt((square(b) - 4 * a * c)), 2 * a)
print(result)
result = divided(-b - sqrt((square(b) - 4 * a * c)), 2 * a)
print(result)