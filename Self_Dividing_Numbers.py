n=int(input())
m=int(input())
k=[]
for i in range(n,m+1):
    i=str(i)
    c=0
    for j in i:
        if int(j)%10!=0 and int(i)%int(j)==0:
            c=c+1
        if c==len(i):
            k.append(i)
print(*k)