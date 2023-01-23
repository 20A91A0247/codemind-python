n=int(input())
l=list(map(int,input().split()))
k=int(input())
a=[]
for i in l:
    if(l.count(i)==k):
        a.append(i)
z=set(a)
aa=list(z)
aa.sort()
if(a==[]):
    print(-1)
else:
    for i in aa:
        print(i,end=" ")