import math
n=int(input())
l=list(map(int,input().split()))
m=math.floor(n/2)
a=l[:m]
b=l[m:]
c=sum(a)
d=sum(b)
print(c)
print(d)