def say(word):
    def name(name):
        print(word,name)

    return name


hi=say("你好")
hi("小明")

print("==========================================")
def func():
    res=[]
    def put(x):
        res.append(x)
    def get():
        return res
    return put,get

p,g=func()
p(1)
p(2)
print(g())
print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
f=lambda x,y:x+y
print(f(2,3))
print((lambda x,y:x**2+y**2)(3,4))