try:
    # 1/0
    print("正常代码")
except Exception as e:
    print("代码出现除0异常，这里进行处理")
else:
    print("这句话将被输出")
finally:
    print("这句话一定执行")
print("我还在执行")