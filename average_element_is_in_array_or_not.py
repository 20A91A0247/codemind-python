n=int(input())
l=list(map(int,input().split()))
a=int(sum(l)/n)
c=0
for i in l:
    if i==a:
        c=c+1
print(c!=0)