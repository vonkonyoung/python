n=int(input("请输入结束的数:"))
i=1
su=0
for element in range(n+1):
    su+=element
print("从1到%d相加的结果：%d"%(n,su))