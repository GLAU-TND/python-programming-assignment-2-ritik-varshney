x=['chair','height','racket','touch','tunic']
p=[]
for i in x:
    if i.startswith('c'):
        p.append(i)
    elif i.startswith('r'):
        p.insert(1,i)
    elif i.startswith('to'):
        p.insert(2,i)
    elif i.startswith('h'):
        p.insert(3,i)
    elif i.startswith('tu'):
        p.insert(4,i)
print('input',x)
print('output',p)
