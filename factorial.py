# Define a function that returns Factorial of a number.

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
num=int(input())
print(fact(num))
