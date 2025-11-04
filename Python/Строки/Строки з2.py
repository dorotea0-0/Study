a=input()
f='0123456789'
result=[]
num_str=""
for c in a:
    if c in f:
        num_str=num_str+c
    else:
        k=int(num_str)if num_str else 1
        result.append(c*k)
        num_str=""
print("".join(result))