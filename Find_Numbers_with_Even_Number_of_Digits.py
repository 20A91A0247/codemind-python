n=int(input())
l=list(map(int,input().split()))
c=0
for i in l:
    s=str(i)
    if len(s)%2==0:
        c=c+1
print(c)