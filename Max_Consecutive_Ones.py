n=int(input())
l=list(map(int,input().split()))
c=0
k=[]
for i in l:
    if i==1:
        c=c+1
    else:
        k.append(c)
        c=c-c
k.append(c)
print(max(k))