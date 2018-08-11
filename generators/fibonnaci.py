def fib(max):
    a,b = 0,1
    while a < max:
        yield a
        a, b = b, a + b

max = input("Please enter max number")
for n in fib(int(max)):
    print(n, end=' ')


list(fib(int(max)))
