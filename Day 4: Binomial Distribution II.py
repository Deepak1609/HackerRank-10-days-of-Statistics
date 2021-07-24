# from math import factorial
# r, p = map(float, input().split())
# def comb(n, r):
#     return factorial(n) / (factorial(r) * factorial(n - r))
# print(round(sum([comb(p, i) * (r / 100)**i * ((100 - r) / 100)**(p - i)  for i in range(0, 3)]), 3))
# print(round(sum([comb(p, i) * (r / 100)**i * ((100 - r) / 100)**(p - i)  for i in range(2, 11)]), 3))



def fact(n):
    return 1 if n == 0 else n*fact(n-1)

def comb(n, x):
    return fact(n) / (fact(x) * fact(n-x))

def b(x, n, p):
    return comb(n, x) * p**x * (1-p)**(n-x)

p, n = list(map(int, input().split(" ")))
print(round(sum([b(i, n, p/100) for i in range(3)]), 3))
print(round(sum([b(i, n, p/100) for i in range(2, n+1)]), 3))
