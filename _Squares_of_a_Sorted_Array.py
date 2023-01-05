n=int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
    m+=[i*i]
m.sort()
for j in m:
    print(j,end=" ")