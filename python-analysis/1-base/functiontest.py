def f(x,y):
    z=x**2+y**2
    return z

def func(name,*args):
    print(name+" 有以下雅称:")
    for i in args:
        print(i)

def func2(**kwargs):
    print(type(kwargs))
    for i in kwargs:
        print(i,kwargs[i])

print(f(2,3))
func("赵钱孙","猴子","毛毛","赵学霸")
func2(x=1,y=2,z="hello")
