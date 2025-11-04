n=int(input("Введите часы работа:"))
f=[int(i) for i in input("Введите число поситителей в час:").split()]
k=int(input("Сколько длится час-пик:"))
q=[]
for x in range(0,n-(k-1)):
    s=f[x]
    h=x
    for d in range(k-1):
        s=s+f[h+1]
        h=h+1
    q=q+[s]
print(max(q))

