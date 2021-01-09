def fib(n):
    if n<=2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

for i in range(1,10):
    print("fib(%s)=%s"%(i,fib(i)))
