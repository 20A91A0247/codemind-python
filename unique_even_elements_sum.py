n=int(input())
l=list(map(int,input().split()))
a=[]
s=0
for i in l:
    if(i%2==0):
        s=s+i
        a.append(i)
z=set(a)
ss=list(z)
print(sum(ss))