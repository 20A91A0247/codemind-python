n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
s=[]
f=0
for i in l:
    if(i<a or i>b):
        f=f+1
        s.append(i)
if(f!=0):
    print(max(l))
else:
    print(-1)
#print(max(l))