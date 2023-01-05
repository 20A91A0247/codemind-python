n=int(input())
l=list(map(int,input().split()))
nn=int(input())
ll=list(map(int,input().split()))
q=int(input())
c=0
for i in range(len(l)):
    if(q in range(l[i],ll[i]+1)):
        c=c+1
print(c)