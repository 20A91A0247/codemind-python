n=int(input())
l=list(map(int,input().split()))
z=l.count(0)
l1=[]
for i in l:
    if i!=0:
        l1.append(i)
for i in range(z):
    l1.append(0)
print(*l1)