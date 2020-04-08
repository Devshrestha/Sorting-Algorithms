import random

inp=[10,78,9]
arr=[]
if inp[1]>inp[2]:
    temp=inp[2]
    inp[2]=inp[1]
    inp[1]=temp
for x in range(inp[0]):        
    arr.append(random.randrange(inp[1],inp[2]))

print(arr)