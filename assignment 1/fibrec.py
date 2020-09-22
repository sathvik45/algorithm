def fib(n):
    if n<0:
        print("Invalid")
    if n<2:
        return n
    else:
        return fib(n-1)+fib(n-2)


print(fib(5))
print(fib(10))
print(fib(100))
print(fib(300))
print(fib(500))
