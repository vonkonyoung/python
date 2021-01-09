class Student(object):

    __pri="这是私有变量"
    def __init__(self,name,tell):
        self.name=name
        self.tell=tell

    def print_tell(self):
        print("%s:%s"%(self.name,self.tell))

big=Student("Bigben",65290)
print(big.name)
print(big.tell)
big.print_tell()