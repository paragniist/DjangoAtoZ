
inp=int(input()) 
l= len(str(inp))
s=str(inp)

cnt=0
for i in s:
    cnt=int(i)+cnt
print(cnt)
    
cnt2=0    
for k in range(0,l):  
    for j in range(k,l):
        print(k,j)
    
result = inp+cnt

print("result",result)