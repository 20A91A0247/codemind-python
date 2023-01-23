a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
p=[]
for i in l1:
    if(i not in l2):
        p.append(i)
for i in l2:
    if(i not in l1):
        p.append(i)
print(*p)