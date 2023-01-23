n=int(input())
l=list(map(int,input().split()))
e=[]
for i in l:
    if(i==l.count(i)):
        e.append(i)
e.sort()
if(e==[]):
    print(-1)
else:
    print(e[0],end=" ")
    print(e[-1])