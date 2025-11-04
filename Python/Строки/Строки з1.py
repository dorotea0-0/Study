a=input()
b=input()
n=len(b)
shifts=set()
for i in range(n):
    shift=b[i:]+b[:i]
    shifts.add(shift)
const=0
for i in range(len(a)-n+1):
    sub=a[i:i+n]
    if sub in shifts:
        const+=1
print(const)