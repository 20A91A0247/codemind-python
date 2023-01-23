n=int(input())
l=list(map(int,input().split()))
c=0
cc=0
for i in l:
    if i%2==0:
        cc=cc+1
for i in range(n):
    if(i%2==0) and (l[i]%2==0):
        c=c+1
print(c==cc)