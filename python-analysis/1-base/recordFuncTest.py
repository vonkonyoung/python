def func(fun,args):
    fun(args)

def f1(x):
    print("这是f1函数:",x)

def f2(x):
    print("这是f2函数:",x)

func(f1,1)
func(f2,"hello")