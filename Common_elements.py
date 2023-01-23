a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
p=[]
for i in l1:
    if(i in l2):
        p.append(i)
l=[]
for i in p:
    if i not in l:
        l.append(i)
print(*l)