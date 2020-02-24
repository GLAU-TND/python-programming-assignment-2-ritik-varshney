x=[10,7,76,415]
s=[]
for i in x:
    if i<=9:
        s.insert(0,i)
    elif i>=11 and i<=100:
        s.insert(1,i)
    elif i>=100 and i<=999:
        s.insert(2,i)
    elif i>=10 and i<=11:
        s.insert(3,i)
for i in s:
    print(i,end="")
