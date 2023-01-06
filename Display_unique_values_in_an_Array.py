n=int(input())
l=list(map(int,input().split()))
a=l
s=set(a)
ll=list(s)
k=[]
for i in l:
    if l.count(i)==1:
        k.append(i)
if(k==[]):
    print(-1)
else:
    print(*k)