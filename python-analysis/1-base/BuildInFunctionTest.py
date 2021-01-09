li=[1,3,4,5]
new_list=map(lambda a:a+100,li)
print(new_list)
print(list(new_list))

print(list(filter(lambda x:x>3,li)))
from functools import reduce
print(reduce(lambda x,y:x+y,li))
print(sum(li))