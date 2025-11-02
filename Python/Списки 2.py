f=[ int(i) for i in input('Введите воследовательность 0 и 1:').split()]
g=0
for t in range(0,len(f)):
    if f[t]==0:
        g+=1
print(g)

