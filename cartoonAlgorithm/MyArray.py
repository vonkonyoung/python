class MyArray:
    def __init__(self,capacity):
        self.array=[None]*capacity
        self.size=0

    def insert(self,index,element):
        #判断访问下标是否超出范围
        if index<0 or index>self.size:
            raise Exception("超出数组实际元素范围")
        #如果实际元素达到数组容量上限，数组扩容
        if self.size >=len(self.array):
            self.resize()
        #从右向左循环，逐个元素向右挪一位
        for i in range(self.size-1,-1,-1):
            self.array[i+1]=self.array[i]
        #腾出的位置放入新元素
        self.array[index]=element
        self.size+=1

    def output(self):
        for i in range(self.size):
            print(self.array[i])

    def resize(self):
        arrary_new=[None]*len(self.array)*2
        #从旧数组复制到新数组
        for i in range(self.size):
            arrary_new[i]=self.array[i]
        self.array=arrary_new

    def remove(self,index):
        #判断访问小标是否超出范围
        if index <0 or index >=self.size:
            raise  Exception("超出数组实际元素范围")
        #从左到右，逐个元素向左挪动一位
        for i in range(index,self.size):
            self.array[i]=self.array[i+1]
        self.size-=1


my_array=MyArray(4)
my_array.insert(0,10)
my_array.insert(0,11)
my_array.insert(0,15)
my_array.insert(0,16)
my_array.insert(2,17)
my_array.output()
print(len(my_array.array))
