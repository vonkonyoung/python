def func(n):
    i=0
    while i<n:
        yield i
        i+=1

for i in func(10):
    print(i)

print("bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
def fab(max):
    n,a,b=0,0,1
    while n<max:
        print(b)
        a,b=b,a+b
        n=n+1

fab(5)

