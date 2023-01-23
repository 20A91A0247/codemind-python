n=int(input())
l=list(map(int,input().split()))
a=[]
x = set(l)
for i in x:
    if (i==l.count(i)):
        a.append(i)
if(len(a)==0):
    print(-1)
else:
    z=sum(a)/len(a)
    print("%.2f"%z)