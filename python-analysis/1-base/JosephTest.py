def move(man,sep):
    """"
      将man列表向左移动sep单位，最左边的元素向列表后面添加
      相当于队列顺时针移动
    """
    for i in range(sep):
        item=man.pop(0)
        man.append(item)

def play(man=41,sep=3,rest=2):
    """"
    man:玩家个数
    sep:杀死数到的第几个人
    rest:幸存者
    """
    print("总共%d个人，每报数到第%d的人自杀，最后剩余%d个人"%(man,sep,rest))
    man=[i for i in range(1,man+1)]
    print("玩家队列：",man)
    sep-=1
    while len(man) > rest:
        move(man,sep)
        print("kill",man.pop(0))
    return man
service=play()
print("最后逃生的人编号：",service)