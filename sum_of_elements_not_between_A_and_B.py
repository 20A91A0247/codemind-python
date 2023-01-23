n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
f=0
s=0
for i in l:
    if(i<a or i>b):
        f=f+1
        s=s+i
if(f!=0):
    print(s)
else:
    print(0)