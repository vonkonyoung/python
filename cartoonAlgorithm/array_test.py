
my_list=[2,3,7,4,6]
#查询
print(my_list[0])
#更新
my_list[0]=100
print(my_list[0])
#插入:变更数组的长度
my_list.insert(0,200)
print(my_list[0])
print(list(my_list))

from cartoonAlgorithm import MyArray
my_array=MyArray(4)
my_array.insert(0,10)
my_array.output()





